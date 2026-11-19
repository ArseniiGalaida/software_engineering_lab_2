# З лабораторної №1. Відповідає за знижку 20% для VIP-пасажирів.

from .base import DiscountStrategy


class VipDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * (1 - 0.2)
