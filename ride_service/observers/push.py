# Завдання №4. Відповідає за Push-сповіщення пасажира про старт поїздки з даними водія (новий клас, наявні файли не змінювалися).

from ..models import Ride
from ..retry.base import RetryStrategy
from .base import RideObserver


class PushObserver(RideObserver):
    def __init__(self, retry: RetryStrategy) -> None:
        self._retry = retry

    def notify(self, ride: Ride) -> None:
        self._retry.send(self._send, ride)

    def _send(self, ride: Ride) -> None:
        print(f"Sending PUSH to passenger {ride.passenger_id}: ride {ride.id} started. The driver is: {ride.driver_name}, {ride.driver_phone}")
