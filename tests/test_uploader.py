import sys
from app.uploader import Uploader
from Adafruit_IO import RequestError
from unittest.mock import Mock
import io

def test_upload_service_init_values():
    up = Uploader('target name')
    assert up.target == 'target name'
    assert len(up.data) == 0

def test_upload_service_read_config():
    up = Uploader('target name')
    file='tests/test_config.yml'
    username, key, pm_two_five, pm_ten = up.read_config(file)
    assert username == 'test user'
    assert key == 'abc123'
    assert pm_two_five == 'pm-two-five'
    assert pm_ten == 'pm-ten'

def test_get_feeds_empty(caplog):
    aio = Mock()
    up = Uploader('target name')
    aio.feeds.return_value= None
    up.get_feeds(aio)
    assert "No feeds found" in caplog.text

    # Mocks the AIO client
    # Mocks the feed object returned from AIO client
    # Checks get_feeds() stdout output contains feed details
def test_get_feeds(capsys):
    aio = Mock()
    feed = Mock()
    feed.name= 'test feed name'
    feed.description= 'test feed description'
    up = Uploader('target name')
    aio.feeds.return_value = {feed}
    
    up.get_feeds(aio)
    captured = capsys.readouterr()
    assert "Getting available feeds...\n\nFound 1 feeds:\n\n" in captured.out
    assert feed.name in captured.out
    assert feed.description in captured.out

def test_get_feed_meta():
    aio = Mock()
    feed = Mock()
    feed.name= 'test feed name'
    up = Uploader('target name')
    assert up.get_feed_meta(aio, feed.name)

def test_retrieve_from_feed():
    aio = Mock()
    feed = Mock()
    feed.name= 'test feed name'
    up = Uploader('target name')
    assert up.retrieve_from_feed(aio, feed)
