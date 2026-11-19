# З лабораторної №1. Відповідає за оплату через PayPal.

from .base import PaymentProcessor


class PayPalPayment(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment for {amount}")
        # PayPal API call...
