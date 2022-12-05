from .db import db, environment, SCHEMA, add_prefix_for_prod
from .review import Review


class ReviewImage(db.Model):
    __tablename__ = 'review_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('reviews.id')))
    url = db.Column(db.String(2048), nullable=False)

    review = db.relationship('Review', back_populates='review_images')
