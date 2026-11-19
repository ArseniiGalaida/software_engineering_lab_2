# З лабораторної №1. Відповідає за оплату кредитною карткою (Stripe).

from .base import PaymentProcessor


class CreditCardPayment(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment for {amount}")
        # Stripe API call...
