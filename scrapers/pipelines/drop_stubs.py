from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from ..items import BillStubItem


class DropStubsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("is_stub") or type(item) is BillStubItem or issubclass(type(item), BillStubItem):
            raise DropItem("Dropped stub")

        return item
