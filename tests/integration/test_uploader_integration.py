import sys, pytest
from app.uploader import Uploader

def test_upload_service_read_config(monkeypatch):
    monkeypatch.setenv('AIO_KEY', 'abc123')
    up = Uploader('target name')
    file='tests/integration/test_config.yml'
    username, key, pm_two_five, pm_ten = up.read_config(file)
    assert username == 'test user'
    assert key == 'abc123'
    assert pm_two_five == 'pm-two-five'
    assert pm_ten == 'pm-ten'