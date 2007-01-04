
import logging

class FutilLogger:
    
    def __init__(self, name='futil', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.hdlr = logging.FileHandler(name + '.log')
        formatter = logging.Formatter('%(asctime)s %(message)s')
        self.hdlr.setFormatter(formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(level)

    def info(self, message):
        self.logger.info(message)
        
    def error(self, message):
        self.logger.error(message)
        
    def warn(self, message):
        self.logger.warn(message)
        
    def __del__(self):
        self.logger.removeHandler(self.hdlr)
        self.hdlr.close() 
