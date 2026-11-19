# З лабораторної №1. Відповідає за оплату криптовалютою (Coinbase).

from .base import PaymentProcessor


class CryptoPayment(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processing crypto payment for {amount}")
        # Coinbase API call...
