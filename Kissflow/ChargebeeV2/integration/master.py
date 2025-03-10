import logging

from integration import configure
from product_catalog.item.item import Item
from product_catalog.item.item_price import ItemPrice
from product_catalog.item_family import ItemFamily


def retrieve_item_families(filter_ids: list = None):
    item_family_ins = ItemFamily()
    params = {
        "limit": 50,
        "offset": None,
        "sort_by[asc]": "name"
    }
    if filter_ids:
        params["id[in]"] = filter_ids

    entries = item_family_ins.retrieve_all(params)
    logging.info(f"ITEM_FAMILY__NEXT_OFFSET:: {entries.next_offset}")
    return entries


def retrieve_items(item_type="plan"):
    item_ins = Item()
    params = {
        "limit": 50,
        "offset": None,
        "sort_by[asc]": "name",
        "item_family_id[in]": item_family_ids,
        "type[is]": item_type
    }
    entries = item_ins.retrieve_all(params)

    logging.info(f"ITEM__NEXT_OFFSET:: {entries.next_offset}")
    return entries


def retrieve_item_prices(item_type="plan"):
    item_ins = ItemPrice()
    params = {
        "limit": 50,
        "offset": None,
        "sort_by[asc]": "created_at",
        "item_id[in]": plan_ids,
        "item_type[is]": item_type
    }
    entries = item_ins.retrieve_all(params)

    logging.info(f"ITEM_PRICE__NEXT_OFFSET:: {entries.next_offset}")
    return entries


if __name__ == "__main__":
    configure()

    item_family_ids = []
    item_families = []
    item_family_entries = retrieve_item_families(["KF-Red"])
    for item_family_entry in item_family_entries:
        item_family = item_family_entry.item_family
        item_family_ids.append(item_family.id)
        values = {
            "id": item_family.id,
            "name": item_family.name,
            "description": item_family.description,
            "status": item_family.status
        }
        item_families.append(item_family.values)

    plan_ids = []
    plans = {}
    plan_entries = retrieve_items()
    for plan_entry in plan_entries:
        plan = plan_entry.item
        plan_ids.append(plan.id)
        values = {
            "id": plan.id,
            "name": plan.name,
            "external_name": plan.external_name,
            "description": plan.description,
            "status": plan.status
        }
        plans.setdefault(plan.item_family_id, []).append(plan.values)

    plan_prices = {}
    plan_prices_entries = retrieve_item_prices()
    for plan_price_entry in plan_prices_entries:
        plan_price = plan_price_entry.item_price
        values = {
            "id": plan_price.id,
            "name": plan_price.name,
            "external_name": plan_price.external_name,
            "description": plan_price.description,
            "status": plan_price.status
        }
        plan_prices.setdefault(plan_price.item_id, []).append(plan_price.values)

    master = {
        "ItemFamily": item_families,
        "Plan": plans,
        "PlanPrice": plan_prices
    }

    print(master)
