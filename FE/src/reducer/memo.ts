import { createSlice, PayloadAction } from '@reduxjs/toolkit';
export interface MemoState {
  selectDate: string | null;
}

const initialState: MemoState = {
  selectDate: null,
};
export const MemoSlice = createSlice({
  name: 'memo',
  initialState,
  reducers: {
    updateDate: (state, action: PayloadAction<string | null>) => {
      state.selectDate = action.payload;
    },
  },
});

export const { updateDate } = MemoSlice.actions;
export default MemoSlice.reducer;
