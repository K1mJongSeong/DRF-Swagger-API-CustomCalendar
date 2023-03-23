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
import { useAppSelector } from 'hooks';
import { RootState } from 'store';
import moment from 'moment';
import { useEffect, useState } from 'react';

const CalendarContainer = ({
  month,
  months,
  selectedDate,
}: {
  month: any;
  months: Array<Date>;
  selectedDate: Date;
}) => {
  const { holidays } = useAppSelector((state: RootState) => state.holidays);
  const currentMonth = months.filter((el, idx) => idx === month - 1)[0];
  const monthStart = startOfMonth(currentMonth);
  const monthEnd = endOfMonth(monthStart);
  const startDate = startOfWeek(monthStart);
  const endDate = endOfWeek(monthEnd);

  const rows: any[] = [];
  let days: any[] = [];
  let day = startDate;
  let formattedDate = '';

  if (holidays.length !== 0) {
    while (day <= endDate && holidays) {
      for (let i = 0; i < 7; i++) {
        const holiday: Array<{ dateName: string }> = holidays.filter((el) => {
          if (isSameDay(day, new Date(el.date))) {
            return el;
          }
        });
        console.log(holiday);
        console.log(holiday.length);
        formattedDate = format(day, 'd');
        days.push(
          <div
            className={`col cell ${
              !isSameMonth(day, monthStart)
                ? 'disabled'
                : getDay(day) === 0 || holiday[0]
                ? 'red'
                : 'not-valid'
            }`}
            key={uuid()}
          >
            <div className="cell_top">
              <span
                className={
                  format(currentMonth, 'M') !== format(day, 'M')
                    ? 'text not-valid'
                    : isSameMonth(day, monthStart) &&
                      isSameDay(day, selectedDate)
                    ? 'text today'
                    : ''
                }
              >
                {formattedDate}
              </span>
              {holiday[0] && (
                <span className="red txt">{holiday[0].dateName}</span>
              )}
            </div>
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
  } else {
    return null;
  }
};

export default CalendarContainer;
