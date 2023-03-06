import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface ImagesState {
  imgs: Array<{ id: number; imgUrl: string }>;
  selectedId: number | null;
}

const initialState: ImagesState = {
  imgs: [],
  selectedId: null,
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
    selectId: (state, action: PayloadAction<number | null>) => {
      state.selectedId = action.payload;
    },
  },
});

export const { updateImg, selectId } = imagesSlice.actions;
export default imagesSlice.reducer;
