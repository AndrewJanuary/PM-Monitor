import serial, pytest

from app.offline import Offline

def test_init():
    offline_mode = Offline('pm25_filename', 'pm10_filename')
    assert offline_mode.pm_two_five_file == 'pm25_filename'
    assert offline_mode.pm_ten_file == 'pm10_filename'