import { EditorIconButton } from 'components/editor/EditorButtons';
import ListTop from 'components/list/ListTop';
import { MdArrowBackIos } from 'react-icons/md';
import { useNavigate } from 'react-router';

const ListTopSection = ({ temp }: { temp: string | null }) => {
  const navigate = useNavigate();
  return (
    <ListTop>
      <EditorIconButton onClick={() => navigate(-1)}>
        <MdArrowBackIos />
      </EditorIconButton>
      {temp}
    </ListTop>
  );
};

export default ListTopSection;
