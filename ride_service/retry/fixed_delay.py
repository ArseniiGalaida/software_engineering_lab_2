# Завдання №4. Відповідає за повтори з фіксованою паузою між спробами (новий клас, наявні файли не змінювалися).

import time

from ..models import Ride
from .base import RetryStrategy, Sender


class FixedDelayStrategy(RetryStrategy):
    def __init__(self, max_attempts: int = 3, delay: float = 0.1) -> None:
        self._max_attempts = max_attempts
        self._delay = delay

    def send(self, sender: Sender, ride: Ride) -> None:
        for attempt in range(1, self._max_attempts + 1):
            try:
                sender(ride)
                return
            except ConnectionError as error:
                print(f"  attempt {attempt}/{self._max_attempts} failed: {error}")
                if attempt < self._max_attempts:
                    time.sleep(self._delay)
        print(f"  giving up on ride {ride.id} after {self._max_attempts} attempts")
