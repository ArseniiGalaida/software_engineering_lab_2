# З лабораторної №1. Відповідає за інтерфейс стратегії знижки (DiscountStrategy).

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float: ...
