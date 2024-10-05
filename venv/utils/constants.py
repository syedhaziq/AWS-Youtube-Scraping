import configparser
import os

parser = configparser.ConfigParser()
print(os.path.dirname(__file__))
#parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))