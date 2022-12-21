const GET_PRODUCTS = "items/GET_PRODUCTS"

const initialState = {};

const populateProducts = (products) => (
    {
        type: GET_PRODUCTS,
        products
    }
)

export const getProducts = (queryParams) => async (dispatch) => {
    let query = []
    let queryString = ''

    for (let [key, val] of Object.entries(queryParams)) {
        query.push(`${key}=${val}`)
    }

    if (query.length > 0) {
        queryString += '?' + query.join('&')
    }


    const responseBody = await fetch(`/api/items${queryString}`).then(res => res.json())
    const products = responseBody.items;
    const numResults = responseBody.numResults;


    const normalizedProducts = products.reduce((acc, product) => {
        acc[product.id] = { ...(delete product.id && product) }
        return acc
    }, {})

    normalizedProducts.numResults = numResults

    dispatch(populateProducts(normalizedProducts))
}

const CLEAR_PRODUCTS = 'items/CLEAR_PRODUCTS'

export const clearItemStore = () => {
    return { type: CLEAR_PRODUCTS }
}

export default function reducer(state = initialState, action) {
    if (action.type === GET_PRODUCTS) {
        return action.products
    } else if (action.type === CLEAR_PRODUCTS) {
        return initialState
    }

    return state
}
