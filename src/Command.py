import inject
import subprocess
from ICommand import ICommand
from ILogger import ILogger
from Logger import Logger


class Command(ICommand):
    @inject.autoparams()
    def __init__(self, logger: ILogger):
        self.logger = logger
    
    def runCommand(self, config): 
        result = subprocess.run(   
            config, 
            capture_output=True, 
            text=True
        )
        self.logger.log(result)



# # Usage
# client = Client()
# client.do_work()
