import requests

url = "http://127.0.0.1:5000/order"
order = {
    "order": {
        "id": 12345,
        "customer": {},
        "items": [
            {
                "product_id": 1,
                "quantity": 1
            },
            {
                "product_id": 2,
                "quantity": 5,
                "currency": "USD"
            },
            {
                "product_id": 3,
                "quantity": 1
            }
        ]
    }
}

r = requests.post(url, json=order)
print(r)
print(r.text)