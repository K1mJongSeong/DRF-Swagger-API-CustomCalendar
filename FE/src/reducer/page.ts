/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import client from 'lib/api/client';

interface basicPageProps {
  pic: string | null;
  nansu: string;
}

interface postPageProps {
  pageName: string;
  pagePayload: basicPageProps;
}

export interface PageState {
  postPageResult: any | null;
  loading: boolean;
  error: string | null | undefined;
}

const initialState: PageState = {
  postPageResult: null,
  loading: false,
  error: null,
};

export const postPage = createAsyncThunk(
  'page/postPage',
  async (postPagePayload: postPageProps) => {
    const res = await client.post(
      `/${postPagePayload.pageName}/`,
      postPagePayload.pagePayload,
      {
        headers: { 'Content-Type': 'application/json' },
      },
    );
    return res.data;
  },
);

export const pageSlice = createSlice({
  name: 'page',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(postPage.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.postPageResult = null;
    });
    builder.addCase(postPage.fulfilled, (state, action) => {
      state.loading = false;
      state.postPageResult = action.payload;
    });
    builder.addCase(postPage.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

// export const {} = pageSlice.actions;
export default pageSlice.reducer;
