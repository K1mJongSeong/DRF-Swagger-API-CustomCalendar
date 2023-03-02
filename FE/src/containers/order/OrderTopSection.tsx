import Top from 'components/common/Top';
import { EditorIconButton } from 'components/editor/EditorButtons';
import { MdArrowBackIos } from 'react-icons/md';
import { useNavigate } from 'react-router';

const OrderTopSection = () => {
  const navigate = useNavigate();

  const handleClickBackBtn = () => {
    navigate(-1);
  };
  return (
    <Top>
      <EditorIconButton onClick={handleClickBackBtn}>
        <MdArrowBackIos />
      </EditorIconButton>
    </Top>
  );
};

export default OrderTopSection;
