from .db import db, environment, SCHEMA, add_prefix_for_prod
from .product import Product


class ProductImage(db.Model):
    __tablename__ = 'product_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')))
    url = db.Column(db.String(2048), nullable=False)
    preview_image = db.Column(db.Boolean, nullable=False)

    product = db.relationship('Product', back_populates='product_images')
