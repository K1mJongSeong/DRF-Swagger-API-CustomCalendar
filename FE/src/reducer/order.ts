import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface OrderState {
  value: number;
}

const initialState: OrderState = {
  value: 0,
};

export const orderSlice = createSlice({
  name: 'order',
  initialState,

  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },

    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
});

export const { increment, decrement, incrementByAmount } = orderSlice.actions;
export default orderSlice.reducer;
