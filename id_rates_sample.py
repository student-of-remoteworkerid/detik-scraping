import requests

# data = requests.get('http://www.floatrates.com/daily/idr.json')

data_currency = \
    {
        "usd": {
            "code": "USD",
            "alphaCode": "USD",
            "numericCode": "840",
            "name": "U.S. Dollar",
            "rate": 0.000069575957224315,
            "date": "Wed, 6 Apr 2022 23:55:01 GMT",
            "inverseRate": 14372.781056766
        },
        "eur": {
            "code": "EUR",
            "alphaCode": "EUR",
            "numericCode": "978",
            "name": "Euro",
            "rate": 0.00006376237100314,
            "date": "Wed, 6 Apr 2022 23:55:01 GMT",
            "inverseRate": 15683.231101158
        },
    }

for currency in data_currency.values():
    print(currency['code'])
    print(currency['name'])
    print(currency['date'])
    print(f"{currency['inverseRate']}\n")
