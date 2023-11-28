import requests


class BaseClient():
    """A client session

    Provides persistent session to Random Data API V2 endpoint

    Basic Usage::
     >>> import random_data.client
     >>> c = client.BaseClient()
     >>> c.get_users(size=1)
    """
    url = 'https://random-data-api.com/api/v2/'

    def __init__(self) -> None:
        pass

    def _send_request(self, resource: str, size: int = 1) -> dict:
        """Sends a GET request.

        :param resource: API resource endpoint name
        :param size: Number of records to return
        :return: :class:`Response <Response>` json() object
        :rtype: dict
        """
        if size > 100:
            raise ValueError('Result size must be 100 or less')

        response = requests.request(
            method='GET',
            url=f'{self.url}/{resource}',
            params={'size': size}
        )
        response.raise_for_status()
        return response.json()

    def get_addresses(self, size: int) -> dict:
        return self._send_request(resource='addresses', size=size)

    def get_appliances(self, size: int) -> dict:
        return self._send_request(resource='appliances', size=size)

    def get_banks(self, size: int) -> dict:
        return self._send_request(resource='banks', size=size)

    def get_beers(self, size: int) -> dict:
        return self._send_request(resource='beers', size=size)

    def get_blood_types(self, size: int) -> dict:
        return self._send_request(resource='blood_types', size=size)

    def get_credit_cards(self, size: int) -> dict:
        return self._send_request(resource='credit_cards', size=size)

    def get_users(self, size: int) -> dict:
        return self._send_request(resource='users', size=size)
