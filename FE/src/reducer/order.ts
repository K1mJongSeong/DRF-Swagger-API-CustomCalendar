import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface OrderState {
  value: number;
  orderInfo: {
    userName: string;
    userPhone: string;
    postCode: string;
    address: string;
    detailAddress: string;
    [props: string]: unknown;
  };
}

const initialState: OrderState = {
  value: 0,
  orderInfo: {
    userName: '',
    userPhone: '',
    postCode: '',
    address: '',
    detailAddress: '',
  },
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
    changeFieldOrderForm: (
      state,
      action: {
        payload: {
          key: string;
          value: string;
        };
      },
    ) => {
      state.orderInfo[action.payload.key] = action.payload.value;
    },
  },
});

export const { increment, decrement, incrementByAmount, changeFieldOrderForm } =
  orderSlice.actions;
export default orderSlice.reducer;
