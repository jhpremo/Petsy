import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/navbar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import ProductsContainer from "./components/MainPage/ProductsContainer/ProductsContainer";
import { authenticate } from "./store/session";
import ListProductForm from "./components/listProductForm/ListProductForm";
import ItemDetailsPage from "./components/ItemDetialsPage";
import EditItemForm from "./components/EditItemForm";
import AddReviewForm from "./components/AddReviewForm";
import ShoppingCart from "./components/ShoppingCart";
import YourReviews from "./components/YourReviews/YourReviews";
import YourOrders from "./components/YourOrders/YourOrders";

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <hr />
      <Switch>
        <Route
          path='/sign-in'
          exact={true}>
          <div className='sign-up-forms-wrapper'>
            <LoginForm />
            <SignUpForm />
          </div>
        </Route>
        <Route
          path='/list-product'
          exact={true}>
          <ListProductForm />
        </Route>
        <ProtectedRoute
          path='/users'
          exact={true}>
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute
          path='/users/:userId'
          exact={true}>
          <User />
        </ProtectedRoute>
        <Route
          path='/'
          exact={true}>
          <ProductsContainer isSearch={false} />
        </Route>
        <Route
          path='/search'
          exact={true}>
          <ProductsContainer isSearch={true} />
        </Route>
        <Route
          exact
          path='/items/:itemId/edit-item'>
          <EditItemForm />
        </Route>
        <Route exact path='/items/:itemId/add-review'>
          <AddReviewForm />
        </Route>
        <Route exact path='/items/:itemId'>
          <ItemDetailsPage />
        </Route>
        <Route path='/cart'>
          <ShoppingCart />
        </Route>
        <Route path='/your-reviews'>
          <YourReviews />
        </Route>
        <Route path='/your-orders'>
          <YourOrders />
        </Route>
        <Route exact path='/404'>
          <h1>404 Error: Not found</h1>
        </Route>
        <Route exact path='/403'>
          <h1>403 Error: Forbidden</h1>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
