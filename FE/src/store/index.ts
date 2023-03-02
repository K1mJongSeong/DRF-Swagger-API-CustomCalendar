import { configureStore } from '@reduxjs/toolkit';
import { orderSlice } from 'reducer/order';

export const store = configureStore({
  reducer: {
    order: orderSlice.reducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
