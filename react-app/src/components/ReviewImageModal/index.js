import './ReviewImageModal.css'
import StarRatings from 'react-star-ratings'
import { useEffect } from 'react'
import { useSelector, useDispatch } from "react-redux";
import { getOneReviewThunk } from '../../store/modalReview'
import { useHistory } from 'react-router-dom';

function ReviewImageModal({ modalStr }) {
    const dispatch = useDispatch();
    const history = useHistory()

    // gets review id and review img url from modal str that was passed as props
    const modalStrArr = modalStr.split(':::::')
    const reviewId = modalStrArr[0]
    const reviewUrl = modalStrArr[1]


    useEffect(async() => {
        await dispatch(getOneReviewThunk(reviewId))
    },[reviewId])

    const review = useSelector((state) => state.modalReview);

    const redirect = () => {
        history.push(`/items/${review.product_id}`)
        history.go(0) //refreshes page, modal will stay open otherwise
    }

    return (
        <>
        {review && (
            <div id='review-img-modal-container'>
                <img src={reviewUrl} alt='review image' id='review-img-modal-img'></img>
                <div id='review-img-modal-review'>
                    <div id='review-img-modal-review-details'>
                        <div id='review-img-modal-review-date'>{new Date(review.date).toDateString().slice(4)}</div>
                        <div id='review-img-modal-review-name'>{review.username}</div>
                        <div id='review-img-modal-review-rating'>
                            <StarRatings
                                rating={review.rating}
                                starRatedColor='black'
                                numberOfStars={5}
                                starDimension='20px'
                                starSpacing='1px'
                            />
                        </div>
                        <div id='review-img-modal-review-text'>{review.text}</div>
                    </div>
                    <div id='review-img-modal-review-product'>
                        <div id='review-img-modal-review-details-head'>Purchased Item:</div>
                        <div id='review-img-modal-review-details-body' onClick={redirect}>
                            <img src={review.product_url} alt='review image' id='review-img-modal-product-img'></img>
                            <div id='review-img-modal-review-details'>
                                <div id='review-img-modal-review-details-name'>{review.product_name}</div>
                                <div id='review-img-modal-review-details-price'>${review.product_price.toFixed(2)}</div>
                            </div>
                        </div>
                    </div>

                </div>

            </div>

        )}
        </>
    )
}

export default ReviewImageModal
