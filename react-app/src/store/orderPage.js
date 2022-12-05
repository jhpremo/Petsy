const GET_ORDERS = 'orderPage/GET_ORDERS'
const getOrders = (orders) => {
    return { type: GET_ORDERS, orders }
}

export const getOrdersThunk = () => async (dispatch) => {
    const response = await fetch(`/api/session/orders`)

    if (response.ok) {
        const orders = await response.json()
        dispatch(getOrders(orders))
        return
    } else if (response.status === 404) {
        throw Error('404')
    } else {
        return ['An error occurred. Please try again.']
    }
}

export const orderPageReducer = (state = null, action) => {
    switch (action.type) {
        case GET_ORDERS:
            const stateGetOrders = [...action.orders]
            return stateGetOrders
        default:
            return state
    }
}
