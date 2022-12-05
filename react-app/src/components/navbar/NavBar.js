
import React, { useEffect } from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import ProfileButton from './profileButton';
import './navbar.css'
import { useState } from 'react';


const NavBar = () => {

  const [searchTerm, setSearchTerm] = useState('')
  const [toggleAdvancedSearch, setToggleAdvancedSearch] = useState(false)
  const [pageSize, setPageSize] = useState('')
  const [minPrice, setMinPrice] = useState('')
  const [maxPrice, setMaxPrice] = useState('')

  //the cart quanity count
  const [cartQuantity, setcartQuantity] = useState(0);
  const updateCartQuantity = () => {
    const cart = JSON.parse(localStorage.getItem('cart'))
      if (!cart) {
        setcartQuantity(0)
      } else {
        setcartQuantity(cart.length)
      }
  }

  useEffect(() => {
    updateCartQuantity()
    window.addEventListener('storage', updateCartQuantity)
  },[])

  const history = useHistory()

  const submitSearch = () => {

    let searchParams = new URLSearchParams()
    if (searchTerm) searchParams.append('q', searchTerm)
    if (minPrice) searchParams.append('minPrice', minPrice)
    if (maxPrice) searchParams.append('maxPrice', maxPrice)
    if (pageSize) searchParams.append('pageSize', Math.round(pageSize))

    setSearchTerm('')
    setMaxPrice('')
    setMinPrice('')
    setPageSize('')
    setToggleAdvancedSearch(false)
    if (searchParams.toString()) {
      history.push('/search?' + searchParams.toString())
    } else {
      history.push('/')
    }
  }

  const checkSubmit = (e) => {
    if (e.nativeEvent.code === "Enter") submitSearch()
  }

  // function to open advanced search drop down
  const openAdvancedSearch = () => {
    setToggleAdvancedSearch(!toggleAdvancedSearch)
  }

  let advancedSearchClass
  if (toggleAdvancedSearch) advancedSearchClass = 'navbar-advanced-search-dropdown-wrapper'
  else advancedSearchClass = 'navbar-hidden'


  return (
    <>
    <nav className='navbar-wrapper'>
      <NavLink to='/' exact={true} activeClassName='active' className="navbar-home-button">
        Petsy
      </NavLink>
      <div className='navbar-relative-wrapper'>
        <div className='navbar-search-wrapper'>
          <input className="navbar-search-input" type='text' placeholder='Search for anything' value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} onKeyDown={checkSubmit}></input>
          <button className='navbar-advanced-search-button' onClick={openAdvancedSearch}>
            <i className="fa-solid fa-caret-down" />
          </button>
          <div className={advancedSearchClass}>
            <div>
              <label>Minimum price: </label>
              <input className='navbar-advanced-search-dropdown-input' type='number' min='0' value={minPrice} onChange={(e) => setMinPrice(e.target.value)}></input>
            </div>
            <div>
              <label>Maximum price: </label>
              <input className='navbar-advanced-search-dropdown-input' type='number' min={`${minPrice}`} value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)}></input>
            </div>
            <div>
              <label>Results per page: </label>
              <input className='navbar-advanced-search-dropdown-input' type='number' min='0' value={pageSize} onChange={(e) => setPageSize(e.target.value)}></input>
            </div>
          </div>
          <button className='navbar-search-button' onClick={submitSearch}>
            <i className="fa-solid fa-magnifying-glass"></i>
          </button>
        </div>
      </div>
      <div className='navbar-buttons-wrapper'>
        <ProfileButton />
        <NavLink to='/cart' exact={true} className="navbar-cart-link">
          <i className="fa-solid fa-cart-shopping" />
          <div id={cartQuantity == 0 ? 'navbar-current-items-cart-hide' : 'navbar-current-items-cart'}><span>{cartQuantity > 999 ? 999 : cartQuantity}</span></div>
        </NavLink>
      </div>
    </nav >
    </>
  );
}

export default NavBar;
