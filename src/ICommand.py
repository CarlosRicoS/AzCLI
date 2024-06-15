from abc import abstractmethod
from abc import ABCMeta
import inject

class ICommand(metaclass=ABCMeta):
    
    @abstractmethod
    def runCommand(self, config):
        pass