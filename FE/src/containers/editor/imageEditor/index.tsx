/* eslint-disable react/prop-types */
import ImageEditorCom from 'components/editor/ImageEditor';
import { useAppSelector } from 'hooks';
import { useEffect, useRef, useState } from 'react';
import { RootState } from 'store';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';

interface propsType {
  type: string;
  id: number;
}

const ImageEditorContainer = () => {
  const { imgs, selectedId } = useAppSelector(
    (state: RootState) => state.images,
  );
  const editRef = useRef<any>(null);
  const [img, setImg] = useState('');
  const [editorIns, setEditorIns] = useState<any>(null);

  const [selectedObjId, setSelectedObjId] = useState<number>(0);

  /** text edit */
  const [txtEdit, setTxtEdit] = useState<boolean>(false);

  useEffect(() => {
    if (!editRef.current && !img) return;
    const editor = editRef.current?.getInstance();
    setEditorIns(editor);

    imgs.forEach((el) => {
      if (el.id === selectedId) setImg(el.imgUrl);
    });

    setTimeout(() => {
      editor
        .loadImageFromURL(img, 'basic')
        .then((objectProps: any) => {
          console.info(objectProps);
        })
        .catch((err: Error) => {
          console.error(err);
        });
    }, 1000);

    /** selected object */
    editor.on('objectActivated', function (props: propsType) {
      console.log(props);
      setSelectedObjId(selectedObjId);
    });

    /** text editing */
    editor.on('textEditing', function () {
      console.log('텍스트 시작!');
      setTxtEdit(true);
    });
  }, [editRef, img]);

  /** crop */
  const handleCrop = () => {
    if (!editorIns) return;
  };

  /** add text */
  const handleAddTxt = () => {
    if (!editorIns) return;
    editorIns
      .addText('더블 클릭')
      .then((props: { id: number }) => {
        console.log(props);
      })
      .catch((err: Error) => console.error(err));
  };

  return (
    <>
      <EditorTopSection />
      <ImageEditorCom editRef={editRef} />
      <EditorBottomSection onCrop={handleCrop} addTxt={handleAddTxt} />
    </>
  );
};

export default ImageEditorContainer;
