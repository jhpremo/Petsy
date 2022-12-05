from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Order, OrderProduct, Product, db

order_routes = Blueprint('orders', __name__)

@order_routes.get('/test')
def test_route():
    return 'orders'


@order_routes.post('')
@login_required
def post_order():
    # create order with dummy total price to get order id
    order = Order(
        user_id=current_user.id,
        total_price=1.00
    )
    db.session.add(order)
    db.session.commit
    # loop through items create order products and tally total price
    total=0
    for checkout_item in request.json['checkoutItems']:
        # query for item
        item = Product.query.get(checkout_item["id"])
        # return error and delete order if any item in order cannot be found
        if not item:
            db.session.delete(order)
            return {"message": "A item in order was not found"}, 404
        # add to total price and create order product
        total+=item.price*checkout_item['quantity']
        order_product = OrderProduct(
            product_id=item.id,
            order_id=order.id,
            item_price=item.price,
            quantity=checkout_item['quantity']
        )
        db.session.add(order_product)
    # update order total price and commit order products to database
    order.total_price=total
    db.session.commit()
    return {"orderId": f"{order.id}"}
