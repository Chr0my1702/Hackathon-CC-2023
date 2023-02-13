import configparser

config = configparser.ConfigParser()

config.read('config.ini')

def ammend_config(key, value):
    config.set('ALL', key, value)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def get_config(key):
    return config.get('ALL', key)