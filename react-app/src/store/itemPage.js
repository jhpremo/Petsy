//Get item details by item id
const GET_ITEM = 'itemPage/GET_ITEM'
const getItem = (item) => {
    return { type: GET_ITEM, item }
}

export const getItemDetailsThunk = (itemId) => async (dispatch) => {
    const response = await fetch(`/api/items/${itemId}`)

    if (response.ok) {
        const item = await response.json()
        dispatch(getItem(item))
        return item
    } else if (response.status === 404) {
        throw Error('404')
    } else {
        return ['An error occurred. Please try again.']
    }
}

// Post an item
const POST_ITEM = 'itemPage/POST_ITEM'
const postItem = (item) => {
    return { type: POST_ITEM, item }
}

export const postItemThunk = (item) => async (dispatch) => {
    const { name, price, description, images_urls } = item
    const response = await fetch('/api/items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            price,
            description,
            images_urls
        })
    })

    if (response.ok) {
        const item = await response.json()
        dispatch(postItem(item))
        return item
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ['An error occurred. Please try again.']
    }
}

//Edit item
const EDIT_ITEM = 'itemPage/EDIT_ITEM'
const editItem = (item) => {
    return { type: EDIT_ITEM, item }
}

export const editItemThunk = (item, itemId) => async (dispatch) => {
    const { name, price, description } = item
    const response = await fetch(`/api/items/${itemId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            price,
            description
        }),
    })

    if (response.ok) {
        const item = await response.json()
        dispatch(editItem(item))
        return item
    } else if (response.status === 404) {
        throw Error('404')
    } else if (response.status === 403) {
        throw Error('403')
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ['An error occurred. Please try again.']
    }
}

//Delete item
const DELETE_ITEM = 'itemPage/DELETE_ITEM'
const deleteItem = (itemId) => {
    return { type: DELETE_ITEM, itemId }
}

export const deleteItemThunk = (itemId) => async (dispatch) => {
    const response = await fetch(`/api/items/${itemId}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        const message = await response.json()
        dispatch(deleteItem(itemId))
        return message
    }
}


export const itemPageReducer = (state = null, action) => {
    switch (action.type) {
        case GET_ITEM:
            const stateGetItemDetails = { ...action.item }
            return stateGetItemDetails
        case POST_ITEM:
            const statePostItem = { ...action.item }
            return statePostItem
        case EDIT_ITEM:
            const stateEditItem = { ...action.item }
            return stateEditItem
        case DELETE_ITEM:
            return null
        default:
            return state
    }
}
