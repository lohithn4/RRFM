import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import BooksReducer from './reducer_books';
import auth from './auth';
import data from './data';
import ActiveBook from './reducer_active_book';
import WeatherReducer from './reducer_weather';

const rootReducer = combineReducers({
    weather: WeatherReducer,
    books: BooksReducer,
    activeBook: ActiveBook,
    routing: routerReducer,
    /* your reducers */
    auth,
    data,
});

export default rootReducer;
