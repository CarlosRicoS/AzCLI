from abc import abstractmethod
from abc import ABCMeta

class ILogger(metaclass=ABCMeta):
    @abstractmethod
    def log(self, message):
        pass