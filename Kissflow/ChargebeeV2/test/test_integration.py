import os
import unittest
from unittest import skipIf

import chargebee

from entitlement.feature import Feature
from product_catalog.item.attach_item import AttachItem
from product_catalog.item.item import Item
from product_catalog.item.item_price import ItemPrice
from product_catalog.item_family import ItemFamily


class IntegrationTestCase(unittest.TestCase):
    skip_delete = True
    api_key = os.getenv("TEST_API_KEY")
    site = os.getenv("TEST_SITE", "")

    item_family_id = "KF-Red"

    plan_item = {
        "Plan1": {
            "id": "Bronze",
            "price": {
                "USD": {
                    "Monthly": "Bronze-USD-Monthly",
                    "Yearly": "Bronze-USD-Yearly"
                },
                "IND": {
                    "Monthly": "Bronze-IND-Monthly",
                    "Yearly": "Bronze-IND-Yearly"
                }
            }
        },
        "Plan2": {
            "id": "Silver"
        },
        "Plan3": {
            "id": "Gold"
        }
    }
    addon_item_id = "Analytics"

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        chargebee.configure(cls.api_key, cls.site)

    def _get_plan_id(self, plan: str) -> str:
        return self.plan_item[plan]["id"]

    def _get_plan_ids(self) -> list:
        return [plan["id"] for plan in self.plan_item.values()]

    def _get_plan_price(self, plan) -> dict:
        return self.plan_item[plan]["price"]


class ItemFamilyTestCase(IntegrationTestCase):

    def test_001_create(self):
        ins = ItemFamily()
        item_family = {
            "id": self.item_family_id,
            "name": "KF Red",
            "description": "KF Red Family"
        }
        created_item_family = ins.create(item_family)
        self.assertEqual(created_item_family.id, item_family["id"])

    def test_002_retrieve(self):
        ins = ItemFamily(self.item_family_id)
        item_family = ins.retrieve()
        self.assertEqual(item_family.id, self.item_family_id)

    def test_003_retrieve_all(self):
        ins = ItemFamily()
        item_families = ins.retrieve_all()
        self.assertIsNone(item_families.next_offset)
        item_family = [item_family for item_family in item_families if
                       self.item_family_id == item_family.item_family.id]
        self.assertTrue(item_family.__len__(), 1)

    def test_004_update(self):
        ins = ItemFamily(self.item_family_id)
        item_family = {
            # "name": "KF Dark Red"
            "description": "Kissflow Red Family"
        }
        updated_item_family = ins.update(item_family)
        # self.assertEqual(updated_item_family.name, item_family["name"])
        self.assertEqual(updated_item_family.description, item_family["description"])

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_005_delete(self):
        ins = ItemFamily(self.item_family_id)
        deleted_item_family = ins.delete()
        self.assertEqual(deleted_item_family.id, self.item_family_id)
        self.assertEqual(deleted_item_family.status, "deleted")


