import sys
import serial, logging
from Adafruit_IO import Client
from serial import SerialException


class Sensor():

    def __init__(self, name, port, startbyte, endbyte, receivebyte):
        self.name = name
        self.data = []
        self.port = port
        self.startbyte = startbyte
        self.endbyte = endbyte
        self.receivebyte = receivebyte

    def connect_to_sensor(self, port):
        try:
            ser = serial.Serial(port)
            logging.info(str.format('Connected to {0}', ser.name))
            return ser
        except SerialException:
            tb = sys.exc_info()[2]
            message = 'Sensor connection failed'
            logging.error(message)
            raise SerialException(message).with_traceback(tb)

    def read_from_sensor(self):
        try:
            ser = self.connect_to_sensor(self.port)
            self.data = []
            for index in range(0, 10):
                datum = ser.read()
                self.data.append(datum)
            return self.data
        except Exception:
            message = 'Read from sensor failed'
            logging.error(message)
            raise Exception(message)

    def get_pm_two_five(self, data):
        pm_two_five = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
        return pm_two_five


    def get_pm_ten(self, data):
        pm_ten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
        return pm_ten

        ##TODO Checksum on message
        ## Sanity check values for PM
    def check_message(self,data):
        if data[0] != self.startbyte:
            message = str.format('Unexpected startbyte {0} received from sensor. Expected {1}', data[0], self.startbyte)
            logging.error(message)
            raise Exception(message)
        if data[1] != self.receivebyte:
            message = str.format('Unexpected recievebyte {0} received from sensor. Expected {1}', data[1], self.receivebyte)
            logging.error(message)
            raise Exception(message)
        return data


    def print_data(self):
        data = self.read_from_sensor()
        pm_two_five = self.get_pm_two_five(data)
        pm_ten = self.get_pm_ten(data)

        print("PM 2.5: " + str(pm_two_five) + "0.1g/M3")
        print("PM 10: " + str(pm_ten) + "0.1g/M3")
