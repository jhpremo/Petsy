import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory, useParams } from 'react-router-dom'
import { editItemThunk, getItemDetailsThunk } from '../../store/itemPage'
import './EditItemForm.css'

function EditItemForm() {
    const { itemId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const location = useLocation()

    const sessionUser = useSelector(state => state.session.user)

    //Sends user to error page if he is not seller of product
    if (location.state) {
        if (location.state.sellerId != sessionUser.id) history.push('/403')
    }

    //Set name, price and description from passed down data from parent if available
    const [name, setName] = useState(location.state ? location.state.name : "")
    const [price, setPrice] = useState(location.state ? location.state.price : 0)
    const [description, setDescription] = useState(location.state ? location.state.description : "")
    const [errors, setErrors] = useState([])

    //If not data passed down from parent, fetches item data from item id
    let item = {}
    if (!location.state) {
        (async () => {
            item = await dispatch(getItemDetailsThunk(itemId))

            //Sends user to error page if he is not seller of product
            if(item.sellerId!= sessionUser.id) history.push('/403')

            await setName(item.name)
            await setPrice(item.price)
            await setDescription(item.description)
        })()
    }

    useEffect(() => {}, [errors])

    const handleSubmit = async (e) => {
        e.preventDefault();
        const updatedItem = {
            name,
            price,
            description
        }

        setErrors([]);

        try {
            const data = await dispatch(editItemThunk(updatedItem, itemId))
            if (data.errors) {
                await setErrors(data.errors);
            } else {
                history.push(`/items/${itemId}`)
            }
        } catch (res) {
            history.push('/404')
        }
    }

    return (
        <div id='edit-item-form-wrapper'>
            <form id='edit-item-form' onSubmit={handleSubmit}>
                <h1>Edit Your Item</h1>
                <div className='errors'>
                    {errors.errors && (errors.errors.map((error, ind) => (
                    <div key={ind}>{error}</div>
                    )))}
                </div>
                <div>
                    <label>Name </label>
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
                    <label>Price </label>
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
                    <label>Description </label>
                    <textarea
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                        minLength={1}
                        maxLength={2000}
                    />
                </div>
                <button  type='submit'>Confirm Changes</button>
            </form>
            <button className='cancel-btn' onClick={() => history.push(`/items/${itemId}`)}>Cancel</button>
        </div>
    )
}

export default EditItemForm
