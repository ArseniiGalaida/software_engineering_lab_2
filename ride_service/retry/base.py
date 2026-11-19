# Завдання №3. Відповідає за інтерфейс стратегії повторних спроб (RetryStrategy).

from abc import ABC, abstractmethod
from collections.abc import Callable

from ..models import Ride

Sender = Callable[[Ride], None]


class RetryStrategy(ABC):
    @abstractmethod
    def send(self, sender: Sender, ride: Ride) -> None:
        """Викликає sender(ride); при ConnectionError повторює згідно зі стратегією."""
