import VisibleBackLoading from 'components/common/loading/VisibleBack';
import PBody from 'components/common/PBody';
import SelectYear from 'components/list/SelectYear';
import TempList from 'components/list/TempList';
import { Renault } from 'data/template/renault';
import { useAppDispatch, useAppSelector } from 'hooks';
import { useEffect, useState } from 'react';
import { useLocation, useNavigate, useParams } from 'react-router';
import {
  updatePrevLoading,
  getPage,
  updatePrevImgs,
  updateSavedPages,
  initialPageError,
  initialUpdatePageResult,
} from 'reducer/page';
import { RootState } from 'store';

const ListMainSection = ({ year }: { year?: string | null }) => {
  const dispatch = useAppDispatch();

  const {
    loading: pageLoading,
    getPageResult,
    error: pageError,
  } = useAppSelector((state: RootState) => state.page);

  const { nansu } = useParams();
  const [selectYear, setSelectYear] = useState<string | undefined | null>('');
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    setSelectYear(year);
  }, [year]);

  const handleChangeYears = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectYear(e.target.value);
  };

  const handleGotoSelectYear = () => {
    if (!selectYear) return alert('년도를 선택해주세요.');
    const { pathname, search } = location;
    navigate(`${pathname}${search}&year=${selectYear}`);
  };

  /** 첫 렌더링 시 작업리스트 가져오기 */
  useEffect(() => {
    if (!nansu) return;
    dispatch(updatePrevLoading(true));
    Renault.forEach((el) => {
      if (!el.pageName) return;
      dispatch(getPage({ pageName: el.pageName, nansu }));
    });
  }, []);

  useEffect(() => {
    if (!getPageResult) return;
    if (getPageResult.data && getPageResult.pageName) {
      dispatch(
        updatePrevImgs({
          data: getPageResult.data,
          pageName: getPageResult.pageName,
        }),
      );
      dispatch(updatePrevLoading(false));
      dispatch(updateSavedPages(getPageResult.pageName));
    }
  }, [getPageResult]);

  useEffect(() => {
    if (pageError) {
      alert('해당 템플릿을 가져올 수 없습니다.');
      navigate('/');
      dispatch(initialPageError());
      dispatch(initialUpdatePageResult());
      return;
    }
  }, [pageError]);

  return (
    <PBody>
      {pageLoading && <VisibleBackLoading />}
      {!year ? (
        <SelectYear
          onChange={handleChangeYears}
          onClick={handleGotoSelectYear}
        />
      ) : (
        <TempList />
      )}
    </PBody>
  );
};

export default ListMainSection;
