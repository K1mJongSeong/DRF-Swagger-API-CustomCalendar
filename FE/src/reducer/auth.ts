/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import client from 'lib/api/client';

export interface AuthState {
  loading: boolean;
  result: {
    data: { nansu: string; nansu_state: string };
    status: number;
  } | null;
  error: string | null | undefined;
}

const initialState: AuthState = {
  loading: false,
  result: null,
  error: null,
};

export const getVerifyNansu = createAsyncThunk(
  'auth/getVerifyNansu',
  async (nansu: string) => {
    const res = await client.get(`/NansuUrlDetail/${nansu}/`);
    return res;
  },
);

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(getVerifyNansu.pending, (state) => {
      state.error = null;
      state.loading = true;
    });
    builder.addCase(getVerifyNansu.fulfilled, (state, action) => {
      state.error = null;
      state.loading = false;
      state.result = action.payload;
    });
    builder.addCase(getVerifyNansu.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export default authSlice.reducer;
