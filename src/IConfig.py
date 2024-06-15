from abc import abstractmethod
from abc import ABCMeta

class IConfig(metaclass=ABCMeta):
    @abstractmethod
    def config(self):
        pass