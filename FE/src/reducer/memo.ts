/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import client from 'lib/api/client';

interface PostMemoProps {
  nansu: string;
  notice?: string;
  monthdays?: string;
}

export interface MemoState {
  selectDate: string | null;
  memoContent: string;
  postMemoPayload: PostMemoProps | null;
  postMemoResult: any | null;
  postError: string | null | undefined;
}

const initialState: MemoState = {
  selectDate: null,
  memoContent: '',
  postMemoPayload: null,
  postMemoResult: null,
  postError: null,
};

export const post = createAsyncThunk(
  'memo/postMemo',
  async (postMemoPayload: PostMemoProps) => {
    const res = await client.post('/Notice/', postMemoPayload, {
      headers: { 'Content-Type': 'application/json' },
    });
    return res.data;
  },
);

export const MemoSlice = createSlice({
  name: 'memo',
  initialState,
  reducers: {
    updateDate: (state, action: PayloadAction<string | null>) => {
      state.selectDate = action.payload;
    },
    changeMemoField: (state, action: PayloadAction<string>) => {
      state.memoContent = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(post.pending, (state) => {
      state.postError = null;
      state.postMemoResult = null;
    });
    builder.addCase(post.fulfilled, (state, action) => {
      state.postMemoResult = action.payload;
    });
    builder.addCase(post.rejected, (state, action) => {
      state.postError = action.error.message;
    });
  },
});

export const { updateDate, changeMemoField } = MemoSlice.actions;
export default MemoSlice.reducer;
