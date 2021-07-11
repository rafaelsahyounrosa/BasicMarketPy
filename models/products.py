from utils.helper import format_float_str_currency


class Product:
    count: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__product_id: int = Product.count
        self.__name: str = name
        self.__price: float = price
        Product.count += 1

    @property
    def product_id(self: object) -> int:
        return self.__product_id

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Product ID: {self.product_id} \nName: {self.name} \nPrice: {format_float_str_currency(self.price)}'
