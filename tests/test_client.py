import pytest
from random_data.client import BaseClient


@pytest.fixture
def client():
    return BaseClient()


def test_get_addresses(client):
    addresses = client.get_addresses(size=1)
    assert isinstance(addresses, dict)
    assert 'id' in addresses
    assert 'uid' in addresses
    assert 'city' in addresses
    assert 'street_name' in addresses
    assert 'street_address' in addresses
    assert 'secondary_address' in addresses
    assert 'building_number' in addresses
    assert 'mail_box' in addresses
    assert 'community' in addresses
    assert 'zip_code' in addresses
    assert 'zip' in addresses
    assert 'postcode' in addresses
    assert 'time_zone' in addresses
    assert 'street_suffix' in addresses
    assert 'city_suffix' in addresses
    assert 'city_prefix' in addresses
    assert 'state' in addresses
    assert 'state_abbr' in addresses
    assert 'country' in addresses
    assert 'country_code' in addresses
    assert 'latitude' in addresses
    assert 'longitude' in addresses
    assert 'full_address' in addresses


def test_get_appliances(client):
    appliances = client.get_appliances(size=1)
    assert isinstance(appliances, dict)
    'id' in appliances
    'uid' in appliances
    'brand' in appliances
    'equipment' in appliances


def test_get_banks(client):
    banks = client.get_banks(size=1)
    assert isinstance(banks, dict)
    assert 'id' in banks
    assert 'uid' in banks
    assert 'account_number' in banks
    assert 'iban' in banks
    assert 'bank_name' in banks
    assert 'routing_number' in banks
    assert 'swift_bic' in banks


def test_get_beers(client):
    beers = client.get_beers(size=1)
    assert isinstance(beers, dict)
    assert 'id' in beers
    assert 'uid' in beers
    assert 'brand' in beers
    assert 'name' in beers
    assert 'style' in beers
    assert 'hop' in beers
    assert 'yeast' in beers
    assert 'malts' in beers
    assert 'ibu' in beers
    assert 'alcohol' in beers
    assert 'blg' in beers


def test_get_blood_types(client):
    blood_types = client.get_blood_types(size=1)
    assert isinstance(blood_types, dict)
    assert 'id' in blood_types
    assert 'uid' in blood_types
    assert 'type' in blood_types
    assert 'rh_factor' in blood_types
    assert 'group' in blood_types


def test_get_credit_cards(client):
    credit_cards = client.get_credit_cards(size=1)
    assert isinstance(credit_cards, dict)
    assert 'id' in credit_cards
    assert 'uid' in credit_cards
    assert 'credit_card_number' in credit_cards
    assert 'credit_card_expiry_date' in credit_cards
    assert 'credit_card_type' in credit_cards


def test_get_users(client):
    users = client.get_users(size=1)
    assert isinstance(users, dict)
    assert 'id' in users
    assert 'uid' in users
    assert 'password' in users
    assert 'first_name' in users
    assert 'last_name' in users
    assert 'username' in users
    assert 'email' in users
    assert 'avatar' in users
    assert 'gender' in users
    assert 'phone_number' in users
    assert 'social_insurance_number' in users
    assert 'date_of_birth' in users
    assert 'employment' in users
    assert 'address' in users
    assert 'credit_card' in users
    assert 'subscription' in users
