import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface ImagesState {
  imgs: Array<{ id: number; imgUrl: string; pageNo: number }>;
  selectedId: number | null;
  selectPageNo: number | null;
}

const initialState: ImagesState = {
  imgs: [],
  selectedId: null,
  selectPageNo: null,
};

export const imagesSlice = createSlice({
  name: 'images',
  initialState,
  reducers: {
    initialImgs: (state) => {
      state.imgs = [];
    },
    updateImg: (
      state,
      action: PayloadAction<{ id: number; imgUrl: string; pageNo: number }>,
    ) => {
      let Arr = [];
      state.imgs.forEach((i) => {
        if (i.id === action.payload.id) {
          Arr = state.imgs.filter((i) => i.id != action.payload.id);
          state.imgs = Arr;
        }
      });
      state.imgs.push(action.payload);
      state.imgs.sort((a, b) => a.id - b.id);
    },
    deleteImg: (
      state,
      action: PayloadAction<{ selectedId: number | null }>,
    ) => {
      const Arr = state.imgs.filter((i) => i.id != action.payload.selectedId);
      state.imgs = Arr;
    },
    selectId: (state, action: PayloadAction<number | null>) => {
      state.selectedId = action.payload;
    },
    selectPageNo: (state, action: PayloadAction<number | null>) => {
      state.selectPageNo = action.payload;
    },
  },
});

export const { initialImgs, updateImg, deleteImg, selectId, selectPageNo } =
  imagesSlice.actions;
export default imagesSlice.reducer;
