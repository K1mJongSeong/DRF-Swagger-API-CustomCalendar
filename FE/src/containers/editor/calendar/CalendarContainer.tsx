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
import { useAppDispatch, useAppSelector } from 'hooks';
import { RootState } from 'store';
import { updateDate } from 'reducer/memo';
import { selectId } from 'reducer/images';

interface DayCellProps {
  day: Date;
  selectedDate: Date;
  currentMonth: Date;
  monthStart: Date;
  holiday?: { dateName: string };
  formattedDate: string;
}

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
        formattedDate = format(day, 'd');
        days.push({
          day,
          selectedDate,
          currentMonth,
          monthStart,
          holiday: holiday[0],
          formattedDate,
        });
        day = addDays(day, 1);
      }
      rows.push(days);
      days = [];
    }

    return (
      <CalendarWrap rowLength={rows.length}>
        {rows.map((el) => (
          <Row key={uuid()} cells={el} />
        ))}
      </CalendarWrap>
    );
  } else {
    return null;
  }
};

const Row = ({ cells }: { cells: Array<DayCellProps> }) => {
  return (
    <div className="row">
      {cells.map((el) => (
        <DayCell
          key={uuid()}
          day={el.day}
          selectedDate={el.selectedDate}
          currentMonth={el.currentMonth}
          monthStart={el.monthStart}
          holiday={el.holiday}
          formattedDate={el.formattedDate}
        />
      ))}
    </div>
  );
};

const DayCell = (props: DayCellProps) => {
  const {
    day,
    selectedDate,
    currentMonth,
    monthStart,
    holiday,
    formattedDate,
  } = props;
  const dispatch = useAppDispatch();
  const { selectDate } = useAppSelector((state: RootState) => state.memo);

  const handleClickCell = (day: Date) => {
    dispatch(updateDate(day.toString()));
    dispatch(selectId(null));
  };

  return (
    <div
      className={
        selectDate && isSameDay(day, new Date(selectDate))
          ? `col cell on ${
              !isSameMonth(day, monthStart)
                ? 'disabled'
                : getDay(day) === 0 || holiday
                ? 'red'
                : 'not-valid'
            }`
          : `col cell ${
              !isSameMonth(day, monthStart)
                ? 'disabled'
                : getDay(day) === 0 || holiday
                ? 'red'
                : 'not-valid'
            }`
      }
      onClick={() => handleClickCell(day)}
    >
      <div className="cell_top">
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
        {holiday && <span className="red txt">{holiday.dateName}</span>}
      </div>
    </div>
  );
};

export default CalendarContainer;
