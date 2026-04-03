import pytest
from serial import SerialException
from unittest.mock import Mock
from start import start_online

def xtest_start_online(capsys):
    start()
    captured = capsys.readouterr()
    assert "Starting Air Monitor in offline mode" in captured.out

