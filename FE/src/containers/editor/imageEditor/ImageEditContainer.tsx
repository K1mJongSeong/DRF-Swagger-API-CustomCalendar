/* eslint-disable @typescript-eslint/no-explicit-any */
import { EditorIconButton } from 'components/editor/EditorButtons';
import SubEditBottom from 'components/editor/SubEditBottom';
import { CgEditFlipH, CgEditFlipV } from 'react-icons/cg';
import { AiOutlineRotateLeft, AiOutlineRotateRight } from 'react-icons/ai';
import styled from 'styled-components';
import { useState } from 'react';

const ImageEditContainer = ({ editorIns }: { editorIns: any }) => {
  const [isFlipX, setIsFlipX] = useState<boolean>(false);
  const [isFlipY, setIsFlipY] = useState<boolean>(false);

  const handleFlipX = () => {
    if (!editorIns) return;
    editorIns.flipX();
    setIsFlipX(!isFlipX);
  };
  const handleFlipY = () => {
    if (!editorIns) return;
    editorIns.flipY();
    setIsFlipY(!isFlipY);
  };
  const handleRotateRight = () => {
    if (!editorIns) return;
    editorIns.rotate(90);
  };
  const handleRotateLeft = () => {
    if (!editorIns) return;
    editorIns.rotate(-90);
  };
  return (
    <SubEditBottom>
      <CustomButton white p="4" onClick={handleFlipX} checked={isFlipX}>
        <CgEditFlipH />
        flip-x
      </CustomButton>
      <CustomButton white p="4" onClick={handleFlipY} checked={isFlipY}>
        <CgEditFlipV />
        flip-y
      </CustomButton>
      <CustomButton white p="4" onClick={handleRotateRight}>
        <AiOutlineRotateRight />
        90°
      </CustomButton>
      <CustomButton white p="4" onClick={handleRotateLeft}>
        <AiOutlineRotateLeft />
        -90°
      </CustomButton>
    </SubEditBottom>
  );
};

const CustomButton = styled(EditorIconButton)`
  display: flex;
  flex-direction: column;
  font-size: 12px;

  svg {
    font-size: 24px;
    margin-bottom: 4px;
  }
`;

export default ImageEditContainer;
