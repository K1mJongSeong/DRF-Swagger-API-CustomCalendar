import styled from 'styled-components';
import ImageEditor from '@toast-ui/react-image-editor';

const ImageEditorCom = () => (
  <ImageEditorBlock>
    <ImageEditor cssMaxHeight={500} cssMaxWidth={500} usageStatistics={false} />
  </ImageEditorBlock>
);

const ImageEditorBlock = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export default ImageEditorCom;
