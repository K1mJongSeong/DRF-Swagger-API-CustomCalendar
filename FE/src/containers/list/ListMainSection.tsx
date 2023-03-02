import PBody from 'components/common/PBody';
import SelectYear from 'components/list/SelectYear';
import TempList from 'components/list/TempList';
import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router';

const ListMainSection = ({ year }: { year?: string | null }) => {
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

  return (
    <PBody>
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
