from product_catalog.item.item_price import ItemPrice


class DifferentialPrice(ItemPrice):
    # Todo implementation

    def __init__(self, item_family_id: str, item_id: str, item_prise_id: str, differential_price_id: str = None):
        super().__init__(item_family_id, item_id, item_prise_id)
        self.__differential_price_id = differential_price_id
