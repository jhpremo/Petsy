import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { logout } from '../../store/session';

const LogoutButton = () => {
  const history = useHistory()
  const dispatch = useDispatch()
  const onLogout = async (e) => {
    await dispatch(logout());
    await history.push('/')
  };

  return <button onClick={onLogout}><i className="fa-solid fa-arrow-right-from-bracket" /> Logout</button>;
};

export default LogoutButton;
