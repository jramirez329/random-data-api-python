import requests


class RandomDataClient():
    def __init__(self) -> None:
        self.url = 'https://random-data-api.com/api/v2/'

    def _send_request(self, resource: str, size: int) -> str:
        if size > 100:
            raise ValueError('Result size must be 100 or less')

        response = requests.request(
            method='GET',
            url=f'{self.url}/{resource}',
            params={'size': size}
        )
        response.raise_for_status()
        return response.json()

    def get_addresses(self, size: int) -> str:
        return self._send_request(resource='addresses', size=size)

    def get_appliances(self, size: int) -> str:
        return self._send_request(resource='appliances', size=size)

    def get_banks(self, size: int) -> str:
        return self._send_request(resource='banks', size=size)

    def get_beers(self, size: int) -> str:
        return self._send_request(resource='beers', size=size)

    def get_blood_types(self, size: int) -> str:
        return self._send_request(resource='blood_types', size=size)

    def get_credit_cards(self, size: int) -> str:
        return self._send_request(resource='credit_cards', size=size)

    def get_users(self, size: int) -> str:
        return self._send_request(resource='users', size=size)
