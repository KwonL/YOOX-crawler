import csv
import locale
import os

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class YooxPipeline:
    def open_spider(self, spider):
        os.makedirs("result", exist_ok=True)
        self.file = open("result/yoox-items.csv", "w")
        self.csv = csv.DictWriter(
            self.file,
            delimiter=",",
            fieldnames=["brand", "name", "price", "image", "url", "code"],
        )
        self.csv.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        try:
            adapter["brand"] = self.clean_text(adapter.get("brand"))
            adapter["name"] = self.clean_text(adapter.get("name"))
            adapter["price"] = int(
                locale.atof(adapter.get("price").split()[1])
            )
            adapter["image"] = adapter.get("image").split("?")[0]
        except Exception:
            DropItem(f"Missing essential properties in {item}")

        self.csv.writerow(adapter.asdict())

        return item

    def clean_text(self, text: str):
        return text.replace("\r", "").replace("\n", "").replace("\t", "")
