import os
import warnings
import requests

GIFTBIT_TEST_ROOT = 'https://api-testbed.giftbit.com/papi/v1'
GIFTBIT_PROD_ROOT = 'https://api.giftbit.com/papi/v1'

class GiftbitClient(object):
    """
    The main client for making requests to the Giftbit API
    """

    def __init__(self, api_key=None, api_root=GIFTBIT_TEST_ROOT):
        super(GiftbitClient, self).__init__()

        self.api_key = api_key or os.environ.get('GIFTBIT_API_KEY')
        if not self.api_key:
            raise Exception("API key must be specified in constructor " +
                            " or stored in an environment variable") 

        self.api_root = api_root
        self.auth_header = {'Authorization': 'Basic {}'.format(self.api_key)}

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

        ping_request = requests.get(self.api_url('ping'), headers=self.auth_header)

        print(ping_request.json())

        if ping_request.status_code != 200:
            warnings.warn(
                "Received status code {} from {}. Are you sure your API key is correct?"
                    .format(ping_request.status_code, self.api_url('ping'))
            )

        return ping_request.status_code == 200
