import VisibleBackLoading from 'components/common/loading/VisibleBack';
import MemoTemplate, { MemoForm } from 'components/editor/MemoTemplate';
import { useAppDispatch, useAppSelector } from 'hooks';
import moment from 'moment';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import {
  changeMemoField,
  getMemoList,
  initialPostResult,
  post,
  updateDate,
} from 'reducer/memo';
import { RootState } from 'store';

const MemoContainer = () => {
  const params = useParams();
  const dispatch = useAppDispatch();
  const { loading, selectDate, memoContent, postMemoResult, error } =
    useAppSelector((state: RootState) => state.memo);

  const { nansu } = params;

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

  const handlePostMemo = () => {
    if (!nansu || !selectDate) return;
    if (!memoContent) return alert('메모를 입력해주세요');
    if (memoContent.length > 50) return alert('50자 이내로 작성해주세요.');
    dispatch(post({ nansu, monthdays: selectDate, notice: memoContent }));
  };

  useEffect(() => {
    if (error) {
      alert(error);
      return;
    }

    if (postMemoResult && nansu) {
      dispatch(updateDate(null));
      dispatch(changeMemoField(''));
      dispatch(initialPostResult());
      dispatch(getMemoList(nansu));
    }
  }, [postMemoResult, error]);

  return (
    <>
      <MemoTemplate>
        <MemoForm
          onClose={handleClose}
          targetDate={targetDate}
          onChange={handleChangeMemo}
          onPost={handlePostMemo}
        />
      </MemoTemplate>
      {loading && <VisibleBackLoading />}
    </>
  );
};

export default MemoContainer;
