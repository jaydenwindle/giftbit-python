import os
import pytest
import vcr
from giftbit import GiftbitClient

@pytest.fixture
def brand_keys():
    return ['brand', 'info']

@pytest.fixture
def brand_list_keys():
    return ['brands', 'info', 'number_of_results', 'limit', 'offset', 'total_count']

def assert_is_valid_giftbit_response(response, is_list=False):
    """
    Verifies that the given response matches Giftbit's conventions
    """

    assert isinstance(response['info'], dict)
    assert isinstance(response['info']['code'], str)

    if is_list:
        assert isinstance(response['number_of_results'], int)
        assert isinstance(response['limit'], int)
        assert isinstance(response['offset'], int)
        assert isinstance(response['total_count'], int)


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

    result = client.ping()

    print(result)

    assert 'error' in result

@vcr.use_cassette('tests/vcr_cassettes/ping-success.yml')
def test_ping_success():
    """
    Tests an API call which determines authentication status
    using correct credentials
    """

    client = GiftbitClient(api_key="correct_test_key")

    result = client.ping()

    assert not 'error' in result

@vcr.use_cassette('tests/vcr_cassettes/list-brands.yml')
def test_list_brands():
    """
    Tests an API call which determines authentication status
    using correct credentials
    """

    client = GiftbitClient(api_key='correct_test_key')

    result = client.list_brands()

    assert_is_valid_giftbit_response(result, is_list=True)

    assert isinstance(result['brands'], list)

    first_brand = result['brands'][0]
    assert isinstance(first_brand['brand_code'], str)
    assert isinstance(first_brand['name'], str)
    assert isinstance(first_brand['disclaimer'], str)
    assert isinstance(first_brand['image_url'], str)


@vcr.use_cassette('tests/vcr_cassettes/get-brand.yml')
def test_get_brand():
    """
    Tests an API call which determines authentication status
    using correct credentials
    """

    client = GiftbitClient(api_key='correct_test_key')

    result = client.get_brand('amazonus')

    assert_is_valid_giftbit_response(result)

    assert isinstance(result['brand'], dict)

    first_brand = result['brand']
    print(first_brand)
    assert isinstance(first_brand['brand_code'], str)
    assert isinstance(first_brand['name'], str)
    assert isinstance(first_brand['disclaimer'], str)
    assert isinstance(first_brand['image_url'], str)
    assert isinstance(first_brand['regions'], list)
    assert isinstance(first_brand['fund_currencyisocode'], str)
    assert isinstance(first_brand['variable_price'], bool)
    assert isinstance(first_brand['min_price_in_cents'], int)
    assert isinstance(first_brand['max_price_in_cents'], int)

