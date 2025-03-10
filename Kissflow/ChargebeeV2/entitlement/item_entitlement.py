import chargebee

from entitlement.entitlement import Entitlement


class ItemEntitlement(Entitlement):
    # Todo add test case

    def item_entitlements_for_item(self, item_id: str, limit: int = 10, offset: int = 0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return chargebee.ItemEntitlement.item_entitlements_for_item(item_id, params)

    def upsert_or_remove_item_entitlements_for_item(self, item_id: str, values: dict):
        return chargebee.ItemEntitlement.upsert_or_remove_item_entitlements_for_item(item_id, values)

    def item_entitlements_for_feature(self, feature_id: str, limit: int = 10, offset: int = 0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return chargebee.ItemEntitlement.item_entitlements_for_feature(feature_id, params)

    def add_item_entitlements(self, feature_id: str, values: dict):
        return chargebee.ItemEntitlement.add_item_entitlements(feature_id, values)
