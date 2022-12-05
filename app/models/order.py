from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user import User
from datetime import datetime


class Order(db.Model):
    __tablename__ = 'orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    total_price = db.Column(db.Float, nullable=False)
    order_datetime = db.Column(db.DateTime, nullable=False, default=datetime.today())

    user = db.relationship('User', back_populates='orders')
    order_products = db.relationship('OrderProduct', back_populates='order')

    def to_dict(self):
        order_dict = {
            "id": self.id,
            "totalPrice": self.total_price,
            "orderDate": self.order_datetime,
            "items": self.order_products
        }
        return order_dict
