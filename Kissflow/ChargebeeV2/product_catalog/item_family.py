import logging

import chargebee
from chargebee import InvalidRequestError

from product_catalog.product_catalog import ProductCatalog


class ItemFamily(ProductCatalog):

    def __init__(self, item_family_id: str = None):
        self._item_family_id = item_family_id

    def create(self, values: dict) -> chargebee.ItemFamily:
        try:
            result = chargebee.ItemFamily.create(values)
            item_family = result.item_family
            logging.info(f"CREATED_ITEM_FAMILY__ID::  {item_family.id}")
            return item_family
        except InvalidRequestError as exc:
            logging.exception(exc)
            raise

    def retrieve(self) -> chargebee.ItemFamily:
        result = chargebee.ItemFamily.retrieve(self._item_family_id)
        return result.item_family

    def retrieve_all(self, params: dict = None):
        return chargebee.ItemFamily.list(params)

    def update(self, values: dict) -> chargebee.ItemFamily:
        result = chargebee.ItemFamily.update(self._item_family_id, values)
        return result.item_family

    def delete(self) -> chargebee.ItemFamily:
        result = chargebee.ItemFamily.delete(self._item_family_id)
        return result.item_family
