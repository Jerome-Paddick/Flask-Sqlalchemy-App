from app import db
from app.models import Products, VatRates, ExchangeRates, ApiKeys
import json


def update():
    prices_data = json.load(open("json_data/prices.json"))

    for price in prices_data["prices"]:
        p = Products(id=price["product_id"],
                     price=price["price"],
                     vat_band=price["vat_band"])
        db.session.add(p)

    for name, rate in prices_data["vat_bands"].items():
        v = VatRates(name=name,
                     rate=rate)
        db.session.add(v)

    country_codes = json.load(open("json_data/country_code.json", errors="ignore")).keys()
    for code in country_codes:
        e = ExchangeRates(country_code=code,
                          exchange_rate=None)
        db.session.add(e)


    api_keys = json.load(open("json_data/api_keys.json"))
    for api in api_keys:
        api = ApiKeys(name=api["name"],
                      api_key=api["api_key"],
                      url=api["url"])
        db.session.add(api)

    db.session.commit()

update()
