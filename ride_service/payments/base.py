# З лабораторної №1. Відповідає за інтерфейс обробки платежів (PaymentProcessor).

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None: ...
