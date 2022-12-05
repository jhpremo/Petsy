import LogoutButton from '../auth/LogoutButton';
import { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import { login } from '../../store/session'

const ProfileButton = () => {
    const sessionUser = useSelector(state => state.session.user)
    const [toggleDropDown, setToggleDropDown] = useState(false)
    const dispatch = useDispatch();
    const history = useHistory()

    // function to log in demo user
    const demoLogin = async () => {
        await dispatch(login('demo@aa.io', 'password'));
        await history.push('/')
    }

    // function to open drop down
    const openDropDown = () => {
        if (toggleDropDown) return;
        setToggleDropDown(true);
    };
    // use effect hook to close drop down if user clicks away from the drop down
    useEffect(() => {
        if (!toggleDropDown) return;

        const closeDropDown = () => {
            setToggleDropDown(false);
        };

        document.addEventListener('click', closeDropDown);

        return () => document.removeEventListener("click", closeDropDown);
    }, [toggleDropDown]);

    // sets visability of drop down based on toggle drop down slice of state
    let dropDownClass
    if (toggleDropDown) {
        dropDownClass = "navbar-profile-dropdown-wrapper"
    } else dropDownClass = 'navbar-hidden'

    // Sets profile drop down or sign in button based on if user is logged in
    let buttonContent
    if (sessionUser) {
        buttonContent = (
            <div className='navbar-profile-wrapper'>
                <button className="navbar-profile-button" onClick={openDropDown}>
                    <span><i className="fas fa-user-circle" /> <i className="fa-solid fa-caret-down" /> </span>
                </button>
                <div className='navbar-profile-dropdown-wrapper'>
                    <div className={dropDownClass}>
                        <div className='navbar-profile-dropdown-header'>
                            <i className="fas fa-user-circle" />
                            <span> </span>
                            {sessionUser.username}
                        </div>
                        <NavLink to={`/search?sellerId=${sessionUser.id}`} activeClassName='active' className='navbar-profile-dropdown-item'>
                            <i className="fa-solid fa-list" /> Your listings
                        </NavLink>
                        <NavLink to='/your-orders' activeClassName='active' className='navbar-profile-dropdown-item'>
                            <i className="fa-regular fa-clipboard" /> <span> </span> Your orders
                        </NavLink>
                        <NavLink to='/your-reviews' activeClassName='active' className='navbar-profile-dropdown-item navbar-star'>
                            <i className="fa-regular fa-star" /> Your reviews
                        </NavLink>
                        <NavLink to='/list-product' activeClassName='active' className='navbar-profile-dropdown-item'>
                            <i className="fa-solid fa-pen-to-square" /> List a product
                        </NavLink>
                        <LogoutButton />
                    </div>
                </div>
            </div >
        )
    } else {
        buttonContent = (
            <>
                <button onClick={demoLogin} className='navbar-demo-user-button'>
                    Demo user
                </button>
                <NavLink to='/sign-in' activeClassName='active' className='navbar-sign-in-link'>
                    Sign in
                </NavLink>
            </>
        )
    }


    return (
        <>
            {buttonContent}
        </>
    )
}






export default ProfileButton
