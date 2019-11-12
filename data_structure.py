from dataclasses import dataclass, field


@dataclass
class Tick:
    ask1: float = 0.0
    bid1: float = 0.0
    volume: float = 0.0
    last: float = 0.0
    asks: list = field(default_factory=list)
    bids: list = field(default_factory=list)
    timestamp: int = 0

    def from_dict(self, d: dict):
        for k, v in d.items():
            if k in self.__dict__:
                self.__setattr__(k, v)


class CandleInterval:
    INTERVAL_1M = '1m'
    INTERVAL_5M = '5m'
    INTERVAL_10M = '10m'
    INTERVAL_1H = '1H'


@dataclass
class Candle:
    high: float = 0.0
    low: float = 0.0
    open: float = 0.0
    close: float = 0.0
    timestamp: int = 0
    interval: str = CandleInterval.INTERVAL_1M

    def from_dict(self, d: dict):
        for k, v in d.items():
            if k in self.__dict__:
                self.__setattr__(k, v)
