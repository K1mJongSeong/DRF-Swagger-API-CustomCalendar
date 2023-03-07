import ImageEditorCom from 'components/editor/ImageEditor';
import { useEffect, useRef } from 'react';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';

const ImageEditorContainer = () => {
  const editRef = useRef<any>(null);

  useEffect(() => {
    if (!editRef.current) return;
    const editor = editRef.current?.getInstance();
    setTimeout(() => {
      editor
        .addImageObject('/assets/images/logo.png')
        .then((objectProps: any) => {
          console.log(objectProps);
        });
    }, 100);
  }, [editRef]);

  return (
    <>
      <EditorTopSection />
      <ImageEditorCom editRef={editRef} />
      <EditorBottomSection />
    </>
  );
};

export default ImageEditorContainer;
