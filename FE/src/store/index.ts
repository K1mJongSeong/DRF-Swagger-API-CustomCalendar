import { configureStore } from '@reduxjs/toolkit';
import auth from 'reducer/auth';
import images from 'reducer/images';
import order from 'reducer/order';

export const store = configureStore({
  reducer: {
    order: order,
    auth: auth,
    images: images,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
