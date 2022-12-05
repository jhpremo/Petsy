const GET_USER_REVIEWS = 'userReviews/GET_REVIEW'
const getUserReviews = (reviews) => {
    return { type: GET_USER_REVIEWS, reviews }
}

export const getUserReviewsThunk = () => async (dispatch) => {
    const response = await fetch(`/api/session/reviews`)

    if (response.ok) {
        const reviews = await response.json()
        let normalizedReviews = {}
        reviews.userReviews.forEach(review => {
            normalizedReviews[review.id] = review
        });
        dispatch(getUserReviews(normalizedReviews))
        return reviews
    }

}

const EDIT_REVIEW = 'userReviews/EDIT_REVIEW'
const editUserReviews = (review) => {
    return { type: EDIT_REVIEW, review }
}

export const editUserReviewThunk = (review) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${review.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(review)
    })

    if (response.ok) {
        const review = await response.json()
        dispatch(editUserReviews(review))
    }
}

const DELETE_REVIEW = 'userReviews/DELETE_REVIEW'
const deleteItem = (reviewId) => {
    return { type: DELETE_REVIEW, reviewId }
}

export const deleteUserReviewThunk = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        const review = await response.json()
        dispatch(deleteItem(reviewId))
    }
}

export const userReviewsReducer = (state = null, action) => {
    switch (action.type) {
        case GET_USER_REVIEWS:
            const stateGetUserReviews = { ...action.reviews }
            return stateGetUserReviews
        case EDIT_REVIEW:
            let stateEditReview = { ...state }
            let editedReview = stateEditReview[action.review.id]
            editedReview.text = action.review.text
            editedReview.starRating = action.review.starRating
            stateEditReview[action.review.id] = editedReview
            return stateEditReview
        case DELETE_REVIEW:
            let stateDeleteReview = { ...state }
            delete stateDeleteReview[action.reviewId]
            return stateDeleteReview
        default:
            return state
    }
}
