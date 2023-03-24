/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import client from 'lib/api/client';

export interface PostMemoProps {
  nansu: string;
  notice: string;
  monthdays: string;
}

export interface MemoState {
  loading: boolean;
  selectDate: string | null;
  memoContent: string;
  postMemoPayload: PostMemoProps | null;
  postMemoResult: any | null;
  getMemoListResult: Array<PostMemoProps> | null;
  error: string | null | undefined;
}

const initialState: MemoState = {
  loading: false,
  selectDate: null,
  memoContent: '',
  postMemoPayload: null,
  postMemoResult: null,
  getMemoListResult: null,
  error: null,
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
export const getMemoList = createAsyncThunk(
  'memo/getMemoList',
  async (nansu: string) => {
    const res = await client.get(`/Notice/?nansu=${nansu}`, {
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
    initialPostResult: (state) => {
      state.postMemoResult = null;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(post.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.postMemoResult = null;
    });
    builder.addCase(post.fulfilled, (state, action) => {
      state.loading = false;
      state.postMemoResult = action.payload;
    });
    builder.addCase(post.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
    builder.addCase(getMemoList.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.getMemoListResult = null;
    });
    builder.addCase(getMemoList.fulfilled, (state, action) => {
      state.loading = false;
      state.getMemoListResult = action.payload;
    });
    builder.addCase(getMemoList.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export const { updateDate, changeMemoField, initialPostResult } =
  MemoSlice.actions;
export default MemoSlice.reducer;
