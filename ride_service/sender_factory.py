# Завдання №4. Відповідає за створення готового Observer'а з правильною стратегією за ідентифікатором каналу (Factory Method).

from collections.abc import Callable

from .observers.base import RideObserver
from .observers.email import EmailObserver
from .observers.push import PushObserver
from .observers.sms import SmsObserver
from .retry.exponential_backoff import ExponentialBackoffStrategy
from .retry.fixed_delay import FixedDelayStrategy
from .retry.no_retry import NoRetryStrategy


class SenderFactory:
    _creators: dict[str, Callable[[], RideObserver]] = {
        "email": lambda: EmailObserver(ExponentialBackoffStrategy()),
        "sms": lambda: SmsObserver(NoRetryStrategy()),
        "push": lambda: PushObserver(FixedDelayStrategy()),
    }

    def create(self, channel: str) -> RideObserver:
        try:
            return self._creators[channel]()
        except KeyError:
            raise ValueError(f"Unknown channel: {channel}") from None
