from scrapers.exporters import OpenStatesJsonItemExporter
from scrapy.utils.log import logger
from scrapy import signals
import os


def clean_whitespace(obj):
    """deep whitespace clean for ScrapeObj & dicts"""
    if isinstance(obj, dict):
        items = obj.items()
        use_setattr = False
    elif isinstance(obj, object):
        items = obj.__dict__.items()
        use_setattr = True

    for k, v in items:
        if isinstance(v, str) and v:
            newv = v.strip()
        elif isinstance(v, list) and v:
            if not v:
                continue
            elif isinstance(v[0], str):
                newv = [i.strip() for i in v]
            elif isinstance(v[0], (dict, object)):
                newv = [clean_whitespace(i) for i in v]
            else:
                raise ValueError(
                    f"Unhandled case, {k} is list of {type(v[0])}")
        else:
            continue

        if use_setattr:
            setattr(obj, k, newv)
        else:
            obj[k] = newv

    return obj


class SaveObjectsPipeline:
    def __init__(self, stats):
        self.stats = stats
        self.base_dir = '_data'

    @classmethod
    def from_crawler(cls, crawler):
        s = cls(crawler.stats)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        logger.info('Spider opened: %s' % spider.name)
        start_dt = self.stats.get_value('start_time').strftime('%Y-%m-%d')

        today_run_cnt = 1

        state_name = spider.name.replace('-bills', '')
        self.datadir = f"{self.base_dir}/{state_name}/{start_dt}"

        if os.path.exists(self.datadir):
            sub_dirs = [name for name in os.listdir(
                self.datadir) if os.path.isdir(os.path.join(self.datadir, name))]
            today_run_cnt = len(sub_dirs) + 1

        self.datadir = f"{self.datadir}/{today_run_cnt}"
        if not os.path.exists(self.datadir):
            os.makedirs(self.datadir)

    def save_object(self, obj, spider):
        clean_whitespace(obj)

        obj.pre_save(spider.jurisdiction.jurisdiction_id)

        filename = f"{obj._type}_{obj._id}.json".replace("/", "-")
        file_path = os.path.join(self.datadir, filename)

        logger.info(f"save {obj._type} as {filename}")

        with open(file_path, "w+b") as f:
            exporter = OpenStatesJsonItemExporter(f)
            exporter.export_item(obj.as_dict())

    def process_item(self, item, spider):
        """
        Save object to disk as JSON.

        Generally shouldn't be called directly.
        """
        self.save_object(item, spider)
        # validate after writing, allows for inspection on failure
        try:
            item.validate()
        except ValueError as ve:
            logger.warn(ve)
        # after saving and validating, save subordinate objects
        for obj in item._related:
            self.save_object(obj, spider)

        return item
