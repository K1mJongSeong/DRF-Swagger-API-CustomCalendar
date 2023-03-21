/* eslint-disable @typescript-eslint/no-explicit-any */
import EditCtrlBtnsWrap from 'components/editor/EditCtrlBtnsWrap';
import { EditorIconButton } from 'components/editor/EditorButtons';
import { useEffect, useState } from 'react';
import { GrUndo, GrRedo } from 'react-icons/gr';

const EditorCtrlBtnsContainer = ({ editorIns }: { editorIns: any }) => {
  const [undoSt, setUndoSt] = useState<boolean>(false);
  const [redoSt, setRedoSt] = useState<boolean>(false);
  useEffect(() => {
    if (!editorIns) return;
    console.log(editorIns.isEmptyUndoStack());
    console.log(editorIns.isEmptyRedoStack());
    setUndoSt(editorIns.isEmptyUndoStack());
    setRedoSt(editorIns.isEmptyRedoStack());
  }, [editorIns]);

  return (
    <EditCtrlBtnsWrap>
      <EditorIconButton white fs="20" isOpacity={undoSt}>
        <GrUndo />
      </EditorIconButton>
      <EditorIconButton white fs="20" isOpacity={redoSt}>
        <GrRedo />
      </EditorIconButton>
    </EditCtrlBtnsWrap>
  );
};

export default EditorCtrlBtnsContainer;
