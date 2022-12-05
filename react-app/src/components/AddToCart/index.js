// AddToCart/index.js

import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getItemDetailsThunk } from "../../store/itemPage";
import { useHistory } from "react-router-dom";

import "../AddToCart/AddToCart.css";

const AddToCart = ({ itemId }) => {
  let localStorageCart = JSON.parse(localStorage.getItem("cart") || "[]");
  const dispatch = useDispatch();
  const [cart, setCart] = useState(localStorageCart);
  // const [trackCart, setTrackCart] = useState("");
  if (!cart) {
    setCart([]);
  }

  const history = useHistory();

  useEffect(() => {
    dispatch(getItemDetailsThunk(itemId)).catch((res) => "error");
  }, [dispatch, itemId]);

  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart));
    window.dispatchEvent(new Event('storage'))
    // console.log("useEffect in add item running");
  }, [cart]);

  const item = useSelector((state) => state.itemPage);

  if (!item) return null;

  let productInfo = {
    previewImg: item.imageURLs[0],
    name: item.name,
    shopName: item.shopName,
    price: item.price,
    itemId
  };

  // console.log("this is cart in addtocart", cart);

  const addToCart = async (productInfo) => {
    let cartArray = [...cart];

    // if (!localStorageCart) {
    //   let initialItem = { ...productInfo, quantity: 1 };
    //   setCart([initialItem]);
    // }

    // console.log("this is productInfo", productInfo);

    let foundItem = cartArray.find(
      (item) => productInfo.itemId === item.itemId
    );

    // console.log("this is found item in ATC before check", foundItem);

    if (foundItem) {
      // console.log("this is adding quantity");
      foundItem.quantity += 1;
    } else {
      // console.log("this is adding item if not found");
      foundItem = { ...productInfo, quantity: 1 };
      cartArray.push(foundItem);
      // console.log("this is cartArray after push", cartArray);
    }

    // console.log("this is cartArray", cartArray);
    // console.log("this is cart before set", cart);
    await setCart(cartArray);
    // console.log("this is cart after set", cart);
    history.push("/cart");
  };

  return (
    <button
      className='AddToCart--button-component'
      onClick={() => addToCart(productInfo)}
      type='button'>
      Add to cart
    </button>
  );
};

export default AddToCart;