class ItemTestCase(IntegrationTestCase):

    def test_001_create__plan_bronze(self):
        ins = Item(self.item_family_id)
        item = {
            "id": self._get_plan_id("Plan1"),
            "type": "plan",
            "name": "Bronze",
            "description": "Bronze Plan",
            # "external_name": "Bronze",
            "item_applicability": "all",
            # "item_applicability": "restricted",
            # "applicable_items": ["day-pass"],
            # "cf_version": 4.0
        }
        created_item = ins.create(item)
        self.assertEqual(created_item.id, item["id"])
        self.assertEqual(created_item.item_family_id, self.item_family_id)
        self.assertEqual(created_item.type, "plan")
        self.assertEqual(created_item.status, "active")

    def test_002_create__plan_silver(self):
        ins = Item(self.item_family_id)
        item = {
            "id": self._get_plan_id("Plan2"),
            "type": "plan",
            "name": "Silver",
            "description": "Silver Plan"
        }
        created_item = ins.create(item)
        self.assertEqual(created_item.id, item["id"])
        self.assertEqual(created_item.item_family_id, self.item_family_id)
        self.assertEqual(created_item.type, "plan")
        self.assertEqual(created_item.status, "active")

    def test_003_create__plan_gold(self):
        ins = Item(self.item_family_id)
        item = {
            "id": self._get_plan_id("Plan3"),
            "type": "plan",
            "name": "Gold",
            "description": "Gold Plan"
        }
        created_item = ins.create(item)
        self.assertEqual(created_item.id, item["id"])
        self.assertEqual(created_item.item_family_id, self.item_family_id)
        self.assertEqual(created_item.type, "plan")
        self.assertEqual(created_item.status, "active")

    def test_004_create__addon(self):
        ins = Item(self.item_family_id)
        item = {
            "id": self.addon_item_id,
            "type": "addon",
            "name": "Analytics",
            "description": "Analytics Addon"
        }
        created_item = ins.create(item)
        self.assertEqual(created_item.id, item["id"])
        self.assertEqual(created_item.item_family_id, self.item_family_id)
        self.assertEqual(created_item.type, "addon")

    def test_005_retrieve(self):
        ins = Item(self.item_family_id, self._get_plan_id("Plan1"))
        item = ins.retrieve()
        self.assertEqual(item.id, self._get_plan_id("Plan1"))

    def test_006_retrieve_all(self):
        ins = Item(self.item_family_id)
        items = ins.retrieve_all()
        self.assertIsNotNone(items.next_offset)
        items = [item for item in items if item.item.id in [*self._get_plan_ids(), self.addon_item_id]]
        self.assertTrue(items.__len__(), 4)

    def test_007_update(self):
        ins = Item(self.item_family_id, self._get_plan_id("Plan1"))
        item = {
            # "name": "Bronze"
            "description": "Kissflow Bronze Plan",
            "enabled_for_checkout": False,
            "enabled_in_portal": False
        }
        updated_item = ins.update(item)
        # self.assertEqual(updated_item.name, item["name"])
        self.assertEqual(updated_item.description, item["description"])
        self.assertEqual(updated_item.enabled_for_checkout, item["enabled_for_checkout"])
        self.assertEqual(updated_item.enabled_in_portal, item["enabled_in_portal"])

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_990_delete__plan_bronze(self):
        ins = Item(self.item_family_id, self._get_plan_id("Plan1"))
        deleted_item = ins.delete()
        self.assertEqual(deleted_item.id, self._get_plan_id("Plan1"))
        self.assertEqual(deleted_item.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_991_delete__plan_silver(self):
        ins = Item(self.item_family_id, self._get_plan_id("Plan2"))
        deleted_item = ins.delete()
        self.assertEqual(deleted_item.id, self._get_plan_id("Plan2"))
        self.assertEqual(deleted_item.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_992_delete__plan_gold(self):
        ins = Item(self.item_family_id, self._get_plan_id("Plan3"))
        deleted_item = ins.delete()
        self.assertEqual(deleted_item.id, self._get_plan_id("Plan2"))
        self.assertEqual(deleted_item.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_992_delete__addon(self):
        ins = Item(self.item_family_id, self.addon_item_id)
        deleted_item = ins.delete()
        self.assertEqual(deleted_item.id, self.addon_item_id)
        self.assertEqual(deleted_item.status, "deleted")


class ItemPriceTestCase(IntegrationTestCase):
    plan_item_price_id = "Bronze-USD-Monthly"
    addon_item_price_id = "Analytics-INR-Yearly"

    def test_001_create__plan_price(self):
        item_id = self._get_plan_id("Plan1")
        ins = ItemPrice(self.item_family_id, item_id)
        item_price = {
            "id": self.plan_item_price_id,
            "name": "Bronze USD Monthly",
            "currency_code": "USD",
            "pricing_model": "per_unit",
            "price": 1000,
            "external_name": "Bronze USD Monthly",
            "period_unit": "month",
            "period": 1
        }
        created_item_price = ins.create(item_price)
        self.assertEqual(created_item_price.id, item_price["id"])
        self.assertEqual(created_item_price.item_family_id, self.item_family_id)
        self.assertEqual(created_item_price.item_id, item_id)
        self.assertEqual(created_item_price.currency_code, "USD")
        self.assertEqual(created_item_price.period, 1)
        self.assertEqual(created_item_price.period_unit, "month")
        self.assertEqual(created_item_price.status, "active")

    def test_002_create__addon_price(self):
        ins = ItemPrice(self.item_family_id, self.addon_item_id)
        item_price = {
            "id": self.addon_item_price_id,
            "name": "Analytics INR Yearly",
            "currency_code": "INR",
            "period": 1,
            "period_unit": "year",
            "pricing_model": "tiered",
            "tiers": [
                {
                    "starting_unit": 1,
                    "ending_unit": 10,
                    "price": 100
                },
                {
                    "starting_unit": 11,
                    "ending_unit": 20,
                    "price": 300
                },
                {
                    "starting_unit": 21,
                    "price": 500
                }
            ]
        }
        created_item_price = ins.create(item_price)
        self.assertEqual(created_item_price.id, item_price["id"])
        self.assertEqual(created_item_price.item_family_id, self.item_family_id)
        self.assertEqual(created_item_price.item_id, self.addon_item_id)
        self.assertEqual(created_item_price.currency_code, "INR")
        self.assertEqual(created_item_price.period, 1)
        self.assertEqual(created_item_price.period_unit, "year")
        self.assertEqual(created_item_price.status, "active")

    def test_003_retrieve(self):
        item_id = self._get_plan_id("Plan1")
        ins = ItemPrice(self.item_family_id, item_id, self.plan_item_price_id)
        item_price = ins.retrieve()
        self.assertEqual(item_price.id, self.plan_item_price_id)

    def test_004_retrieve_all(self):
        item_id = self._get_plan_id("Plan1")
        ins = ItemPrice(self.item_family_id, item_id)
        item_prices = ins.retrieve_all()
        self.assertIsNotNone(item_prices.next_offset)
        item_prices = [item_price for item_price in item_prices if
                       item_price.item_price.id in [self.plan_item_price_id, self.addon_item_price_id]]
        self.assertTrue(item_prices.__len__(), 2)

    def test_005_update(self):
        item_id = self._get_plan_id("Plan1")
        ins = ItemPrice(self.item_family_id, item_id, self.plan_item_price_id)
        item_price = {
            # "name": "Bronze USD Monthly",
            "price": 10000,
            "period": 1,
            "period_unit": "month"
        }
        updated_item_price = ins.update(item_price)
        # self.assertEqual(updated_item_price.name, item_price["name"])
        self.assertEqual(updated_item_price.price, item_price["price"])
        self.assertEqual(updated_item_price.period, item_price["period"])
        self.assertEqual(updated_item_price.period_unit, item_price["period_unit"])

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_991_delete__plan_price(self):
        item_id = self._get_plan_id("Plan1")
        ins = ItemPrice(self.item_family_id, item_id, self.plan_item_price_id)
        deleted_item_price = ins.delete()
        self.assertEqual(deleted_item_price.id, self.plan_item_price_id)
        self.assertEqual(deleted_item_price.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_992_delete__addon_price(self):
        item_id = self._get_plan_id("Plan1")
        ins = ItemPrice(self.item_family_id, item_id, self.addon_item_price_id)
        deleted_item_price = ins.delete()
        self.assertEqual(deleted_item_price.id, self.addon_item_price_id)
        self.assertEqual(deleted_item_price.status, "deleted")


class AttachItemTestCase(IntegrationTestCase):
    __attached_item_id = "f1883230-0512-468c-9cea-af820999bdd2"

    def test_001_create(self):
        item_id = self._get_plan_id("Plan1")
        ins = AttachItem(self.item_family_id, item_id)
        item = {
            "item_id": self.addon_item_id,
            "type": "mandatory",
            "quantity": 1
        }
        attached_item = ins.create(item)
        self.assertIsNotNone(attached_item.id)
        self.assertEqual(attached_item.parent_item_id, item_id)
        self.assertEqual(attached_item.item_id, self.addon_item_id)
        self.assertEqual(attached_item.type, "mandatory")
        self.assertEqual(attached_item.quantity, 1)
        self.assertEqual(attached_item.object, "attached_item")
        self.assertEqual(attached_item.status, "active")

    def test_002_retrieve(self):
        item_id = self._get_plan_id("Plan1")
        ins = AttachItem(self.item_family_id, item_id, self.__attached_item_id)
        attached_item = ins.retrieve()
        self.assertEqual(attached_item.id, self.__attached_item_id)

    def test_003_retrieve_all(self):
        item_id = self._get_plan_id("Plan1")
        ins = AttachItem(self.item_family_id, item_id)
        attached_items = ins.retrieve_all()
        self.assertIsNone(attached_items.next_offset)
        item_prices = [attached_item for attached_item in attached_items if
                       attached_item.attached_item.id in [self.__attached_item_id]]
        self.assertTrue(item_prices.__len__(), 1)

    def test_004_update(self):
        item_id = self._get_plan_id("Plan1")
        ins = AttachItem(self.item_family_id, item_id, self.__attached_item_id)
        item = {
            "type": "recommended"
        }
        attached_item = ins.update(item)
        self.assertEqual(attached_item.type, "recommended")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_991_delete(self):
        item_id = self._get_plan_id("Plan1")
        ins = AttachItem(self.item_family_id, item_id, self.__attached_item_id)
        attached_item = ins.delete()
        self.assertEqual(attached_item.id, self.__attached_item_id)
        self.assertEqual(attached_item.status, "deleted")


class FeatureTestCase(IntegrationTestCase):
    features = {
        "Feature1": {
            "id": "Blood-Red"
        },
        "Feature2": {
            "id": "Brick-Red"
        },
        "Feature3": {
            "id": "Bright-Red"
        },
        "Feature4": {
            "id": "Red"
        }
    }

    def __get_feature_id(self, feature: str) -> str:
        return self.features[feature]["id"]

    def __get_feature_ids(self) -> list:
        return [feature["id"] for feature in self.features.values()]

    def test_001_create__switch(self):
        ins = Feature()
        feature = {
            "id": self.__get_feature_id("Feature1"),
            "name": "Blood Red",
            "type": "switch",
            "description": "Blood Red Feature",
            "status": "active"
        }
        created_feature = ins.create(feature)
        self.assertEqual(created_feature.id, feature["id"])
        self.assertEqual(created_feature.name, feature["name"])
        self.assertEqual(created_feature.type, feature["type"])
        self.assertEqual(created_feature.status, feature["status"])

    def test_002_create__quantity(self):
        ins = Feature()
        feature = {
            "id": self.__get_feature_id("Feature2"),
            "name": "Brick Red",
            "type": "quantity",
            "description": "Brick Red",
            "levels": [
                {
                    "level": 0,
                    "value": "5",
                    "name": "5 Shade"
                },
                {
                    "level": 1,
                    "value": "10",
                    "name": "10 Shade"
                },
                {
                    "level": 2,
                    "value": "Unlimited",
                    "name": "Unlimited Shade",
                    "is_unlimited": True
                }
            ],
            "status": "active"
        }
        created_feature = ins.create(feature)
        self.assertEqual(created_feature.id, feature["id"])
        self.assertEqual(created_feature.name, feature["name"])
        self.assertEqual(created_feature.type, feature["type"])
        # self.assertCountEqual(created_feature.levels, feature["levels"])
        self.assertEqual(created_feature.status, feature["status"])

    def test_003_create__range(self):
        ins = Feature()
        feature = {
            "id": self.__get_feature_id("Feature3"),
            "name": "Bright Red",
            "type": "range",
            "description": "Bright Red",
            "levels": [
                {
                    "level": 0,
                    "value": "5",
                    "name": "5 shade/month"
                },
                {
                    "level": 1,
                    "value": "100",
                    "name": "100 shade/month"
                }
            ],
            "status": "active"
        }
        created_feature = ins.create(feature)
        self.assertEqual(created_feature.id, feature["id"])
        self.assertEqual(created_feature.name, feature["name"])
        self.assertEqual(created_feature.type, feature["type"])
        # self.assertCountEqual(created_feature.levels, feature["levels"])
        self.assertEqual(created_feature.status, feature["status"])

    def test_004_create__custom(self):
        ins = Feature()
        feature = {
            "id": self.__get_feature_id("Feature4"),
            "name": "Red",
            "type": "custom",
            "description": "Red",
            "levels": [
                {
                    "level": 0,
                    "value": "24 * 5",
                    "name": "24 * 5"
                },
                {
                    "level": 1,
                    "value": "24 * 7",
                    "name": "24 * 7"
                }
            ],
            "status": "active"
        }
        created_feature = ins.create(feature)
        self.assertEqual(created_feature.id, feature["id"])
        self.assertEqual(created_feature.name, feature["name"])
        self.assertEqual(created_feature.type, feature["type"])
        # self.assertCountEqual(created_feature.levels, feature["levels"])
        self.assertEqual(created_feature.status, feature["status"])

    def test_005_retrieve(self):
        ins = Feature(self.__get_feature_id("Feature1"))
        feature = ins.retrieve()
        self.assertEqual(feature.id, self.__get_feature_id("Feature1"))

    def test_006_retrieve_all(self):
        ins = Feature()
        features = ins.retrieve_all()
        self.assertIsNone(features.next_offset)
        features = [feature for feature in features if feature.feature.id in self.__get_feature_ids()]
        self.assertTrue(features.__len__(), 4)

    def test_007_update(self):
        ins = Feature(self.__get_feature_id("Feature1"))
        feature = {
            "name": "Blood Red",
            "description": "Blood Red Feature",
            "status": "active"
        }
        updated_feature = ins.update(feature)
        self.assertEqual(updated_feature.name, feature["name"])
        self.assertEqual(updated_feature.description, feature["description"])
        self.assertEqual(updated_feature.status, feature["status"])

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_981_archive__switch(self):
        ins = Feature(self.__get_feature_id("Feature1"))
        archived_feature = ins.archive()
        self.assertEqual(archived_feature.id, self.__get_feature_id("Feature1"))
        self.assertEqual(archived_feature.status, "archived")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_982_archive__quantity(self):
        ins = Feature(self.__get_feature_id("Feature2"))
        archived_feature = ins.archive()
        self.assertEqual(archived_feature.id, self.__get_feature_id("Feature2"))
        self.assertEqual(archived_feature.status, "archived")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_983_archive__range(self):
        ins = Feature(self.__get_feature_id("Feature3"))
        archived_feature = ins.archive()
        self.assertEqual(archived_feature.id, self.__get_feature_id("Feature3"))
        self.assertEqual(archived_feature.status, "archived")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_984_archive__custom(self):
        ins = Feature(self.__get_feature_id("Feature4"))
        archived_feature = ins.archive()
        self.assertEqual(archived_feature.id, self.__get_feature_id("Feature4"))
        self.assertEqual(archived_feature.status, "archived")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_991_delete__switch(self):
        ins = Feature(self.__get_feature_id("Feature1"))
        deleted_feature = ins.delete()
        self.assertEqual(deleted_feature.id, self.__get_feature_id("Feature1"))
        self.assertEqual(deleted_feature.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_993_delete__quantity(self):
        ins = Feature(self.__get_feature_id("Feature2"))
        deleted_feature = ins.delete()
        self.assertEqual(deleted_feature.id, self.__get_feature_id("Feature2"))
        self.assertEqual(deleted_feature.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_993_delete__range(self):
        ins = Feature(self.__get_feature_id("Feature3"))
        deleted_feature = ins.delete()
        self.assertEqual(deleted_feature.id, self.__get_feature_id("Feature3"))
        self.assertEqual(deleted_feature.status, "deleted")

    @skipIf(IntegrationTestCase.skip_delete, "Skipped for local testing.")
    def test_994_delete__custom(self):
        ins = Feature(self.__get_feature_id("Feature4"))
        deleted_feature = ins.delete()
        self.assertEqual(deleted_feature.id, self.__get_feature_id("Feature4"))
        self.assertEqual(deleted_feature.status, "deleted")
