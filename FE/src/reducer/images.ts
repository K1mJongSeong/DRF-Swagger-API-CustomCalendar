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

export const { updateImg } = imagesSlice.actions;
export default imagesSlice.reducer;
