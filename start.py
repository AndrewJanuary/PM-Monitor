from app.sensor import Sensor
from app.uploader import Uploader
from app.offline import Offline
import time, logging, argparse, sys, random, datetime

logging.basicConfig(filename='airquality.log', level=logging.DEBUG, filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

sen = Sensor('PM Sensor 1', '/dev/ttyUSB0', b'\xaa', b'0xAB', b'\xc0')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--offline', action="store_true")

    args = parser.parse_args(sys.argv[2:])

    if args.offline:
        start_offline()
    else:
        try:
            start_online()
        except:
            start_offline()

def start_offline():
    print("Starting Air Monitor in offline mode")
    off = Offline('pm25', 'pm10')
    while True:
        data = sen.read_from_sensor()
        sen.check_message(data)
        pm_two_five = sen.get_pm_two_five(data)
        pm_ten = sen.get_pm_ten(data)
        off.write_pm_two_five(pm_two_five)
        off.write_pm_ten(pm_ten)

def start_online():
    print("Starting Air Monitor")
    file = 'config.yml'
    up = Uploader('AIO')
    username, key, feed_two_five, feed_ten = up.read_config(file)
    aio = up.connect_to_aio(username, key)
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
