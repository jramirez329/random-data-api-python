# Random Data API Client

## Description

This is a Python client for interacting with [Random Data API](https://random-data-api.com/). It provides a simple way to call the API endpoints for V2.

## Installation

You can install the Random Data API client via `pip3`

```bash
pip3 install random-data-api
```

## Usage

Here's an example of how to use the `BaseClient` class and functions:

```python3
from random_data.client import BaseClient

client = BaseClient()

users = client.get_users(size=2)

print(users)
```

## Documentation

For more detailed information about the API and its endpoints, please refer to the official documentation ([here](https://random-data-api.com/documentation)).


## Contributing

We welcome contributions! Please see our contributing guidelines for more details.