from scrapy import exporters
from scrapy.utils.python import to_bytes
from scrapers.utils import OpenStatesJSONEncoder


class OpenStatesJsonItemExporter(exporters.JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, **kwargs)
        self.encoder = OpenStatesJSONEncoder(**self._kwargs)
