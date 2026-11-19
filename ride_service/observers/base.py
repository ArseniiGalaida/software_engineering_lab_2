# Завдання №2. Відповідає за інтерфейс спостерігача (RideObserver), який RideService сповіщає про старт поїздки.

from abc import ABC, abstractmethod

from ..models import Ride


class RideObserver(ABC):
    @abstractmethod
    def notify(self, ride: Ride) -> None: ...
