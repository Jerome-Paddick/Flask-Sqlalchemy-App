from app import app
from flask import request
from flask import make_response
from flask import jsonify
from app.models import Products, VatRates
from app.exchange_rate import get_exchange_rate


@app.route('/', methods=['GET'])
def index():
    return "SERVER IS RUNNING"


@app.route('/order', methods=['POST'])
def return_order():
    if not request.json or not "order" in request.json:
        return make_response("no json recieved", 400)
    output = []
    for items in request.json["order"]["items"]:
        print("INPUT:", items)
        if items.get("currency"):
            exchange_rate = get_exchange_rate(items["currency"])
            currency = items["currency"]
        else:
            exchange_rate = 1
            currency = None
        product_id = items["product_id"]
        quantity = items["quantity"]
        prod = Products.query.filter(Products.id == product_id).first()
        print(prod.price, quantity, exchange_rate)
        total_price = (prod.price)*quantity*exchange_rate
        vat_rate = VatRates.query.filter(VatRates.name == prod.vat_band).first().rate
        output.append({"_product_id": product_id,
                       "price": round(total_price),
                       "vat": round(vat_rate*total_price),
                       "price_plus_vat": round(total_price + (vat_rate*total_price)),
                       "currency": currency})
        print(output)
    return make_response(jsonify(output))