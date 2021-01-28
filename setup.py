import yaml, os
from Adafruit_IO import Client, AdafruitIOError, RequestError
import logging, argparse, sys

logging.basicConfig(filename='airquality.log', level=logging.DEBUG, filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file = 'config.yml'
default_config = {"aio": {"username": '', "key": '', "feeds": {"pm-two-five": '', "pm-ten": ''}}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--default')
    args = parser.parse_args(sys.argv[2:])

    if args.default:
        write_config(file, default_config)
    else:
        username = input("Enter AIO username: ")
        key = (input("Enter AIO API Key: "))
        pm_two_five = (input("Enter name of PM 2.5 feed: "))
        pm_two_ten = (input("Enter name of PM 10 feed: "))
        config = set_config(username, key, pm_two_five, pm_two_ten)
        write_config(file, config)


def read_config(file):
    logging.debug('Reading config file')
    with open(file, 'r') as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    return config['aio']['username'], config['aio']['key']


def set_config(username, key, pm_two_five, pm_ten):
    config = default_config
    config['aio']['username'] = ("{0}".format(username))
    config['aio']['key'] = key
    config['aio']['feeds']['pm-two-five'] = pm_two_five
    config['aio']['feeds']['pm-ten'] = pm_ten
    return config


def write_config(file, values):
    logging.debug('Writing to config file')
    try:
        with open(file, 'w') as ymlfile:
            yaml.dump(values, ymlfile)
    except Exception:
        logging.error('Write to config file failed')


def connect_to_aio(username, key):
    try:
        aio = Client(username, key)
        logging.info('Created AIO client')
        return aio
    except AdafruitIOError:
        logging.error('Ada fruit IO Client creation failed')
