import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"
import { getUserReviewsThunk } from "../../store/userReview"
import StarRatings from "react-star-ratings";
import { editUserReviewThunk, deleteUserReviewThunk } from "../../store/userReview";
import './yourReview.css'

const YourReviews = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const [isLoaded, setIsLoaded] = useState(false)
    const user = useSelector((state) => state.session.user)
    const [editFocus, setEditFocus] = useState(null)
    const [starRating, setStarRating] = useState(0)
    const [text, setText] = useState('')

    useEffect(async () => {
        if (!user) {
            history.push('/')
            return
        }
        await dispatch(getUserReviewsThunk())
        setIsLoaded(true)
    }, [dispatch])

    const reviews = useSelector((state) => {
        if (isLoaded) return Object.values(state.userReviews)
        else return []
    })

    const reviewObj = useSelector((state) => {
        if (isLoaded) return state.userReviews
    })

    useEffect(() => {
        if (isLoaded && editFocus) {
            setStarRating(reviewObj[editFocus].starRating)
            setText(reviewObj[editFocus].text)
        } else if (!editFocus) {
            setStarRating(0)
            setText('')
        }
    }, [editFocus, isLoaded])

    const handleSubmit = async (e) => {
        e.preventDefault()
        let payload = {
            id: editFocus,
            rating: starRating,
            text
        }
        await dispatch(editUserReviewThunk(payload))
        setEditFocus(null)
    }

    const handleDelete = (reviewId) => {
        return async () => {
            if (
                window.confirm(
                    "Are you sure you want to delete this review? You can not recover this review after deletion."
                )
            ) {
                await dispatch(deleteUserReviewThunk(reviewId))
            }
        }
    }

    return (
        <div>
            <div className="your-reviews-wrapper">
                <h1 className="your-reviews-header">Your Reviews</h1>

                {isLoaded && reviews?.map((review) => {
                    return (
                        <div className="your-reviews-review-wrapper" key={review.id}>
                            <div className="your-reviews-review-border-wrapper">
                                <div className="your-reviews-item-image" onClick={() => history.push(`/items/${review?.item.itemId}`)} style={{ backgroundImage: `url(${review?.item.previewImageURL})` }}></div>
                                <div className="your-reviews-review-content-wrapper">
                                    <h2 onClick={() => history.push(`/items/${review?.item.itemId}`)}>{review?.item.name} sold by {review?.item.shopName}</h2>
                                    <div className="your-reviews-review-content">
                                        {editFocus !== review.id && <>
                                            <h4><StarRatings
                                                rating={review.starRating}
                                                starRatedColor='black'
                                                numberOfStars={5}
                                                starDimension='15px'
                                                starSpacing='1px'
                                            /> | {(new Date(review.date)).toDateString()}</h4>
                                            <p>{review.text}</p>
                                            {review?.reviewImageURL && <div className="your-reviews-review-image" style={{ backgroundImage: `url(${review?.reviewImageURL})` }}></div>}
                                        </>}
                                        {editFocus === review.id && <>
                                            <form onSubmit={handleSubmit} className="your-reviews-edit-form">
                                                <div className='your-reviews-input-wrapper'>
                                                    <StarRatings
                                                        rating={starRating}
                                                        starRatedColor='black'
                                                        numberOfStars={5}
                                                        starDimension='15px'
                                                        starSpacing='1px'
                                                    />
                                                    <input
                                                        type="range"
                                                        min={1}
                                                        max={5}
                                                        step={1}
                                                        value={starRating}
                                                        onChange={(e) => setStarRating(Number(e.target.value))}
                                                        required
                                                        className='your-reviews-form-input-slider'
                                                    />
                                                </div>
                                                <div className='your-reviews-input-wrapper'>
                                                    <textarea
                                                        className='your-reviews-form-input-textarea'
                                                        onChange={e => setText(e.target.value)}
                                                        value={text}
                                                        maxLength='255'
                                                    />
                                                </div>
                                                <div className='input-wrapper'>
                                                    <button className='your-reviews-submit-button'>Post edits</button>
                                                </div>
                                            </form>
                                        </>}
                                    </div>
                                </div>
                            </div>
                            <div className="your-reviews-buttons">
                                <button onClick={() => {
                                    if (editFocus === review.id) setEditFocus(null)
                                    else setEditFocus(review.id)
                                }}>
                                    {editFocus === review.id && 'Cancel'}{editFocus !== review.id && 'Edit'}</button>
                                <button onClick={handleDelete(review.id)}>Delete</button>
                            </div>
                        </div>
                    )
                })}
            </div>
            {isLoaded && (
                <h6 className="about-links-footer">
                  <div className="about-links-github-icon"> <a href="https://github.com/jhpremo/Petsy-group-project"><i className="fa-brands fa-github" /></a></div>
                  <div className="about-links-creators">Website clone created by <a href="https://github.com/cgalang9">Carmelino Galang</a>, <a href="https://github.com/jhpremo">Jason Premo</a>, <a href="https://github.com/jwad96">Jwad Aziz</a>, and <a href="https://github.com/DevSPK">Sean Kennedy</a></div>
                </h6>)}
        </div>
    )
}

export default YourReviews
