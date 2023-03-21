/* eslint-disable @typescript-eslint/no-explicit-any */
import EditCtrlBtnsWrap from 'components/editor/EditCtrlBtnsWrap';
import { EditorIconButton } from 'components/editor/EditorButtons';
import { GrUndo, GrRedo } from 'react-icons/gr';

const EditorCtrlBtnsContainer = ({
  undoSt,
  redoSt,
  onUndo,
  onRedo,
}: {
  undoSt: boolean;
  redoSt: boolean;
  onUndo: () => void;
  onRedo: () => void;
}) => {
  return (
    <EditCtrlBtnsWrap>
      <EditorIconButton white fs="20" disabled={undoSt} onClick={onUndo}>
        <GrUndo />
      </EditorIconButton>
      <EditorIconButton white fs="20" disabled={redoSt} onClick={onRedo}>
        <GrRedo />
      </EditorIconButton>
    </EditCtrlBtnsWrap>
  );
};

export default EditorCtrlBtnsContainer;
