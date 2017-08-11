import {  FETCH_WEATHER,} from '../constants/index';
const API_KEY = '993f686c7dbf308f11228938ac62cf94';
const ROOT_URL = `https://api.openweathermap.org/data/2.5/forecast?appid=${API_KEY}`;
import axios from 'axios';



export function fetchWeather(city){
  const url = `${ROOT_URL}&q=${city},us`;
  const request = axios.get(url);


  return {
    type: FETCH_WEATHER,
    payload: request
  };
}
export function selectBook(book){
  // console.log('A book has been selected:', book.title);
  // selectBook is an actionCreator, it needs to return an action,
  // an object with a type property.
  return {
    type: 'BOOK_SELECTED',
    payload: book
  };
}
