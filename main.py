# Завдання №2–4. Відповідає за налаштування застосунку: підписку каналів на RideService (вручну і через SenderFactory) та демонстрацію стратегій повторів.

from ride_service.discounts.standard import StandardDiscount
from ride_service.discounts.vip import VipDiscount
from ride_service.models import FareItem, Ride
from ride_service.observers.analytics import AnalyticsObserver
from ride_service.observers.email import EmailObserver
from ride_service.observers.sms import SmsObserver
from ride_service.payments.credit_card import CreditCardPayment
from ride_service.repositories.mysql import MySQLRideRepository
from ride_service.retry.exponential_backoff import ExponentialBackoffStrategy
from ride_service.retry.no_retry import NoRetryStrategy
from ride_service.ride_service import RideService

# Завдання 4: нові модулі
from ride_service.retry.fixed_delay import FixedDelayStrategy
from ride_service.sender_factory import SenderFactory


def make_ride(ride_id: str) -> Ride:
    return Ride(
        id=ride_id,
        passenger_id="P-42",
        passenger_type="VIP",
        fare_items=[FareItem("Base fare", 50.0), FareItem("Distance 12 km", 150.0)],
        passenger_email="passenger@example.com",
        passenger_phone="+380501112233",
        driver_name="Тарас",
        driver_email="driver@example.com",
        driver_phone="+380674445566",
    )


def make_service() -> RideService:
    return RideService(
        discounts={"VIP": VipDiscount(), "Standard": StandardDiscount()},
        payment=CreditCardPayment(),
        repository=MySQLRideRepository(),
    )


def flaky_sender(failures: int):
    """Імітує збій мережі: перші `failures` викликів падають з ConnectionError."""
    calls = {"count": 0}

    def send(ride: Ride) -> None:
        calls["count"] += 1
        if calls["count"] <= failures:
            raise ConnectionError("network is unreachable")
        print(f"  sent for ride {ride.id} on call #{calls['count']}")

    return send


def main() -> None:
    print("=== Завдання 2–3: ручна підписка (Email / SMS / Analytics) ===")
    service = make_service()
    service.subscribe(EmailObserver(ExponentialBackoffStrategy()))
    service.subscribe(SmsObserver(NoRetryStrategy()))
    service.subscribe(AnalyticsObserver(ExponentialBackoffStrategy()))
    service.start_ride(make_ride("R-1"))

    print("\n=== Завдання 4: підписка через SenderFactory (Email / Push) ===")
    factory = SenderFactory()
    service = make_service()
    for channel in ("email", "push"):
        service.subscribe(factory.create(channel))
    service.subscribe(AnalyticsObserver(ExponentialBackoffStrategy()))
    service.start_ride(make_ride("R-2"))

    print("\n=== Стратегії повторів при збої мережі (2 невдалі спроби) ===")
    ride = make_ride("R-3")
    for strategy in (ExponentialBackoffStrategy(), NoRetryStrategy(), FixedDelayStrategy()):
        print(f"{type(strategy).__name__}:")
        strategy.send(flaky_sender(failures=2), ride)


if __name__ == "__main__":
    main()
