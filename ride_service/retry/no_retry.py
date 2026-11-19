# Завдання №3. Відповідає за одну спробу без повторів (кожна спроба коштує грошей); використовується для SMS.

from ..models import Ride
from .base import RetryStrategy, Sender


class NoRetryStrategy(RetryStrategy):
    def send(self, sender: Sender, ride: Ride) -> None:
        try:
            sender(ride)
        except ConnectionError as error:
            print(f"  failed, no retry for ride {ride.id}: {error}")
