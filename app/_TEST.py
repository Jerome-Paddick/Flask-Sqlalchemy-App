


unit_tests = {  "normal":               [{"product_id": 1,
                                        "quantity": 1,
                                        "currency": "GBP"}],
                "multiple_products":    [{"product_id": 1,
                                        "quantity": 1,
                                        "currency": "PHP"
                                        },
                                        {"product_id": 2,
                                        "quantity": 5,
                                        "currency": "USD"
                                        }],
                "fake_currency":        [{"product_id": 3,
                                        "quantity": 1,
                                        "currency": "FAKEVALUE"
                                        }],
                "incorrect_id":         [{"product_id": 80,
                                        "quantity": 1}],
                "negative_quantity":    [{"product_id": 3,
                                        "quantity": -4}],
                "empty":                [{}]}


for critera, test in unit_tests.items():
    import requests
    url = "http://127.0.0.1:5000/order"
    r = requests.get(url, json={"order": {"id": 12345,"customer": {},"items": test}})
    print("|"*50)
    print(critera)
    print(r.status_code)
    print(r.text)