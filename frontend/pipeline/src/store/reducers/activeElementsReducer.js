import { createSlice } from "@reduxjs/toolkit";

export const activeElementsReducer = createSlice({
    name: 'activeElents',
    initialState: {
        value: []
    },
    reducers: {
        addElement: (state, action) => {
            state.value = [...state.value, action.payload]
        },
        deleteElement: (state, action) => {
            state.value = state.value.filter(elements => elements !== action.payload)
        }
    }
});

export const { addElement, deleteElement } = activeElementsReducer.actions;

export default activeElementsReducer.reducer;