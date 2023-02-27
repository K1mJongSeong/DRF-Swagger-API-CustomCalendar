import { EditorTextButton } from 'components/editor/EditorButtons';
import EditorTop from 'components/editor/EditorTop';
import { useNavigate } from 'react-router';
import { BsCartPlus } from 'react-icons/bs';
import { MdArrowBackIos } from 'react-icons/md';

const EditorTopSection = ({ children }: { children: React.ReactNode }) => {
  const nevigate = useNavigate();
  const handleTestClick = () => {
    nevigate('/');
  };
  return (
    <EditorTop>
      <EditorTextButton white onClick={() => nevigate(-1)}>
        <MdArrowBackIos />
      </EditorTextButton>
      <div className="right">
        <EditorTextButton red onClick={handleTestClick}>
          저장
        </EditorTextButton>
        <EditorTextButton white>
          <BsCartPlus />
        </EditorTextButton>
      </div>
      {children}
    </EditorTop>
  );
};

export default EditorTopSection;
