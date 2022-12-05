import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"
import { getOrdersThunk } from "../../store/orderPage"
import "./yourOrders.css"

const YourOrders = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setIsLoaded] = useState(false)
    const user = useSelector((state) => state.session.user)

    useEffect(async () => {
        if (!user) {
            history.push('/')
            return
        }
        await dispatch(getOrdersThunk())
        setIsLoaded(true)
    }, [dispatch])

    const orders = useSelector((state) => state.orders)

    return (
        <div className="your-orders-wrapper">
            <h1 className="your-reviews-header">Your Orders</h1>
            {orders?.map((order) => {
                return (
                    <div key={order.id} className="your-orders-order-wrapper">
                        <div className="your-orders-order-border-wrapper">
                            <h2>Ordered {order.totalItems} items on {(new Date(order.orderDate)).toDateString().slice(3,)}</h2>
                            <div className="your-orders-items-wrapper">
                                {order.items?.map((item) => {
                                    return (
                                        <div className="your-orders-item-wrapper" key={item.id}>
                                            <div className="your-orders-item-image" onClick={() => history.push(`/items/${item.product_id}`)} style={{ backgroundImage: `url(${item.previewImageURL})` }}></div>
                                            <div className="your-orders-item-text-wrapper">
                                                <h4 >Purchased {item.quantity} x <span onClick={() => history.push(`/items/${item.product_id}`)}>{item.name}</span></h4>
                                                <h5 >Sold by {item.shopName} </h5>
                                                <h6>${item.purchasePrice} x {item.quantity} = ${(item.purchasePrice * item.quantity).toFixed(2)}</h6>
                                            </div>
                                        </div>
                                    )
                                })}
                            </div>
                            <h3>Order total: ${(Math.round(order.totalPrice * 100) / 100).toFixed(2)}</h3>
                        </div>
                    </div>
                )
            })}

            {isLoaded && (
                <h6 className="about-links-footer">
                  <div className="about-links-github-icon"> <a href="https://github.com/jhpremo/Petsy-group-project"><i className="fa-brands fa-github" /></a></div>
                  <div className="about-links-creators">Website clone created by <a href="https://github.com/cgalang9">Carmelino Galang</a>, <a href="https://github.com/jhpremo">Jason Premo</a>, <a href="https://github.com/jwad96">Jwad Aziz</a>, and <a href="https://github.com/DevSPK">Sean Kennedy</a></div>
                </h6>)}
        </div>
    )
}

export default YourOrders
