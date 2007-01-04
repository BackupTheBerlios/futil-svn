
import logging

class FutilLogger:
    
    def __init__(self, name='futil', level=logging.INFO):
        self.logger = logging.getLogger(name)
        hdlr = logging.FileHandler(name + '.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(level)

    def info(self, message):
        self.logger.info(message)
