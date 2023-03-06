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
      console.log(action.payload);
      state.imgs.push(action.payload);
    },
  },
});

export const { updateImg } = imagesSlice.actions;
export default imagesSlice.reducer;
