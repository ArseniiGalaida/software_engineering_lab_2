# Завдання №3. Відповідає за повтори з експоненційною паузою (0.1 → 0.2 → 0.4 с); використовується для Email.

import time

from ..models import Ride
from .base import RetryStrategy, Sender


class ExponentialBackoffStrategy(RetryStrategy):
    def __init__(self, max_attempts: int = 3, base_delay: float = 0.1) -> None:
        self._max_attempts = max_attempts
        self._base_delay = base_delay

    def send(self, sender: Sender, ride: Ride) -> None:
        delay = self._base_delay
        for attempt in range(1, self._max_attempts + 1):
            try:
                sender(ride)
                return
            except ConnectionError as error:
                print(f"  attempt {attempt}/{self._max_attempts} failed: {error}")
                if attempt < self._max_attempts:
                    time.sleep(delay)
                    delay *= 2
        print(f"  giving up on ride {ride.id} after {self._max_attempts} attempts")
