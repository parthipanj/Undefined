import chargebee

from entitlement.entitlement import Entitlement


class EntitlementOverride(Entitlement):
    # Todo add test case

    def add_entitlement_override_for_subscription(self, subscription_id: str, values: dict):
        return chargebee.EntitlementOverride.add_entitlement_override_for_subscription(subscription_id, values)

    def list_entitlement_override_for_subscription(self, subscription_id: str, limit: int = 10, offset: int = 0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return chargebee.EntitlementOverride.list_entitlement_override_for_subscription(subscription_id, params)
