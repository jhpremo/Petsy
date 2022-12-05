//Get review images by seller id
const GET_IMAGES = 'sellerReviewimages/GET_IMAGES'
const getImages = (reviews) => {
    return { type: GET_IMAGES, reviews }
}

export const getImagesBySellerIdThunk = (sellerId) => async (dispatch) => {
    const response = await fetch(`/api/sellers/${sellerId}/images`)

    if(response.ok) {
        const images = await response.json()
        dispatch(getImages(images))
        return images
    } else if (response.status === 404) {
        throw Error('404')
    } else {
      return ['An error occurred. Please try again.']
    }
}

export const sellerReviewImagesReducer = (state = null, action) => {
    switch(action.type) {
        case GET_IMAGES:
            const stateGetImages = action.reviews
            return stateGetImages
        default:
            return state
    }
}
