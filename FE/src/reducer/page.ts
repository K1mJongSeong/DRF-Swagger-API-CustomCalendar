/* eslint-disable camelcase */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import client from 'lib/api/client';

interface basicPageProps {
  pic: string;
  nansu: string;
  total_pic: string;
}

interface postPageProps {
  pageName: string;
  pageNo: number;
  pagePayload: basicPageProps;
}

interface getPageProps {
  pageName: string;
  nansu: string;
  pageNo: number;
}

export interface PageState {
  postPageResult: {
    result: { pic: Array<string>; nansu: string; total_pic: string };
    pageName: string;
    pageNo: number;
  } | null;
  loading: boolean;
  error: string | null | undefined;
  getPageResult: {
    data: Array<string>;
    pageName: string;
    total_pic: string;
    pageNo: number;
  } | null;
  prevImgs: Array<{ data: Array<string>; pageName: string }>;
  getPrevLoading: boolean;
  getPrevDone: boolean;
  savedPages: Array<string>;
  updatePageResult: {
    result: { pic: Array<string>; nansu: string; total_pic: string };
    pageName: string;
    pageNo: number;
  } | null;
  totalPicArr: Array<{ total_pic: string; pageName: string; pageNo: number }>;
}

const initialState: PageState = {
  postPageResult: null,
  loading: false,
  error: null,
  getPageResult: null,
  prevImgs: [],
  getPrevLoading: false,
  getPrevDone: false,
  savedPages: [],
  updatePageResult: null,
  totalPicArr: [],
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
    return {
      result: res.data,
      pageName: postPagePayload.pageName,
      pageNo: postPagePayload.pageNo,
    };
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
      return {
        data: res.data[0]?.pic,
        pageName: getPagePayload.pageName,
        total_pic: res.data[0].total_pic,
        pageNo: getPagePayload.pageNo,
      };
    } else {
      return res.data;
    }
  },
);

export const updatePage = createAsyncThunk(
  'page/updatePage',
  async (updatePagePayload: postPageProps) => {
    const res = await client.put(
      `/${updatePagePayload.pageName}Put/${updatePagePayload.pagePayload.nansu}/`,
      updatePagePayload.pagePayload,
      {
        headers: { 'Content-Type': 'application/json' },
      },
    );
    return {
      result: res.data,
      pageName: updatePagePayload.pageName,
      pageNo: updatePagePayload.pageNo,
    };
  },
);

export const pageSlice = createSlice({
  name: 'page',
  initialState,
  reducers: {
    initialPageError: (state) => {
      state.error = null;
    },
    initialPostPageResult: (state) => {
      state.postPageResult = null;
    },
    initialUpdatePageResult: (state) => {
      state.updatePageResult = null;
    },
    initialPrevImgs: (state) => {
      state.prevImgs = [];
    },
    initialTotalPicArr: (state) => {
      state.totalPicArr = [];
    },
    afterPrintPrevImgs: (state, action: PayloadAction<string>) => {
      const newArr = state.prevImgs.filter(
        (el) => el.pageName !== action.payload,
      );
      state.prevImgs = newArr;
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
    updatePrevLoading: (state, action: PayloadAction<boolean>) => {
      state.getPrevLoading = action.payload;
    },
    updatePrevDone: (state) => {
      state.getPrevDone = true;
    },
    updateSavedPages: (state, action: PayloadAction<string>) => {
      let Arr = [];
      state.savedPages.forEach((sp) => {
        if (sp === action.payload) {
          Arr = state.savedPages.filter((el) => el != action.payload);
          state.savedPages = Arr;
        }
      });
      state.savedPages.push(action.payload);
    },
    updateTotalPicArr: (
      state,
      action: PayloadAction<{
        pageName: string;
        total_pic: string;
        pageNo: number;
      }>,
    ) => {
      let Arr = [];
      state.totalPicArr.forEach((sp) => {
        if (sp.pageName === action.payload.pageName) {
          Arr = state.totalPicArr.filter(
            (el) => el.pageName != action.payload.pageName,
          );
          state.totalPicArr = Arr;
        }
      });
      state.totalPicArr.push(action.payload);
      state.totalPicArr.sort((a, b) => a.pageNo - b.pageNo);
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
    builder.addCase(updatePage.pending, (state) => {
      state.loading = true;
      state.error = null;
      state.updatePageResult = null;
    });
    builder.addCase(updatePage.fulfilled, (state, action) => {
      state.loading = false;
      state.updatePageResult = action.payload;
    });
    builder.addCase(updatePage.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export const {
  initialPageError,
  initialPrevImgs,
  afterPrintPrevImgs,
  initialUpdatePageResult,
  initialTotalPicArr,
  updatePrevImgs,
  updatePrevLoading,
  updatePrevDone,
  updateSavedPages,
  updateTotalPicArr,
} = pageSlice.actions;
export default pageSlice.reducer;
