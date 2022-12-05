import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./listproduct.css"
import { postItemThunk } from "../../store/itemPage";

const ListProductForm = () => {
    const [name, setName] = useState("");
    const [price, setPrice] = useState(0);
    const [description, setDescription] = useState("");
    const [urls, setUrls] = useState("");
    const [errors, setErrors] = useState([]);
    const [submitted, setSubmitted] = useState(false)
    const dispatch = useDispatch()
    const history = useHistory()
    const user = useSelector((state) => state.session.user)

    useEffect(() => {
        if (!user) {
            history.push('/')
            return
        }
    }, [user])

    useEffect(() => {
        let errorsArr = []
        let parsedPrice = parseFloat(price)
        let urlArr = urls.split(/\r?\n/)

        const validateUrl = (urls) => {
            let check = true
            urls.forEach(url => {
                if (!url || !url.includes('.') || url.length > 2048) check = false
            });
            return check
        }

        if (!(name && description && price)) errorsArr.push("All fields must be filled out")
        if (name && name.length > 75) errorsArr.push("Product name must be less than 50 characters")
        if (description && description.length > 2000) errorsArr.push("Product description must be less than 255 characters")
        if (price && (!parsedPrice || !Number(price) || parsedPrice <= 0)) errorsArr.push('Price must be a positive number')
        if (urls && !validateUrl(urlArr)) errorsArr.push('Each image must have a valid url seperated by a comma')

        setErrors(errorsArr)
    }, [name, description, price, urls])

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (errors.length) {
            setSubmitted(true)
            return
        }

        let urlStr = urls.split(/\r?\n/).join(', ')

        let payload = {
            name,
            description,
            price,
            images_urls: urlStr
        }

        const item = await dispatch(postItemThunk(payload))
        history.push(`/items/${item.id}`)
    }

    return (
        <div className="list-product-form-wrapper">
            <form onSubmit={handleSubmit} className='list-product-form'>
                <h1>List your product</h1>
                {errors.length > 0 && submitted && <ul className="list-product-form-errors">
                    {errors.map((error, idx) => <li key={idx}>{error}</li>)}
                </ul>}
                <div>
                    <label>
                        Name
                    </label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                        minLength={1}
                        maxLength={75}
                    />
                </div>
                <div>
                    <label>
                        Price
                    </label>
                    <input
                        type="number"
                        step="0.01"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                        required
                        min={0.01}
                    />
                </div>
                <div>
                    <label>
                        Description
                    </label>
                    <textarea
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                        minLength={1}
                        maxLength={2000}
                    />
                </div>
                <div>
                    <label>Image urls (separated by comma)</label>
                    <textarea
                        onChange={e => setUrls(e.target.value)}
                        value={urls}
                        required
                    />
                </div>
                <button type='submit'>Post product</button>
            </form>
            <button className='cancel-btn' onClick={() => history.push(`/`)}>Cancel</button>
        </div>
    )
}

export default ListProductForm
