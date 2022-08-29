import logging
import os
import random
import string
from datetime import datetime
from Utilities.readproperties import ReadConfig

class CommonHelper(object):
    def __init__(self):
        self.data = ReadConfig()

    def time_stamp_generator(self):
        '''
        Function generates current time time stamp
        :return: timestamp string
        '''
        current_time = datetime.now().strftime("%d%m%y%H%M%S")
        return (current_time)

    def get_logger(self):
        logging.basicConfig(filename=('.//Logs/logfile.log'),
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger =logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    def random_generator(self, size=8,chars=string.ascii_lowercase+string.digits):
         return ''.join(random.choice(chars) for x in range(size))