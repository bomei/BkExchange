from abc import ABCMeta, abstractmethod


class TickDBInterface(metaclass=ABCMeta):
    @abstractmethod
    def generate_tick(self):
        pass
