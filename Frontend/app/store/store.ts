import { configureStore } from '@reduxjs/toolkit';
import responseReducer from '../features/responseSlice';
import { enableMapSet } from "immer";
enableMapSet();

export const store = configureStore({
  reducer: {
    response: responseReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
