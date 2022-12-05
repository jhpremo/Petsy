import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import items from './items'
import { itemReviewsReducer } from './itemReviews';
import { itemPageReducer } from './itemPage';
import { userReviewsReducer } from './userReview';
import { sellerReviewImagesReducer } from './sellerReviewImages';
import { orderPageReducer } from './orderPage';
import { modalReviewReducer } from './modalReview';

const rootReducer = combineReducers({
  session,
  itemPage: itemPageReducer,
  itemReviews: itemReviewsReducer,
  items,
  userReviews: userReviewsReducer,
  sellerReviewImages: sellerReviewImagesReducer,
  orders: orderPageReducer,
  modalReview: modalReviewReducer
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
