import serial, pytest
from unittest.mock import Mock

from app.offline import Offline

def test_init():
    offline_mode = Offline('pm25_filename', 'pm10_filename')
    assert offline_mode.pm_two_five_file == 'pm25_filename'
    assert offline_mode.pm_ten_file == 'pm10_filename'

def test_print_pm_two_five(capsys):
    offline_mode = Offline('pm25_filename', 'pm10_filename')
    offline_mode.print_pm_two_five(7.77)
    captured = capsys.readouterr()
    assert "PM 2.5 7.77\n" in captured.out

def test_print_pm_ten(capsys):
    offline_mode = Offline('pm25_filename', 'pm10_filename')
    offline_mode.print_pm_ten(7.77)
    captured = capsys.readouterr()
    assert "PM 10 7.77\n" in captured.out
