import logging

import chargebee
from chargebee import InvalidRequestError

from product_catalog.item.item import Item


class AttachItem(Item):

    def __init__(self, item_family_id: str, item_id: str, attached_item_id: str = None):
        super().__init__(item_family_id, item_id)
        self.__attached_item_id = attached_item_id

    def create(self, values: dict) -> chargebee.AttachedItem:
        try:
            result = chargebee.AttachedItem.create(self._item_id, values)
            attached_item = result.attached_item
            logging.info(f"CREATED_ATTACHED_ITEM__ID::  {attached_item.id}")
            return attached_item
        except InvalidRequestError as exc:
            logging.exception(exc)
            raise

    def retrieve(self) -> chargebee.AttachedItem:
        params = {
            "parent_item_id": self._item_id
        }
        result = chargebee.AttachedItem.retrieve(self.__attached_item_id, params)
        return result.attached_item

    def retrieve_all(self, params: dict = None):
        return chargebee.AttachedItem.list(self._item_id, params)

    def update(self, values: dict) -> chargebee.AttachedItem:
        default_values = {
            "parent_item_id": self._item_id
        }
        values.update(default_values)
        result = chargebee.AttachedItem.update(self.__attached_item_id, values)
        return result.attached_item

    def delete(self) -> chargebee.AttachedItem:
        params = {
            "parent_item_id": self._item_id
        }
        result = chargebee.AttachedItem.delete(self.__attached_item_id, params)
        return result.attached_item
