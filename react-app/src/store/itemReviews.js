//Get item reviews by item id
const GET_REVIEWS = 'itemReviews/GET_REVIEWS'
const getItemReviews = (reviews) => {
    return { type: GET_REVIEWS, reviews }
}

export const getItemReviewsThunk = (itemId) => async (dispatch) => {
    const response = await fetch(`/api/items/${itemId}/reviews`)

    if (response.ok) {
        const reviews = await response.json()
        dispatch(getItemReviews(reviews))
        return reviews
    }
}

//Post review by item id
const ADD_REVIEW = 'itemReviews/ADD_REVIEW'
const addItemReview = (review) => {
    return { type: ADD_REVIEW, review }
}

export const addItemReviewThunk = (itemId, review) => async (dispatch) => {
    const { rating, text } = review
    const response = await fetch(`/api/items/${itemId}/reviews`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            rating,
            text
        })
    })

    if (response.ok) {
        const review = await response.json()
        dispatch(addItemReview(review))
        return review
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

export const itemReviewsReducer = (state = null, action) => {
    switch (action.type) {
        case GET_REVIEWS:
            const stateGetItemReviews = [...action.reviews['itemReviews']]
            return stateGetItemReviews
        case ADD_REVIEW:
            // console.log('state', state)
            const stateAddItemReview = state
            return stateAddItemReview
        default:
            return state
    }
}
