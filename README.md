# giftbit-python

A Python SDK for GiftBit's API.

## Installation
```bash
$ pip install giftbit
```

## Getting Started 

### API Credentials
The `GiftbitClient` needs your Giftbit credentials. You can pass them into the constructor
or use the environment variable `GIFTBIT_API_KEY`.
```python
from giftbit import GiftbitClient

client = GiftbitClient(api_key="<your api key here>")

# or using the environment variable
client = GiftbitClient()
```

By default, the `GiftbitClient` uses Giftbit's testbed API. To use the production API server, do the following: 
```python
from giftbit import GiftbitClient

client = GiftbitClient(testbed=False)
```

You can check to see if the client is configured correctly by using the ping method
```python
from giftbit import GiftbitClient

client = GiftbitClient(testbed=False)

result = client.ping()

print(result)
```

## Brands 

### List Brands 

```python
from giftbit import GiftbitClient

client = GiftbitClient()

result = client.list_brands()

for brand in result['brands']:
    print(brand['name'])
```

### Get Individual Brand

```python
from giftbit import GiftbitClient

client = GiftbitClient()

result = client.get_brand('amazonus')

print(result['brand'])
```

## Regions 
Not implemented yet

## Campaigns 
Not implemented yet

## Funds 
Not implemented yet

## Gifts 
Not implemented yet

## Links 
Not implemented yet
