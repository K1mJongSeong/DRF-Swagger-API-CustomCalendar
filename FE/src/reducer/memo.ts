/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import client from 'lib/api/client';

interface BasicMemoProps {
  nansu: string;
  monthdays: string;
}
export interface PostMemoProps extends BasicMemoProps {
  notice: string;
}

export interface MemoState {
  loading: boolean;
  selectDate: string | null;
  memoContent: string;
  postMemoPayload: PostMemoProps | null;
  resMemoResult: any | null;
  getMemoListResult: Array<PostMemoProps> | null;
  error: string | null | undefined;
  isMemo: boolean;
}

const initialState: MemoState = {
  loading: false,
  selectDate: null,
  memoContent: '',
  postMemoPayload: null,
  resMemoResult: null,
  getMemoListResult: null,
  error: null,
  isMemo: false,
};

export const postMemo = createAsyncThunk(
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

export const updateMemo = createAsyncThunk(
  'memo/updateMemo',
  async (updateMemoPayload: PostMemoProps) => {
    const res = await client.put('/Notice/', updateMemoPayload, {
      headers: { 'Content-Type': 'application/json' },
    });
    return res.data;
  },
);

export const removeMemo = createAsyncThunk(
  'memo/removeMemo',
  async (removeMemoPayload: BasicMemoProps) => {
    const res = await client.delete(
      `/Notice/?monthdays=${removeMemoPayload.monthdays}&nansu=${removeMemoPayload.nansu}`,
    );
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
      state.resMemoResult = null;
    },
    initialMemoError: (state) => {
      state.error = null;
    },
    hasMemo: (state, action: PayloadAction<boolean>) => {
      state.isMemo = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(postMemo.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.resMemoResult = null;
    });
    builder.addCase(postMemo.fulfilled, (state, action) => {
      state.loading = false;
      state.resMemoResult = action.payload;
    });
    builder.addCase(postMemo.rejected, (state, action) => {
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
    builder.addCase(updateMemo.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.resMemoResult = null;
    });
    builder.addCase(updateMemo.fulfilled, (state, action) => {
      state.loading = false;
      state.resMemoResult = action.payload;
    });
    builder.addCase(updateMemo.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
    builder.addCase(removeMemo.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.resMemoResult = null;
    });
    builder.addCase(removeMemo.fulfilled, (state) => {
      state.loading = false;
    });
    builder.addCase(removeMemo.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export const {
  updateDate,
  changeMemoField,
  initialPostResult,
  initialMemoError,
  hasMemo,
} = MemoSlice.actions;
export default MemoSlice.reducer;
