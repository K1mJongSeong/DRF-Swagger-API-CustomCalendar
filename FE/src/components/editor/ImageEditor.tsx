import styled from 'styled-components';
import 'tui-image-editor/dist/tui-image-editor.css';
import ImageEditor from '@toast-ui/react-image-editor';

const editorOption = {
  cssMaxWidth: 700,
  cssMaxHeight: 500,
  selectionStyle: {
    cornerSize: 20,
    rotatingPointOffset: 70,
  },
};
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
  & > div {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
`;

export default ImageEditorCom;
