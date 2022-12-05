from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user import User


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    name = db.Column(db.String(75), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(2000), nullable=False)

    user = db.relationship('User', back_populates='products')
    reviews = db.relationship('Review',  back_populates='product', cascade="all, delete-orphan")
    order_products = db.relationship('OrderProduct', back_populates='product')
    product_images = db.relationship('ProductImage', back_populates='product', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }
