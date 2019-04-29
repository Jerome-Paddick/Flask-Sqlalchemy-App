from app import app
from flask import request
from flask import make_response
from flask import jsonify
from app.models import Products, VatRates
from app.exchange_rate import get_exchange_rate
from sqlalchemy import exc

@app.route('/', methods=['GET'])
def index():
    return "SERVER IS RUNNING"


@app.route('/order', methods=['GET'])
def return_order():
    if not "order" in request.json:
        return make_response("json not formatted", 400)
    output = []
    for items in request.json["order"]["items"]:
        if not items:
            return make_response("data is empty", 400)
        print("INPUT:", items)
        if items.get("currency"):
            exchange_rate = get_exchange_rate(items["currency"])
            if exchange_rate:
                currency = items["currency"]
            else:
                exchange_rate = 1
                currency = "Incorrect_Currency_Code"
        else:
            exchange_rate = 1
            currency = "N/A"
        product_id = items["product_id"]
        quantity = items["quantity"]
        if quantity < 0:
            return make_response("Quantity Cannot be Negative", 506)
        prod = Products.query.filter(Products.id == product_id).first()
        try:
            print(prod.price, quantity, exchange_rate)
            total_price = (prod.price) * quantity * exchange_rate
        except AttributeError:
            return make_response("INCORRECT ID: " + str(product_id), 505)
        vat_rate = VatRates.query.filter(VatRates.name == prod.vat_band).first().rate
        output.append({"_product_id": product_id,
                       "price": round(total_price),
                       "vat": round(vat_rate*total_price),
                       "price_plus_vat": round(total_price + (vat_rate*total_price)),
                       "currency": currency})
        print("OUTPUT:", output)

    return make_response(jsonify(output))