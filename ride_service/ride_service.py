# Завдання №2. Відповідає за старт поїздки і роль Subject: зберігає підписників і сповіщає кожного через notify(ride).

from collections.abc import Mapping

from .discounts.base import DiscountStrategy
from .models import Ride
from .observers.base import RideObserver
from .payments.base import PaymentProcessor
from .repositories.base import RideRepository


class RideService:
    def __init__(
        self,
        discounts: Mapping[str, DiscountStrategy],
        payment: PaymentProcessor,
        repository: RideRepository,
    ) -> None:
        self._discounts = discounts
        self._payment = payment
        self._repository = repository
        self._observers: list[RideObserver] = []

    def subscribe(self, observer: RideObserver) -> None:
        self._observers.append(observer)

    def start_ride(self, ride: Ride) -> None:
        if not ride.fare_items:
            raise ValueError("Ride has no fare items")

        subtotal = sum(item.price for item in ride.fare_items)
        strategy = self._discounts.get(ride.passenger_type)
        ride.total = strategy.apply(subtotal) if strategy else subtotal

        self._payment.pay(ride.total)
        self._repository.save(ride)

        for observer in self._observers:
            observer.notify(ride)
