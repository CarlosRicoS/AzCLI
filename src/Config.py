from abc import abstractmethod
from abc import ABCMeta

class Config(metaclass=ABCMeta):
    @abstractmethod
    def config(self):
        pass