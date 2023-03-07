import ImageEditorCom from 'components/editor/ImageEditor';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';

const ImageEditorContainer = () => {
  return (
    <>
      <EditorTopSection />
      <ImageEditorCom />
      <EditorBottomSection />
    </>
  );
};

export default ImageEditorContainer;
