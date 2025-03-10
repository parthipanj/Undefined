import logging

import chargebee
from chargebee import InvalidRequestError

from entitlement.entitlement import Entitlement


class Feature(Entitlement):

    def __init__(self, feature_id: str = None):
        self.__feature_id = feature_id

    def create(self, values: dict) -> chargebee.Feature:
        try:
            result = chargebee.Feature.create(values)
            feature = result.feature
            logging.info(f"CREATED_FEATURE__ID::  {feature.id}")
            return feature
        except InvalidRequestError as exc:
            logging.exception(exc)
            raise

    def retrieve(self) -> chargebee.Feature:
        result = chargebee.Feature.retrieve(self.__feature_id)
        return result.feature

    def retrieve_all(self, params: dict = None):
        return chargebee.Feature.list(params)

    def update(self, values: dict) -> chargebee.Feature:
        result = chargebee.Feature.update(self.__feature_id, values)
        return result.feature

    def activate(self) -> chargebee.Feature:  # Todo add test case
        result = chargebee.Feature.activate(self.__feature_id)
        return result.feature

    def archive(self) -> chargebee.Feature:
        result = chargebee.Feature.archive(self.__feature_id)
        return result.feature

    def reactive(self) -> chargebee.Feature:  # Todo add test case
        result = chargebee.Feature.reactivate(self.__feature_id)
        return result.feature

    def delete(self) -> chargebee.Feature:
        result = chargebee.Feature.delete(self.__feature_id)
        return result.feature
