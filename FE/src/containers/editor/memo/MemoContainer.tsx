import MemoTemplate, { MemoForm } from 'components/editor/MemoTemplate';
import { format } from 'date-fns';
import { useAppDispatch, useAppSelector } from 'hooks';
import moment from 'moment';
import { useEffect, useState } from 'react';
import { updateDate } from 'reducer/memo';
import { RootState } from 'store';

const MemoContainer = () => {
  const dispatch = useAppDispatch();
  const { selectDate } = useAppSelector((state: RootState) => state.memo);

  const handleClose = () => {
    dispatch(updateDate(null));
  };

  const [targetDate, setTargetDate] = useState<string | null>(null);

  useEffect(() => {
    if (!selectDate) return;
    console.log(moment(selectDate).format('yyyy년 MM월 DD일'));
    setTargetDate(moment(selectDate).format('yyyy년 MM월 DD일'));
  }, [selectDate]);
  return (
    <MemoTemplate>
      <MemoForm onClose={handleClose} targetDate={targetDate} />
    </MemoTemplate>
  );
};

export default MemoContainer;
