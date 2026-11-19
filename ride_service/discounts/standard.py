# З лабораторної №1. Відповідає за знижку 5% для Standard-пасажирів.

from .base import DiscountStrategy


class StandardDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * (1 - 0.05)
