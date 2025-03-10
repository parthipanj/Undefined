import chargebee

from entitlement.entitlement import Entitlement


class SubscriptionEntitlement(Entitlement):
    # Todo add test case

    def subscription_entitlements_for_subscription(self, subscription_id: str, limit: int = 10, offset: int = 0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return chargebee.SubscriptionEntitlement.subscription_entitlements_for_subscription(subscription_id, params)

    def set_subscription_entitlement_availability(self, subscription_id: str, values: dict):
        return chargebee.SubscriptionEntitlement.set_subscription_entitlement_availability(subscription_id, values)
