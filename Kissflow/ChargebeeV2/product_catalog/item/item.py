import logging

import chargebee
from chargebee import InvalidRequestError

from product_catalog.item_family import ItemFamily


class Item(ItemFamily):

    def __init__(self, item_family_id: str = None, item_id: str = None):
        super().__init__(item_family_id)
        self._item_id = item_id

    def create(self, values: dict) -> chargebee.Item:
        try:
            default_values = {
                "item_family_id": self._item_family_id
            }
            values.update(default_values)

            result = chargebee.Item.create(values)
            item = result.item
            logging.info(f"CREATED_ITEM__ID::  {item.id}")
            return item
        except InvalidRequestError as exc:
            logging.exception(exc)
            raise

    def retrieve(self) -> chargebee.Item:
        result = chargebee.Item.retrieve(self._item_id)
        return result.item

    def retrieve_all(self, params: dict = None):
        return chargebee.Item.list(params)

    def update(self, values: dict) -> chargebee.Item:
        result = chargebee.Item.update(self._item_id, values)
        return result.item

    def delete(self) -> chargebee.Item:
        result = chargebee.Item.delete(self._item_id)
        return result.item
