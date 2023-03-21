/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable react/prop-types */
import ImageEditorCom from 'components/editor/ImageEditor';
import { useAppSelector } from 'hooks';
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router';
import { RootState } from 'store';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';
import TextEditContainer from './TextEditContainer';

interface propsType {
  type: string;
  id: number;
}

const ImageEditorContainer = () => {
  const navigate = useNavigate();
  const { imgs, selectedId } = useAppSelector(
    (state: RootState) => state.images,
  );
  /** 작업 이미지 */
  const [img, setImg] = useState('');

  /** editor Ref */
  const editRef = useRef<any>(null);
  /** editor instance */
  const [editorIns, setEditorIns] = useState<any>(null);

  /** selected object */
  /** id */
  const [selectedObjId, setSelectedObjId] = useState<number>(0);
  /** text object */
  const [selectedTxt, setSelectedTxt] = useState<any>(null);
  console.log(selectedTxt);

  /** text edit */
  const [txtEdit, setTxtEdit] = useState<boolean>(false);

  useEffect(() => {
    if (imgs.length <= 0) {
      alert('이미지가 존재하지 않습니다.');
      return navigate(-1);
    }
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
  }, [editRef, img]);

  useEffect(() => {
    if (!editorIns) return;
    /** selected object */
    editorIns.on('objectActivated', function (props: propsType) {
      setSelectedObjId(props.id);
      if (props.type === 'i-text') {
        setSelectedTxt(props);
      }
    });

    /** text editing */
    editorIns.on('textEditing', function () {
      setTxtEdit(true);
    });
  }, [editorIns]);

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
        setSelectedObjId(props.id);
        setTxtEdit(true);
        setSelectedTxt(props);
      })
      .catch((err: Error) => console.error(err));
  };

  return (
    <>
      <EditorTopSection />
      <ImageEditorCom editRef={editRef} />
      {txtEdit && (
        <TextEditContainer
          editorIns={editorIns}
          selectedObjId={selectedObjId}
        />
      )}
      <EditorBottomSection onCrop={handleCrop} addTxt={handleAddTxt} />
    </>
  );
};

export default ImageEditorContainer;
