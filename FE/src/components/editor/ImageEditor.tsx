import styled from 'styled-components';
import ImageEditor from '@toast-ui/react-image-editor';

const editorOption = {};

const ImageEditorCom = ({
  editRef,
}: {
  editRef: React.MutableRefObject<any>;
}) => {
  return (
    <ImageEditorBlock>
      <ImageEditor ref={editRef} {...editorOption} />
    </ImageEditorBlock>
  );
};

const ImageEditorBlock = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export default ImageEditorCom;
