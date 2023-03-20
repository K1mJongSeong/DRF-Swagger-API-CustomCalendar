/* eslint-disable @typescript-eslint/no-explicit-any */
import { EditorIconButton } from 'components/editor/EditorButtons';
import TextEditor from 'components/editor/TextEditor';
import { BsTypeBold, BsTypeItalic, BsTypeUnderline } from 'react-icons/bs';

const TextEditContainer = ({
  editorIns,
  selectedObjId,
}: {
  editorIns: any;
  selectedObjId: number;
}) => {
  /** bold */
  const handleTxtBold = () => {
    if (!editorIns || !selectedObjId) return;
    editorIns.changeTextStyle(selectedObjId, {
      fontWeight: 'bold',
    });
  };
  /** italic */
  const handleTxtItaric = () => {
    if (!editorIns || !selectedObjId) return;
    editorIns.changeTextStyle(selectedObjId, {
      fontStyle: 'italic',
    });
  };
  /** underLine */
  const handleTxtDeco = () => {
    if (!editorIns || !selectedObjId) return;
    editorIns.changeTextStyle(selectedObjId, {
      textDecoration: 'underline',
    });
  };

  return (
    <TextEditor>
      <EditorIconButton white fs="24" onClick={handleTxtBold}>
        <BsTypeBold />
      </EditorIconButton>
      <EditorIconButton white fs="24" onClick={handleTxtItaric}>
        <BsTypeItalic />
      </EditorIconButton>
      <EditorIconButton white fs="24" onClick={handleTxtDeco}>
        <BsTypeUnderline />
      </EditorIconButton>
    </TextEditor>
  );
};

export default TextEditContainer;
