import os
import warnings
import requests

GIFTBIT_TEST_ROOT = 'https://api-testbed.giftbit.com/papi/v1'
GIFTBIT_PROD_ROOT = 'https://api.giftbit.com/papi/v1'

class GiftbitClient(object):
    """
    The main client for making requests to the Giftbit API
    """

    def __init__(self, api_key=None, testbed=True):
        super(GiftbitClient, self).__init__()

        self.api_key = api_key or os.environ.get('GIFTBIT_API_KEY')
        if not self.api_key:
            raise Exception("API key must be specified in constructor " +
                            " or stored in an environment variable") 

        if testbed:
            self.api_root = GIFTBIT_TEST_ROOT
        else:
            self.api_root = GIFTBIT_PROD_ROOT

        self.auth_header = {'Authorization': 'Bearer {}'.format(self.api_key)}

    def api_url(self, endpoint):
        """
        Returns the full url of an endpoint

        :returns: The full URL of the endpoint
        """

        return '{}/{}'.format(self.api_root, endpoint)

    def ping(self):
        """
        Returns a boolean to indicate whether the API had been correctly configured.
        If the API isn't configured correctly, a warning will be raised with more details.

        :returns: boolean indicating if API is configured correctly or not.
        """

        url = self.api_url('ping')

        return requests.get(url, headers=self.auth_header).json()

    def list_brands(self, **kwargs):
        """
        Returns a list of available brands from the API. 
        """
        url = self.api_url('brands')

        return requests.get(
            url,
            headers=self.auth_header,
            params=kwargs,
        ).json()

    def get_brand(self, brand_code, **kwargs):
        """
        Returns a single brand from the API. 
        """
        url = self.api_url('brands/{}'.format(brand_code))

        return requests.get(
            url,
            headers=self.auth_header,
            params=kwargs,
        ).json()
