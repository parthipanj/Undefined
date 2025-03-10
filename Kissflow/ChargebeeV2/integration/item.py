import logging

from entitlement.item_entitlement import ItemEntitlement
from integration import configure
from product_catalog.item.attach_item import AttachItem
from product_catalog.item.item import Item


def retrieve_plans():
    item_ins = Item()
    params = {
        "limit": 50,
        "offset": None,
        "sort_by[asc]": "name",
        # "item_family_id[is]": plan_id,
        "type[is]": "plan"
    }
    item_entries = item_ins.retrieve_all(params)

    print(item_entries.next_offset)

    for item_entry in item_entries:
        print(item_entry.item)


def retrieve_plan(item_family_id, item_id):
    item_ins = Item(item_family_id, item_id)
    return item_ins.retrieve()


def item_entitlements(item_id: str):
    ins = ItemEntitlement()
    entries = ins.item_entitlements_for_item(item_id, limit=50)
    logging.info(f"ITEM_ENTITLEMENTS__NEXT_OFFSET:: {entries.next_offset}")

    for entry in entries:
        item_entitlement = entry.item_entitlement
        print(item_entitlement)


def retrieve_attached_items(item_family_id, item_id):
    ins = AttachItem(item_family_id, item_id)
    params = {
        "limit": 50,
        "offset": None,
        "sort_by[asc]": "created_at"
    }
    entries = ins.retrieve_all(params)

    for entry in entries:
        attached_item = entry.attached_item
        # print(attached_item)


if __name__ == "__main__":
    _item_family_id = "KF-Red"
    plan_id = "Bronze"
    configure()
    # retrieve_plans()
    # retrieve_plan(item_family_id, item_id)

    item_entitlements(plan_id)
    retrieve_attached_items(_item_family_id, plan_id)
