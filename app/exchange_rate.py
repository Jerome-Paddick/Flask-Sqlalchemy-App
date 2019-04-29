from app.models import ExchangeRates, ApiKeys

import datetime
import requests


def exchange_rate_api(country_code):
    query = ApiKeys.query.filter(ApiKeys.name == "free_curr_conv").first()
    url = query.url
    api_key = query.api_key
    r = requests.get(url=url,
                     params={"q": "GBP_" + country_code,
                             "apiKey": api_key,
                             "compact": "ultra"})
    if r.status_code == 200:
        print(r.json())
        return r.json()["GBP_" + country_code]
    else:
        return False


def get_exchange_rate(country_code):
        rate = ExchangeRates.query.filter(ExchangeRates.country_code == country_code).first()
        if not rate:
            return None
        elif datetime.datetime.now() - rate.last_updated >  datetime.timedelta(days=1):
            current_rate = exchange_rate_api(country_code)
            rate.exchange_rate = current_rate
            print("current rate", current_rate)
            return current_rate
        else:
            rate.exchange_rate = exchange_rate_api(country_code)
            return rate.exchange_rate



