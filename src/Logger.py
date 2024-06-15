from ILogger import ILogger

class Logger(ILogger):
    def log(self, message):
        print('stdout:', message.stdout)
        print('stderr:', message.stderr)