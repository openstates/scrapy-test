from scrapy.exceptions import IgnoreRequest


class ScoutOnlyDownloaderMiddleware(object):
    def process_request(self, request, spider):
        if "robots.txt" in request.url:
            return None
        elif request.meta.get("is_scout"):
            return None
        else:
            raise IgnoreRequest()
