import logging

import chargebee
from chargebee import InvalidRequestError

from product_catalog.item.item import Item


class ItemPrice(Item):

    def __init__(self, item_family_id: str = None, item_id: str = None, item_prise_id: str = None):
        super().__init__(item_family_id, item_id)
        self._item_prise_id = item_prise_id

    def create(self, values: dict) -> chargebee.ItemPrice:
        try:
            default_values = {
                "item_id": self._item_id
            }
            values.update(default_values)

            result = chargebee.ItemPrice.create(values)
            item_price = result.item_price
            logging.info(f"CREATED_ITEM_PRICE__ID::  {item_price.id}")
            return item_price
        except InvalidRequestError as exc:
            logging.exception(exc)
            raise

    def retrieve(self) -> chargebee.ItemPrice:
        result = chargebee.ItemPrice.retrieve(self._item_prise_id)
        return result.item_price

    def retrieve_all(self, params: dict = None):
        return chargebee.ItemPrice.list(params)

    def find_applicable_items(self, limit: int = 10, offset: int = 0):
        # Todo add test case
        params = {
            "limit": limit,
            "offset": offset
        }
        return chargebee.ItemPrice.find_applicable_items(self._item_prise_id, params)

    def find_applicable_item_prices(self, limit: int = 10, offset: int = 0):
        # Todo add test case
        params = {
            "limit": limit,
            "offset": offset
        }
        return chargebee.ItemPrice.find_applicable_item_prices(self._item_prise_id, params)

    def update(self, values: dict) -> chargebee.ItemPrice:
        result = chargebee.ItemPrice.update(self._item_prise_id, values)
        return result.item_price

    def delete(self) -> chargebee.ItemPrice:
        result = chargebee.ItemPrice.delete(self._item_prise_id)
        return result.item_price


class PlanItem(Item):
    _type = "plan"


class AddonItem(Item):
    _type = "addon"


class ChargeItem(Item):
    _type = "charge"
