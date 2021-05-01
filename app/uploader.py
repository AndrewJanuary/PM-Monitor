from Adafruit_IO import Client, AdafruitIOError, RequestError
import logging
import yaml


class Uploader:

    def __init__(self, target):
        self.target = target
        self.data = []

    def read_config(self, file):
        logging.debug('Reading config file')
        try:
            with open(file, 'r') as ymlfile:
                config = yaml.load(ymlfile, Loader=yaml.SafeLoader)
            return config['aio']['username'], config['aio']['key'], config['aio']['feeds']['pm-two-five'], \
                config['aio']['feeds']['pm-ten']
        except FileNotFoundError:
            message = 'Config file not found'
            logging.error(message)
            raise Exception(message)

    def connect_to_aio(self, username, key):
        try:
            aio = Client(username, key)
            logging.info('Created AIO client')
            return aio
        except AdafruitIOError:
            message = 'Ada fruit IO Client creation failed'
            logging.error(message)
            raise Exception(message)

    def send_to_aio(self, aio, feed_name, data):
        aio.send(feed_name, data)

    def get_feeds(self, aio):
        print("Getting available feeds...\n")
        try:
            feeds = aio.feeds()
            if feeds is not None:
                print(str.format("Found {0} feeds:\n", len(feeds)))
                for feed in feeds:
                    print(str.format("{0} - {1}", feed.name, feed.description))
            else:
                logging.error('No feeds found')
        except RequestError:
            logging.error('Get feeds failed')

    def get_feed_meta(self, aio, feed_name):
        try:
            meta = aio.feeds(feed_name)
            return meta
        except RequestError:
            logging.error('Get feed metadata failed')

    def retrieve_from_feed(self, aio, feed):
        try:
            data = aio.receive(feed)
            return data
        except RequestError:
            logging.error('Retrieve data from feed failed')

