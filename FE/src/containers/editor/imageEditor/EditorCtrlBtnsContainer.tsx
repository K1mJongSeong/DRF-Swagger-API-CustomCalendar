/* eslint-disable @typescript-eslint/no-explicit-any */
import EditCtrlBtnsWrap from 'components/editor/EditCtrlBtnsWrap';
import { EditorIconButton } from 'components/editor/EditorButtons';
import { GrUndo, GrRedo } from 'react-icons/gr';
import { VscTrash } from 'react-icons/vsc';

const EditorCtrlBtnsContainer = ({
  undoSt,
  redoSt,
  onUndo,
  onRedo,
  isActive,
  onRemove,
}: {
  undoSt: boolean;
  redoSt: boolean;
  onUndo: () => void;
  onRedo: () => void;
  isActive: boolean;
  onRemove: () => void;
}) => {
  return (
    <EditCtrlBtnsWrap>
      <EditorIconButton white fs="20" disabled={undoSt} onClick={onUndo}>
        <GrUndo />
      </EditorIconButton>
      <EditorIconButton white fs="20" disabled={redoSt} onClick={onRedo}>
        <GrRedo />
      </EditorIconButton>
      {isActive && (
        <EditorIconButton red fs="20" onClick={onRemove}>
          <VscTrash />
        </EditorIconButton>
      )}
    </EditCtrlBtnsWrap>
  );
};

export default EditorCtrlBtnsContainer;
