import { createSlice, PayloadAction } from '@reduxjs/toolkit';
export interface MemoState {
  selectDate: string | null;
  memoContent: string;
}

const initialState: MemoState = {
  selectDate: null,
  memoContent: '',
};
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
  },
});

export const { updateDate, changeMemoField } = MemoSlice.actions;
export default MemoSlice.reducer;
