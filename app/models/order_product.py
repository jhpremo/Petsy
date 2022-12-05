from .db import db, environment, SCHEMA, add_prefix_for_prod
from .product import Product
from .order import Order


class OrderProduct(db.Model):
    __tablename__ = 'order_products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')))
    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('orders.id')))
    item_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', back_populates='order_products')
    order = db.relationship('Order', back_populates='order_products')
