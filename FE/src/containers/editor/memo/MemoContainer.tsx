import MemoTemplate, { MemoForm } from 'components/editor/MemoTemplate';
import { useAppDispatch, useAppSelector } from 'hooks';
import moment from 'moment';
import { useEffect, useState } from 'react';
import { changeMemoField, updateDate } from 'reducer/memo';
import { RootState } from 'store';

const MemoContainer = () => {
  const dispatch = useAppDispatch();
  const { selectDate } = useAppSelector((state: RootState) => state.memo);

  const handleClose = () => {
    dispatch(updateDate(null));
    dispatch(changeMemoField(''));
  };

  const [targetDate, setTargetDate] = useState<string | null>(null);

  useEffect(() => {
    if (selectDate) {
      setTargetDate(moment(selectDate).format('yyyy년 MM월 DD일'));
    } else {
      setTargetDate(null);
    }
  }, [selectDate]);

  const handleChangeMemo = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const { value } = e.target;
    const maxRows = 3;
    const lineCount = (value.match(/[^\n]*\n[^\n]*/gi)?.length ?? 1) + 1;
    if (lineCount > maxRows) {
      alert('최대 3줄까지 작성 가능합니다.');
      return;
    }
    dispatch(changeMemoField(value));
  };

  return (
    <MemoTemplate>
      <MemoForm
        onClose={handleClose}
        targetDate={targetDate}
        onChange={handleChangeMemo}
      />
    </MemoTemplate>
  );
};

export default MemoContainer;
