/* eslint-disable @typescript-eslint/no-explicit-any */
import {
  format,
  startOfWeek,
  addDays,
  endOfWeek,
  isSameDay,
  isSameMonth,
  startOfMonth,
  endOfMonth,
  getDay,
} from 'date-fns';
import uuid from 'react-uuid';
import CalendarWrap from 'components/editor/calendar/CalendarWrap';
import { useEffect } from 'react';

const CalendarContainer = ({
  month,
  months,
  selectedDate,
}: {
  month: any;
  months: Array<Date>;
  selectedDate: Date;
}) => {
  const currentMonth = months.filter((el, idx) => idx === month - 1)[0];
  const monthStart = startOfMonth(currentMonth);
  const monthEnd = endOfMonth(monthStart);
  const startDate = startOfWeek(monthStart);
  const endDate = endOfWeek(monthEnd);

  const rows: any[] = [];
  let days: any[] = [];
  let day = startDate;
  let formattedDate = '';

  while (day <= endDate) {
    console.log(day);
    for (let i = 0; i < 7; i++) {
      formattedDate = format(day, 'd');
      days.push(
        <div
          className={`col cell ${
            !isSameMonth(day, monthStart)
              ? 'disabled'
              : getDay(day) === 0
              ? 'red'
              : 'not-valid'
          }`}
          key={uuid()}
        >
          <span
            className={
              format(currentMonth, 'M') !== format(day, 'M')
                ? 'text not-valid'
                : isSameMonth(day, monthStart) && isSameDay(day, selectedDate)
                ? 'text today'
                : ''
            }
          >
            {formattedDate}
          </span>
        </div>,
      );
      day = addDays(day, 1);
    }
    rows.push(
      <div className="row" key={uuid()}>
        {days}
      </div>,
    );
    days = [];
  }

  return <CalendarWrap>{rows}</CalendarWrap>;
};

export default CalendarContainer;
