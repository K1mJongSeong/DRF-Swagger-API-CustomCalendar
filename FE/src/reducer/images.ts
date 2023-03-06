import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface ImagesState {
  imgs: Array<{ id: number; imgUrl: string }>;
}

const initialState: ImagesState = {
  imgs: [],
};

export const imagesSlice = createSlice({
  name: 'images',
  initialState,
  reducers: {
    uploadImg: (
      state,
      action: PayloadAction<{ id: number; imgUrl: string }>,
    ) => {
      state.imgs.push(action.payload);
    },
    updateImg: (
      state,
      action: PayloadAction<{ id: number; imgUrl: string }>,
    ) => {
      let Arr = [];
      state.imgs.forEach((i) => {
        if (i.id === action.payload.id) {
          Arr = state.imgs.filter((i) => i.id != action.payload.id);
          state.imgs = Arr;
        }
      });
      state.imgs.push(action.payload);
    },
  },
});

export const { uploadImg, updateImg } = imagesSlice.actions;
export default imagesSlice.reducer;
