from flask import Blueprint, jsonify
from app.models import Review, Product, User, ReviewImage, db

seller_routes = Blueprint('sellers', __name__)

@seller_routes.get('/test')
def test_route():
    return 'seller'

@seller_routes.get("/<int:id>/reviews")
def get_seller_reviews(id):
    """
    Get all reviews by seller Id
    """
    seller_id = id

    print(seller_id)



    seller_reviews = db.session.query(
                                    Review.id,
                                    Product.user_id.label("sellerId"),
                                    Review.date_created,
                                    Review.rating,
                                    Review.text,
                                    Product.id.label("itemId"),
                                    Product.name,
                                    User.username
                                    ).join(
                                    Product, Review.product_id == Product.id
                                    ).join(
                                    User, Product.user_id == User.id
                                    ).all()


    seller_reviews = [
                {
                    "id": row.id,
                    "user" : { "name": row.username },
                    "sellerId": row.sellerId,
                    "itemId": row.itemId,
                    "text": row.text,
                    "date": row.date_created,
                    "starRating": row.rating
                } for row in seller_reviews if row.sellerId == seller_id
                    ]

    if seller_reviews:
        return jsonify({"sellerReviews": seller_reviews})
    else:
        return {"message": "seller not found"}, 404


@seller_routes.get('/<int:id>/images')
def get_review_image(id):
    """
    Get review images by seller id
    """
    user = User.query.get(id)
    if user == None:
        return {"message": "seller not found"}, 404

    reviews = ReviewImage.query.join(Review).join(Product).filter(Product.user_id == id)
    allReviews = []
    for review in reviews:
        review_obj = {
            "id": review.id,
            "reviewId": review.review_id,
            "url": review.url
        }
        allReviews.append(review_obj)

    return allReviews
