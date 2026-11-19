# Завдання №2–3. Відповідає за SMS-сповіщення пасажира про старт поїздки з даними водія; надсилає через стратегію повторів, отриману в конструкторі.

from ..models import Ride
from ..retry.base import RetryStrategy
from .base import RideObserver


class SmsObserver(RideObserver):
    def __init__(self, retry: RetryStrategy) -> None:
        self._retry = retry

    def notify(self, ride: Ride) -> None:
        self._retry.send(self._send, ride)

    def _send(self, ride: Ride) -> None:
        print(f"Sending SMS to {ride.passenger_phone}: ride {ride.id} started. The driver is: {ride.driver_name}, {ride.driver_phone}")
