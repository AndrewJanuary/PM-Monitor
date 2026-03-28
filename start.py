from app.sensor import Sensor
from app.uploader import Uploader
from app.offline import Offline
import time, logging, argparse, sys

logging.basicConfig(filename='airquality.log', level=logging.DEBUG, filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--offline', action="store_true")

    args = parser.parse_args(sys.argv[2:])

    try:
        sen = Sensor('PM Sensor 1', '/dev/ttyUSB0', b'\xaa', b'0xAB', b'\xc0')
    except Exception as e:
        message = 'Failed to initialise sensor: {0}'.format(e)
        logging.error(message)
        print(message)
        sys.exit(1)

    if args.offline:
        start_offline(sen)
    else:
        try:
            start_online(sen)
        except Exception as e:
            message = 'Online mode failed, falling back to offline mode: {0}'.format(e)
            logging.error(message)
            print(message)
            start_offline(sen)


def start_offline(sen):
    print("Starting Air Monitor in offline mode")
    off = Offline('pm25', 'pm10')
    while True:
        try:
            data = sen.read_from_sensor()
            sen.check_message(data)
            pm_two_five = sen.get_pm_two_five(data)
            pm_ten = sen.get_pm_ten(data)
            off.write_pm_two_five(pm_two_five)
            off.write_pm_ten(pm_ten)
        except Exception as e:
            message = 'Error reading from sensor in offline mode: {0}'.format(e)
            logging.error(message)
            print(message)


def start_online(sen):
    print("Starting Air Monitor")
    file = 'config.yml'
    up = Uploader('AIO')

    try:
        username, key, feed_two_five, feed_ten = up.read_config(file)
    except Exception as e:
        message = 'Failed to read config: {0}'.format(e)
        logging.error(message)
        print(message)
        sys.exit(1)

    try:
        aio = up.connect_to_aio(username, key)
    except Exception as e:
        message = 'Failed to connect to Adafruit IO: {0}'.format(e)
        logging.error(message)
        print(message)
        sys.exit(1)

    while True:
        up.get_feeds(aio)
        data = sen.read_from_sensor()
        sen.check_message(data)
        pm_two_five = sen.get_pm_two_five(data)
        pm_ten = sen.get_pm_ten(data)

        up.send_to_aio(aio, feed_two_five, pm_two_five)
        up.send_to_aio(aio, feed_ten, pm_ten)

        print(up.retrieve_from_feed(aio, feed_two_five))
        print(up.retrieve_from_feed(aio, feed_ten))
        time.sleep(60)
