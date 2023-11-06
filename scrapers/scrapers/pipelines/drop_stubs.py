from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from ..items import BillStub


class DropStubsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("is_stub") or type(item) is BillStub or issubclass(type(item), BillStub):
            raise DropItem("Dropped stub")

        return item
