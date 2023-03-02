import Top from 'components/common/Top';
import { EditorIconButton } from 'components/editor/EditorButtons';
import { MdArrowBackIos } from 'react-icons/md';

const OrderTopContainer = () => {
  return (
    <Top>
      <EditorIconButton>
        <MdArrowBackIos />
      </EditorIconButton>
    </Top>
  );
};

export default OrderTopContainer;
