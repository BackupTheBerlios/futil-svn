
import logging

class FutilLogger:
    
    def __init__(self, name='futil', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.clear()
        self.hdlr = logging.FileHandler(name + '.log')
        formatter = logging.Formatter('%(asctime)s %(message)s')
        self.hdlr.setFormatter(formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(level)
        
    def clear(self):
        handlers = self.logger.handlers
        for handler in handlers:
            self.logger.removeHandler(handler)

    def info(self, message):
        self.logger.info('INFO: ' + message)
        
    def error(self, message):
        self.logger.error('ERROR: ' + message)
        
    def warn(self, message):
        self.logger.warn('WARN: ' + message)

