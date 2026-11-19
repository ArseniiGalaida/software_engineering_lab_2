# З лабораторної №1. Відповідає за знижку 30% для Corporate-пасажирів.

from .base import DiscountStrategy


class CorporateDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * (1 - 0.3)
