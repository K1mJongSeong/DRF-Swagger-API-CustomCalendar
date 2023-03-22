/* eslint-disable @typescript-eslint/no-explicit-any */
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

export interface HolidaysState {
  loading: boolean;
  result: any;
  error: string | null | undefined;
  holidays: Array<any>;
}

const initialState: HolidaysState = {
  loading: false,
  result: null,
  error: null,
  holidays: [],
};
export const getHolidays = createAsyncThunk(
  'holidays/getHolidays',
  async (month: string) => {
    const res = await axios.get(
      `http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?solYear=2023&solMonth=${month}&_type=json&ServiceKey=${process.env.REACT_APP_GET_HOLIDAY_KEY}`,
      {
        headers: { 'Content-Type': 'application/json' },
        timeout: 5000,
      },
    );
    return res.data.response.body.items.item;
  },
);

const holidaysSlice = createSlice({
  name: 'holidays',
  initialState,
  reducers: {
    addHoliday: (state, action) => {
      state.holidays.push(action.payload);
    },
  },
  extraReducers: (builder) => {
    builder.addCase(getHolidays.pending, (state) => {
      state.result = null;
      state.error = null;
      state.loading = true;
    });
    builder.addCase(getHolidays.fulfilled, (state, action) => {
      state.error = null;
      state.loading = false;
      state.result = action.payload;
    });
    builder.addCase(getHolidays.rejected, (state, action) => {
      state.loading = false;
      state.error = action.error.message;
    });
  },
});

export default holidaysSlice.reducer;
