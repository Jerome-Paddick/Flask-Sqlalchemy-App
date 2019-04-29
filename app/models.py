from app import db
import datetime


class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column('product_id', db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    vat_band = db.Column(db.String(20), db.ForeignKey("vat_rates.name"))
    vat = db.relationship("VatRates", backref="vat_rates")


class VatRates(db.Model):
    __tablename__ = 'vat_rates'
    name = db.Column(db.String(20), primary_key=True)
    rate = db.Column(db.Float)
    products = db.relationship("Products", backref="products")


class ExchangeRates(db.Model):
    __tablename__ = 'exchange_rates'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(3),
                             unique=True)
    exchange_rate = db.Column(db.Float, nullable=True)
    last_updated = db.Column(db.DateTime,
                             nullable=False,
                             default=datetime.datetime.now(),
                             onupdate=datetime.datetime.now())


class ApiKeys(db.Model):
    __tablename__ = 'api_keys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    api_key = db.Column(db.String(50))
    url = db.Column(db.String(200))