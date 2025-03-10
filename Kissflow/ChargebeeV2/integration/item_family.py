from integration import configure
from product_catalog.item_family import ItemFamily


def retrieve_item_families():
    item_family_ins = ItemFamily()
    params = {
        "limit": 50,
        "offset": None,
        "sort_by[asc]": "name"
    }
    item_family_entries = item_family_ins.retrieve_all(params)

    print(item_family_entries.next_offset)
    for item_family_entry in item_family_entries:
        print(item_family_entry.item_family)


if __name__ == "__main__":
    configure()
    retrieve_item_families()
