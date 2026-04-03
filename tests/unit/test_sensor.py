import serial, pytest
from serial import SerialException
from unittest.mock import Mock, patch

from app.sensor import Sensor

valid_message = [b'\xaa', b'\xc0', b'\x13', b'\x00', b'5', b'\x00', b'\xd6', b'(', b'F', b'\xab']
invalid_startbyte = [b'\xab', b'\xc0', b'\x13', b'\x00', b'5', b'\x00', b'\xd6', b'(', b'F', b'\xab']
invalid_receivebyte = [b'\xaa', b'\xc1', b'\x13', b'\x00', b'5', b'\x00', b'\xd6', b'(', b'F', b'\xab']
invalid_checksum = [b'\xaa', b'\xc0', b'\x13', b'\x00', b'5', b'\x00', b'\xd6', b'(', b'G', b'\xab']
pm_two_five_out_of_range = [b'\xaa', b'\xc0', b'\x10', b'\x27', b'5', b'\x00', b'\xd6', b'(', b'j', b'\xab']
pm_ten_out_of_range = [b'\xaa', b'\xc0', b'\x13', b'\x00', b'\x10', b'\x27', b'\xd6', b'(', b'H', b'\xab']
startbyte = b'\xaa'
endbyte = b'0xAB'
receivebyte = b'\xc0'

def test_get_pm_two_five():
    sen = Sensor('Test sensor name string', '/dir/serialport', startbyte, endbyte, receivebyte)
    two_five_value = sen.get_pm_two_five(valid_message)
    assert two_five_value == 1.9

def test_get_pm_ten():
    sen = Sensor('Test sensor name string', '/dir/serialport', startbyte, endbyte, receivebyte)
    ten_value = sen.get_pm_ten(valid_message)
    assert ten_value == 5.3

def test_connect_to_sensor(caplog):
    sen = Mock()
    sen.name = 'test'
    sen.port = 'test'
    # sen = Sensor('Test sensor name string', port, startbyte, endbyte, receivebyte)
    sen.connect_to_sensor.return_value = '123'
    assert sen.connect_to_sensor(sen.port)== ('123')
    assert sen.connect_to_sensor.called_once()

def test_sensor_service_init_values():
    sen = Sensor('Test sensor name string', '/dir/serialport', startbyte, endbyte, receivebyte)
    assert sen.name == 'Test sensor name string'
    assert sen.port == '/dir/serialport'
    assert sen.startbyte ==  startbyte
    assert sen.endbyte == endbyte
    assert len(sen.data) == 0

def test_connection_failure_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.connect_to_sensor(sen.port)
    assert e_info.type == SerialException
    assert "Sensor connection failed" in str(e_info.value)

def test_read_from_sensor_failure_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.read_from_sensor()
    assert "Read from sensor failed" in str(e_info.value)

def test_check_message_valid_message():
    sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
    assert sen.check_message(valid_message) == valid_message

def test_invalid_startbyte_failure_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.check_message(invalid_startbyte)
    assert "Unexpected startbyte" in str(e_info.value)

def test_invalid_receivebyte_failure_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.check_message(invalid_receivebyte)
    assert "Unexpected recievebyte" in str(e_info.value)

def test_invalid_checksum_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.check_message(invalid_checksum)
    assert "Checksum mismatch" in str(e_info.value)

def test_pm_two_five_out_of_range_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.get_pm_two_five(pm_two_five_out_of_range)
    assert "PM2.5 reading" in str(e_info.value)
    assert "exceeds maximum valid value" in str(e_info.value)

def test_pm_ten_out_of_range_raises_exception():
    with pytest.raises(Exception) as e_info:
        sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
        sen.get_pm_ten(pm_ten_out_of_range)
    assert "PM10 reading" in str(e_info.value)
    assert "exceeds maximum valid value" in str(e_info.value)

def test_warm_up_sleeps_for_warmup_seconds():
    sen = Sensor('Test sensor name string', '/testdir/testserialport', startbyte, endbyte, receivebyte)
    with patch('app.sensor.time.sleep') as mock_sleep:
        sen.warm_up()
        mock_sleep.assert_called_once_with(30)