from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy import or_, and_
from sqlalchemy.orm import joinedload
from ..models import db, Product, Review, OrderProduct, ProductImage, User
from ..forms.item_form import CreateEditProductForm
from ..forms.add_image_form import AddImageForm
from ..forms.item_form import CreateEditProductForm
from ..forms.review_form import CreateEditReviewForm
from ..models import OrderProduct, Product, ProductImage, Review, db
from .auth_routes import validation_errors_to_error_messages


item_routes = Blueprint('items', __name__)

@item_routes.get('/')
def all_items():
    page = 1
    size = 20
    min_price = -float('inf')
    max_price = float('inf')
    keywords = []
    seller_id = None

    if "page" in request.args:
        page = int(request.args["page"])

    if "pageSize" in request.args:
        size = int(request.args["pageSize"])

    if "minPrice" in request.args:
        min_price = int(request.args["minPrice"])

    if "maxPrice" in request.args:
        max_price = int(request.args["maxPrice"])

    if "q" in request.args:
        keywords = [keyword.lower() for keyword in request.args["q"].split()]

    if "sellerId" in request.args:
        seller_id = request.args["sellerId"]


    keywords_condition = or_(*[Product.name.ilike(f"%{kw}%") for kw in keywords], *[Product.description.ilike(f"%{kw}%") for kw in keywords])
    price_condition = and_(Product.price >= min_price, Product.price <= max_price)

    if not seller_id:
        # queried_products = Product.query.filter(price_condition, keywords_condition).limit(size).offset((page - 1) * size)
        queried_products = Product.query.filter(price_condition, keywords_condition)
    else:
        # queried_products = Product.query.filter(price_condition, keywords_condition, Product.user_id == seller_id).limit(size).offset((page - 1) * size)
        queried_products = Product.query.filter(price_condition, keywords_condition, Product.user_id == seller_id)


    constructed_products = []

    for product in queried_products:
        constructed_product = dict()

        shop_name = User.query.get(product.user_id).username
        shop_reviews = Review.query.join(Review.product).filter(Product.user_id == product.user_id)
        review_ratings = [review.rating for review in shop_reviews]
        num_shop_reviews = len(review_ratings)
        avg_shop_rating = round(sum(review_ratings) / (len(review_ratings) or 1), 2)
        preview_image = ProductImage.query.filter(ProductImage.product_id == product.id)[0]

        constructed_product = {
            "id": product.id,
            "sellerId": product.user_id,
            "name": product.name,
            "avgShopRating": avg_shop_rating,
            "shopReviews": num_shop_reviews,
            "price": product.price,
            "shopName": shop_name,
            "previewImageURL": preview_image.url,
        }

        constructed_products.append(constructed_product)

    offset = (page - 1) * size

    # print("numRESULLLLLTS", len(constructed_products))

    return {
        "items": [product for product in constructed_products][offset:offset + size],
        "numResults": len(constructed_products)
    }

@item_routes.get("/<int:id>")
def item_by_id(id):
    product = Product.query.get(id)

    if not product:
        return {
            "message": "Item could not be found"
        }, 404

    seller_name = User.query.get(product.user_id).username
    shop_reviews = Review.query.join(Review.product).filter(Product.user_id == product.user_id)
    shop_review_ratings = [review.rating for review in shop_reviews]
    item_review_ratings = [review.rating for review in shop_reviews if review.product_id == product.id]
    avg_rating = round(sum(shop_review_ratings) / (len(shop_review_ratings) or 1), 2)
    shop_orders = OrderProduct.query.join(OrderProduct.product).filter(Product.user_id == product.user_id)
    shop_sales = sum([order.quantity for order in shop_orders])
    images = ProductImage.query.filter(ProductImage.product_id == product.id)
    image_urls = [image.url for image in images]


    constructed_product = {
        "sellerId": product.user_id,
        "name": product.name,
        "shopName": seller_name,
        "price": product.price,
        "avgShopRating": avg_rating,
        "shopSales": shop_sales,
        "description": product.description,
        "shopReviews": len(shop_review_ratings),
        "itemReviews": len(item_review_ratings),
        "imageURLs": image_urls
    }


    return constructed_product



