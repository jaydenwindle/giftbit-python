import os
import pytest
from giftbit import GiftbitClient

def test_init_env():
    """Test client intialization from API key stored in env var"""
    key = 'test_key_env'
    os.environ["GIFTBIT_API_KEY"] = key

    client = GiftbitClient()

    assert client.api_key == key


def test_init_key():
    """Test client intialization from API key passed to client"""
    key = 'test_key'

    client = GiftbitClient(api_key=key)

    assert client.api_key == key

def test_ping_warning():
    """
    Tests an API call which determines authentication status
    using incorrect credentials
    """

    client = GiftbitClient(api_key="test_key")

    with pytest.warns(Warning):
        result = client.ping()
        assert result == False

def test_ping_success():
    """
    Tests an API call which determines authentication status
    using correct credentials
    """

    client = GiftbitClient(api_key="")

    with pytest.warns(Warning) as record:
        result = client.ping()
        assert result == True
        assert not record.list
