# Завдання №2–3. Відповідає за запис старту поїздки в журнал аналітики; записує через стратегію повторів, отриману в конструкторі.

from ..models import Ride
from ..retry.base import RetryStrategy
from .base import RideObserver


class AnalyticsObserver(RideObserver):
    def __init__(self, retry: RetryStrategy) -> None:
        self._retry = retry

    def notify(self, ride: Ride) -> None:
        self._retry.send(self._send, ride)

    def _send(self, ride: Ride) -> None:
        print(f"[ANALYTICS] ride {ride.id} started, total={ride.total}")
