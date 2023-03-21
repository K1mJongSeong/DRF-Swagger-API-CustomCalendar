/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable react/prop-types */
import CropZone from 'components/editor/CropZone';
import ImageEditorCom from 'components/editor/ImageEditor';
import { useAppSelector } from 'hooks';
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router';
import { RootState } from 'store';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';
import CropEditContainer from './CropEditContainer';
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

  /** text edit */
  const [txtEdit, setTxtEdit] = useState<boolean>(false);
  /** crop edit */
  const [cropEdit, setCropEdit] = useState<boolean>(false);

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
    editorIns.startDrawingMode('CROPPER');
    setTxtEdit(false);
    setCropEdit(true);
  };

  const handleSetCropZone = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!editorIns) return;
    const { value } = e.target;

    if (value === 'none') {
      editorIns.setCropzoneRect(0);
    } else if (value === '1') {
      editorIns.setCropzoneRect(1);
    } else if (value === '2') {
      editorIns.setCropzoneRect(1.7777777777777777);
    } else if (value === '3') {
      editorIns.setCropzoneRect(1.5);
    } else if (value === '4') {
      editorIns.setCropzoneRect(1.25);
    }
  };

  const handleApplyCrop = () => {
    if (!editorIns) return;
    const cropZone = editorIns.getCropzoneRect();

    if (!cropZone) return;
    if (cropZone.width <= 1 || cropZone.height <= 1) {
      return;
    }
    editorIns.crop(cropZone);
  };
  const handlecancleCrop = () => {
    if (!editorIns) return;
    editorIns.stopDrawingMode();
    setCropEdit(false);
  };

  /** add text */
  const handleAddTxt = () => {
    if (!editorIns) return;
    editorIns.stopDrawingMode();
    setCropEdit(false);
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
      {cropEdit && (
        <CropEditContainer
          onChange={handleSetCropZone}
          onApply={handleApplyCrop}
          onCancle={handlecancleCrop}
        />
      )}
      {txtEdit && (
        <TextEditContainer
          editorIns={editorIns}
          selectedObjId={selectedObjId}
          selectedTxt={selectedTxt}
          setSelectedTxt={setSelectedTxt}
        />
      )}
      <EditorBottomSection onCrop={handleCrop} addTxt={handleAddTxt} />
    </>
  );
};

export default ImageEditorContainer;
