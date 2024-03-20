from scrapy import exporters
from scrapy.utils.python import to_bytes
from scrapy.exporters import BaseItemExporter
from scrapers.utils import OpenStatesJSONEncoder


class OpenStatesJsonItemExporter(exporters.JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, **kwargs)
        self.encoder = OpenStatesJSONEncoder(**self._kwargs)


class OpenStatesCloudStorageJsonItemExporter(BaseItemExporter):
    def __init__(self, client, bucket, path, **kwargs):
        super().__init__(dont_fail=True, **kwargs)
        self.client = client
        self.bucket = bucket
        self.path = path
        self._kwargs.setdefault("ensure_ascii", not self.encoding)
        self.encoder = OpenStatesJSONEncoder(**self._kwargs)

    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict) + "\n"

        bucket = self.client.bucket(self.bucket)
        blob = bucket.blob(self.path)
        blob.upload_from_string(data)
