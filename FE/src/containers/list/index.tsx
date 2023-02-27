import { useSearchParams } from 'react-router-dom';
import ListMainSection from './ListMainSection';
import ListTopSection from './ListTopSection';

const ListContainer = () => {
  const [searchParam] = useSearchParams();
  const temp = searchParam?.get('temp');
  const year = searchParam?.get('year');
  return (
    <>
      <ListTopSection temp={temp} />
      <ListMainSection year={year} />
    </>
  );
};

export default ListContainer;
