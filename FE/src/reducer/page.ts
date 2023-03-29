/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import client from 'lib/api/client';

interface basicPageProps {
  pic: string | null;
  nansu: string;
}

interface postPageProps {
  pageName: string;
  pagePayload: basicPageProps;
}

interface getPageProps {
  pageName: string;
  nansu: string;
}

export interface PageState {
  postPageResult: any | null;
  loading: boolean;
  error: string | null | undefined;
  getPageResult: { data: Array<string>; pageName: string } | null;
  prevImgs: Array<{ data: Array<string>; pageName: string }>;
  getPrevLoading: boolean;
  getPrevDone: boolean;
}

const initialState: PageState = {
  postPageResult: null,
  loading: false,
  error: null,
  getPageResult: null,
  prevImgs: [],
  getPrevLoading: false,
  getPrevDone: false,
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

export const getPage = createAsyncThunk(
  'page/getPage',
  async (getPagePayload: getPageProps) => {
    const res = await client.get(
      `/${getPagePayload.pageName}/?nansu=${getPagePayload.nansu}`,
      {
        headers: { 'Content-Type': 'application/json' },
      },
    );
    if (Array.isArray(res.data)) {
      return { data: res.data[0]?.pic, pageName: getPagePayload.pageName };
    } else {
      return res.data;
    }
  },
);

export const pageSlice = createSlice({
  name: 'page',
  initialState,
  reducers: {
    initialPrevImgs: (state) => {
      state.prevImgs = [];
    },
    updatePrevImgs: (
      state,
      action: PayloadAction<{
        data: Array<string>;
        pageName: string;
      }>,
    ) => {
      let Arr = [];
      state.prevImgs.forEach((pv) => {
        if (pv.pageName === action.payload.pageName) {
          Arr = state.prevImgs.filter(
            (pv) => pv.pageName != action.payload.pageName,
          );
          state.prevImgs = Arr;
        }
      });
      state.prevImgs.push(action.payload);
    },
    updatePrevLoading: (state, aciton: PayloadAction<boolean>) => {
      state.getPrevLoading = aciton.payload;
    },
    updatePrevDone: (state) => {
      state.getPrevDone = true;
    },
  },
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
    builder.addCase(getPage.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.getPageResult = null;
    });
    builder.addCase(getPage.fulfilled, (state, action) => {
      state.loading = false;
      state.getPageResult = action.payload;
    });
    builder.addCase(getPage.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export const {
  initialPrevImgs,
  updatePrevImgs,
  updatePrevLoading,
  updatePrevDone,
} = pageSlice.actions;
export default pageSlice.reducer;
