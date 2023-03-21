/* eslint-disable @typescript-eslint/no-explicit-any */
import ColorPicker from 'components/editor/ColorPicker';
import { EditorIconButton } from 'components/editor/EditorButtons';
import TextEditor, { CustomColorBtn } from 'components/editor/TextEditor';
import { useEffect, useState } from 'react';
import { BsTypeBold, BsTypeItalic, BsTypeUnderline } from 'react-icons/bs';

const TextEditContainer = ({
  editorIns,
  selectedObjId,
  selectedTxt,
  setSelectedTxt,
}: {
  editorIns: any;
  selectedObjId: number;
  selectedTxt: any;
  setSelectedTxt: React.Dispatch<any>;
}) => {
  /** bold */
  const handleTxtBold = () => {
    if (!editorIns || !selectedObjId) return;
    editorIns.changeTextStyle(selectedObjId, {
      fontWeight: 'bold',
    });
    setSelectedTxt((prev: any) => {
      const newObj = { ...prev };
      if (newObj['fontWeight'] === 'normal') {
        newObj['fontWeight'] = 'bold';
      } else {
        newObj['fontWeight'] = 'normal';
      }
      return newObj;
    });
  };
  /** italic */
  const handleTxtItaric = () => {
    if (!editorIns || !selectedObjId) return;
    editorIns.changeTextStyle(selectedObjId, {
      fontStyle: 'italic',
    });
    setSelectedTxt((prev: any) => {
      const newObj = { ...prev };
      if (newObj['fontStyle'] === 'normal') {
        newObj['fontStyle'] = 'italic';
      } else {
        newObj['fontStyle'] = 'normal';
      }
      return newObj;
    });
  };
  /** underLine */
  const handleTxtDeco = () => {
    if (!editorIns || !selectedObjId) return;
    editorIns.changeTextStyle(selectedObjId, {
      textDecoration: 'underline',
    });
    setSelectedTxt((prev: any) => {
      const newObj = { ...prev };
      if (newObj['textDecoration'] === undefined) {
        newObj['textDecoration'] = 'underline';
      } else {
        newObj['textDecoration'] = undefined;
      }
      return newObj;
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
    colPickInstance.on('selectColor', (e: { color: string }) => {
      editorIns.changeTextStyle(selectedObjId, {
        fill: e.color,
      });
      setSelectedTxt((prev: any) => {
        const newObj = { ...prev };
        newObj['fill'] = e.color;
        return newObj;
      });
    });
  }, [colPickInstance]);

  return (
    <TextEditor>
      <div className="txtStyleBtn_wrap">
        <EditorIconButton
          white
          fs="24"
          onClick={handleTxtBold}
          checked={selectedTxt?.fontWeight !== 'normal'}
        >
          <BsTypeBold />
        </EditorIconButton>
        <EditorIconButton
          white
          fs="24"
          onClick={handleTxtItaric}
          checked={selectedTxt?.fontStyle !== 'normal'}
        >
          <BsTypeItalic />
        </EditorIconButton>
        <EditorIconButton
          white
          fs="24"
          onClick={handleTxtDeco}
          checked={
            selectedTxt?.textDecoration !== undefined &&
            selectedTxt?.textDecoration !== ''
          }
        >
          <BsTypeUnderline />
        </EditorIconButton>
      </div>

      <div className="colorBtn_wrap">
        <CustomColorBtn
          onClick={handleToggleColPicker}
          color={selectedTxt.fill}
        />
        {cpVisible && (
          <ColorPicker
            setColPick={setColPickInstance}
            color={selectedTxt.fill}
          />
        )}
      </div>
    </TextEditor>
  );
};

export default TextEditContainer;
