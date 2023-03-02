import Top from 'components/common/Top';
import { EditorIconButton } from 'components/editor/EditorButtons';
import { MdArrowBackIos } from 'react-icons/md';
import { useNavigate, useParams } from 'react-router';
import { useSearchParams } from 'react-router-dom';

const ListTopSection = ({ temp }: { temp: string | null }) => {
  const navigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();
  const handleClickBackBtn = () => {
    const year = searchParams?.get('year');
    const { nansu } = params;
    const temp = searchParams?.get('temp');

    if (year) return navigate(`/${nansu}/list?temp=${temp}`);

    navigate(`/${nansu}`);
  };

  return (
    <Top>
      <EditorIconButton onClick={handleClickBackBtn}>
        <MdArrowBackIos />
      </EditorIconButton>
      {temp}
    </Top>
  );
};

export default ListTopSection;
