from flask import Blueprint
from flask_login import current_user, login_required
from app.models import Review, ReviewImage, db

review_image_routes = Blueprint('reviewImages', __name__)


@review_image_routes.delete('/<int:id>')
@login_required
def delete_review_image(id):
    """
    deletes review image by review image id
    """
    deleted_review_image = ReviewImage.query.get(id)
    if not deleted_review_image:
        return {"message": "Review image not found"}, 404

    review = Review.query.get(deleted_review_image.review_id)
    if current_user.is_authenticated and review.user_id == current_user.id:
        db.session.delete(deleted_review_image)
        db.session.commit()
        return {"message": "Review image successfully deleted"}
    else:
        return {"message": "Forbidden"}, 403
