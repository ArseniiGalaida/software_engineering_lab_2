# З лабораторної №1. Відповідає за інтерфейс збереження поїздок (RideRepository).

from abc import ABC, abstractmethod

from ..models import Ride


class RideRepository(ABC):
    @abstractmethod
    def save(self, ride: Ride) -> None: ...
