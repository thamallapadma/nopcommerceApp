import configparser
import os
from pathlib import *

class ReadConfig:
    def __init__(self):
        self.temp_dir = str(Path(__file__).parent.parent)
        self.tag_file = os.path.join(self.temp_dir, 'Configurations', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.tag_file)
        self.url = self.config['LOGIN_CREDENTIALS']['baseURL']
        self.user = self.config['LOGIN_CREDENTIALS']['username']
        self.password = self.config['LOGIN_CREDENTIALS']['password']
        self.rootpath = self.config['ROOTPATH']['root_path']