@item_routes.post('')
@login_required
def create_item():
    """
    Creates/posts a new item
    """
    form = CreateEditProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_product = Product(
            user_id=current_user.get_id(),
            name=form.data['name'],
            price=form.data['price'],
            description=form.data['description']
        )
        db.session.add(new_product)
        db.session.commit()

        # Adds item images if provided
        if form.data['images_urls']:
            url_lst = form.data['images_urls'].split(',')
            for url in url_lst:
                new_image = ProductImage(
                    product_id = new_product.id,
                    url = url,
                    preview_image = True if url_lst.index(url) == 0 else False # Makes first listed url the preview image
                )
                db.session.add(new_image)
                db.session.commit()

        # Gets all reviews of shop then calculates avg rating
        # Uses current user id since current user will always be seller when creating item
        reviews = Review.query.join(Product).filter(Product.user_id == current_user.get_id()).all()
        avg_rating = 0
        if reviews:
            for review in reviews:
                avg_rating += review.rating
            avg_rating /= len(reviews)

        # Gets all reviews of store then calculates number of sales
        # Uses current user id since current user will always be seller/store owner when creating item
        orders = OrderProduct.query.join(Product).filter(Product.user_id == current_user.get_id()).all()
        sales = 0
        for order in orders:
            sales += order.quantity

        final_product = {
            "id": new_product.id,
            "sellerId": current_user.id,
            "name": new_product.name,
            "shopName": current_user.username,
            "price": new_product.price,
            "avgShopRating": avg_rating,
            "shopSales": sales,
            "description": new_product.description,
            "shopReviews": len(reviews),
            "itemReviews": 0,
            "imageURLs": form.data['images_urls'].split(', ') if form.data['images_urls'] else [] # Turns urls into list if provided else it will equal an empty list
        }

        return final_product
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@item_routes.put('/<int:product_id>')
@login_required
def edit_product(product_id):
    """
    Edit an item by item id
    """
    form = CreateEditProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        current_product = Product.query.get(product_id)

        if current_product == None:
            return {"message": "Item could not be found"}, 404

        if current_product.user_id != int(current_user.get_id()):
            return {"message": "Forbidden"}, 403


        current_product.name = form.data['name']
        current_product.price = form.data['price']
        current_product.description = form.data['description']

        db.session.commit()

        # Gets all reviews of shop then calculates avg rating
        # Uses current user id since current user must be the seller to be able to edit item
        shop_reviews = Review.query.join(Product).filter(Product.user_id == current_user.get_id()).all()
        avg_rating = 0
        if shop_reviews:
            for review in shop_reviews:
                avg_rating += review.rating
            avg_rating /= len(shop_reviews)

        # Gets all reviews of store then calculates number of sales
        # Uses current user id since current user must be the seller to be able to edit item
        orders = OrderProduct.query.join(Product).filter(Product.user_id == current_user.get_id()).all()
        sales = 0
        for order in orders:
            sales += order.quantity

        # Gets all reviews of item
        item_reviews_count = Product.query.join(Review).filter(Review.product_id == current_product.id).count()

        # Gets all image URLs
        images = ProductImage.query.filter(ProductImage.product_id == current_product.id).all()

        final_product = {
            "id": current_product.id,
            "sellerId": current_user.get_id(),
            "name": current_product.name,
            "shopName": current_user.username,
            "price": current_product.price,
            "avgShopRating": avg_rating,
            "shopSales": sales,
            "description": current_product.description,
            "shopReviews": len(shop_reviews),
            "itemReviews": item_reviews_count,
            "imageURLs": [image.url for image in images] if images else []
        }
        return final_product
    else:
        print(form.errors)
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@item_routes.delete('/<int:product_id>')
@login_required
def delete_product(product_id):
    """
    Delete an item by item id
    """
    current_product = Product.query.get(product_id)
    print(type(current_user.get_id()))
    print(type(current_product.user_id))

    if current_product == None:
        return {"message": "Item could not be found"}, 404

    if current_product.user_id != int(current_user.get_id()):
        return {"message": "Forbidden"}, 403

    db.session.delete(current_product)
    db.session.commit()

    return { "message": "Successfully deleted" }


@item_routes.post('/<int:product_id>/images')
@login_required
def add_image(product_id):
    """
    Add image of item by item id
    """
    form = AddImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        current_product = Product.query.get(product_id)

        if current_product == None:
            return {"message": "Item could not be found"}, 404

        if current_product.user_id != int(current_user.get_id()):
            return {"message": "Forbidden"}, 403

        new_image = ProductImage(
            product_id = product_id,
            url = form.data['url'],
            preview_image = form.data['preview_image']
        )

        db.session.add(new_image)
        db.session.commit()

        return { 'id': new_image.id, 'url': new_image.url, 'preview_image': new_image.preview_image}
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@item_routes.get('/<int:product_id>/reviews')
def get_reviews_by_item(product_id):
    """
    Get all reviews by item Id
    """
    current_product = Product.query.get(product_id)

    if current_product == None:
        return {"message": "Item could not be found"}, 404

    reviews = Review.query.filter(Review.product_id == product_id).options(joinedload(Review.user)).options(joinedload(Review.product)).options(joinedload(Review.review_images)).all()


    review_lst = []
    for review in reviews:
        user_obj = {'id': review.user.id, 'username': review.user.username}

        review_data = {
            'id': review.id,
            'user': user_obj,
            'sellerId': review.product.user_id,
            'itemId': review.product.id,
            'starRating': review.rating,
            'text': review.text,
            'date': review.date_created,
            'imgUrls': [images.url for images in review.review_images]
        }
        review_lst.append(review_data)


    return { "itemReviews": review_lst }


@item_routes.post("/<int:product_id>/reviews")
@login_required
def create_review(product_id):
    """
    Add review of item by item id
    """
    # check if item up for review exists
    item_check = Product.query.get(product_id)


    # if it doesn't exist in database, return error
    if not item_check:
        return {"message": "item not found"}, 404


    # assign shorter form name and get csrf_token
    form = CreateEditReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    # using wtforms validation to check validity of review data for database
    if form.validate_on_submit():

        # create new review in database
        new_review = Review(
            user_id=current_user.id,
            product_id=product_id,
            rating=form.data["rating"],
            text=form.data["text"]
        )
        db.session.add(new_review)
        db.session.commit()

        # format response body
        new_review_details = {
            "id": new_review.id,
            "user": {"name": current_user.username},
            "sellerId": item_check.user_id,
            "itemId": product_id,
            "text": new_review.text,
            "date": new_review.date_created,
            "starRating": new_review.rating
        }

        return new_review_details
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
