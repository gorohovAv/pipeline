import {configureStore} from '@reduxjs/toolkit'

import dbElementsReducer from './reducers/dbElementsReducer';
import activeElementsReducer from './reducers/activeElementsReducer';


export default configureStore(
    {
        reducer: {
            dbElements: dbElementsReducer,
            activeElements: activeElementsReducer
        }
    }
);