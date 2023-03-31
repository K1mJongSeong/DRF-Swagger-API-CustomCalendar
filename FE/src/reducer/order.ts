/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import client from 'lib/api/client';

interface postOrderPayload {
  user_name: string;
  user_phone: string;
  address: string;
  nansu?: string;
  postcode: string;
  detailAddress: string;
  orderState: string;
  order_date: string;
  pic: string;
}
interface postOrderProps {
  nansu: string;
  postOrderPayload: postOrderPayload;
}
export interface OrderState {
  loading: boolean;
  value: number;
  orderInfo: {
    userName: string;
    userPhone: string;
    postCode: string;
    address: string;
    detailAddress: string;
    [props: string]: unknown;
  };
  postOrderResult: any | null;
  error: string | null | undefined;
}

const initialState: OrderState = {
  loading: false,
  value: 0,
  orderInfo: {
    userName: '',
    userPhone: '',
    postCode: '',
    address: '',
    detailAddress: '',
  },
  postOrderResult: null,
  error: null,
};

export const postOrder = createAsyncThunk(
  'order/postOrder',
  async ({ nansu, postOrderPayload }: postOrderProps) => {
    const res = await client.post(
      `/OrderUrlDetail/${nansu}/`,
      postOrderPayload,
      {
        headers: { 'Content-Type': 'application/json' },
      },
    );
    return res.data;
  },
);

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
  extraReducers: (builder) => {
    builder.addCase(postOrder.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.postOrderResult = null;
    });
    builder.addCase(postOrder.fulfilled, (state, action) => {
      state.loading = false;
      state.postOrderResult = action.payload;
    });
    builder.addCase(postOrder.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export const { increment, decrement, incrementByAmount, changeFieldOrderForm } =
  orderSlice.actions;
export default orderSlice.reducer;
