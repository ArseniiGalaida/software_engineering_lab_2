# З лабораторної №1. Відповідає за збереження поїздок у MySQL.

from ..models import Ride
from .base import RideRepository


class MySQLRideRepository(RideRepository):
    def save(self, ride: Ride) -> None:
        print(f"Saving ride {ride.id} to MySQL Database...")
