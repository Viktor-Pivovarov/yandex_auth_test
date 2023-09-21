import configparser

config = configparser.ConfigParser()
config.read('./config/config.ini')

wait_time = int(config['General']['WaitTime'])
