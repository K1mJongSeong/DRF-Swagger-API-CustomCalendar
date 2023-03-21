/* eslint-disable @typescript-eslint/no-explicit-any */
import ColorPicker from 'components/editor/ColorPicker';
import { EditorIconButton } from 'components/editor/EditorButtons';
import TextEditor, { CustomColorBtn } from 'components/editor/TextEditor';
import { useEffect, useState } from 'react';
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

  /** color picker */
  const [cpVisible, setCpVisible] = useState(false);
  const [colPickInstance, setColPickInstance] = useState<any>(null);

  const handleToggleColPicker = () => {
    setCpVisible(!cpVisible);
  };

  useEffect(() => {
    if (!colPickInstance) return;
    console.log(colPickInstance.getColor());
  }, [colPickInstance]);

  return (
    <TextEditor>
      <div className="txtStyleBtn_wrap">
        <EditorIconButton white fs="24" onClick={handleTxtBold}>
          <BsTypeBold />
        </EditorIconButton>
        <EditorIconButton white fs="24" onClick={handleTxtItaric}>
          <BsTypeItalic />
        </EditorIconButton>
        <EditorIconButton white fs="24" onClick={handleTxtDeco}>
          <BsTypeUnderline />
        </EditorIconButton>
      </div>

      <div className="colorBtn_wrap">
        <CustomColorBtn onClick={handleToggleColPicker} />
        {cpVisible && <ColorPicker setColPick={setColPickInstance} />}
      </div>
    </TextEditor>
  );
};

export default TextEditContainer;
