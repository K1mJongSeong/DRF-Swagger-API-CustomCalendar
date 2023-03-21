/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable react/prop-types */
import VisibleBackLoading from 'components/common/loading/VisibleBack';
import ImageEditorCom from 'components/editor/ImageEditor';
import { useAppSelector } from 'hooks';
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router';
import { RootState } from 'store';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';
import AddLayerContainer from './AddLayerContainer';
import CropEditContainer from './CropEditContainer';
import EditorCtrlBtnsContainer from './EditorCtrlBtnsContainer';
import ImageEditContainer from './ImageEditContainer';
import TextEditContainer from './TextEditContainer';

interface propsType {
  type: string;
  id: number;
}

type dataURLType = string[];

const ImageEditorContainer = () => {
  const navigate = useNavigate();
  const { imgs, selectedId } = useAppSelector(
    (state: RootState) => state.images,
  );
  /** 작업 배경 이미지 */
  const [img, setImg] = useState('');
  const [imgWidth, setImgWidth] = useState<number>(0);

  /** loading */
  const [loading, setLoading] = useState<boolean>(false);

  /** editor Ref */
  const editRef = useRef<any>(null);
  /** editor instance */
  const [editorIns, setEditorIns] = useState<any>(null);

  /** undo, redo */
  const [undoSt, setUndoSt] = useState<boolean>(true);
  const [redoSt, setRedoSt] = useState<boolean>(true);
  const [undoStack, setUndoStack] = useState<number>(0);
  const [redoStack, setRedoStack] = useState<number>(0);

  /** selected object */
  /** isActive */
  const [isActive, setIsActive] = useState<boolean>(false);
  /** id */
  const [selectedObjId, setSelectedObjId] = useState<number>(0);
  /** text object */
  const [selectedTxt, setSelectedTxt] = useState<any>(null);

  /** crop edit */
  const [cropEdit, setCropEdit] = useState<boolean>(false);
  /** image edit */
  const [imgEdit, setImgEdit] = useState<boolean>(false);
  /** text edit */
  const [txtEdit, setTxtEdit] = useState<boolean>(false);
  /** add image layer */
  const [addLayer, setAddLayer] = useState<boolean>(false);

  /** instance 생성 및 배경이미지 */
  useEffect(() => {
    if (imgs.length <= 0) {
      alert('이미지가 존재하지 않습니다.');
      return navigate(-1);
    }
    if (!editRef.current) return;
    const editor = editRef.current?.getInstance();
    setEditorIns(editor);

    imgs.forEach((el) => {
      if (el.id === selectedId) setImg(el.imgUrl);
    });
    setLoading(true);

    setTimeout(() => {
      editor
        .loadImageFromURL(img, 'basic')
        .then((props: any) => {
          console.log(props);
          setImgWidth(props.newWidth);
          setLoading(false);
        })
        .catch((err: Error) => {
          console.error(err);
        });
    }, 1000);
  }, [editRef, img]);

  /** instance 이벤트 */
  useEffect(() => {
    if (!editorIns) return;
    /** selected object */
    editorIns.on('objectActivated', function (props: propsType) {
      setSelectedObjId(props.id);
      setIsActive(false);
      if (props.type === 'i-text') {
        setIsActive(true);
        setSelectedTxt(props);
      } else if (props.type === 'image') {
        setIsActive(true);
        setCropEdit(false);
        setImgEdit(false);
        setTxtEdit(false);
        setAddLayer(true);
      } else {
        setIsActive(false);
      }
    });

    /** text editing */
    editorIns.on('textEditing', function () {
      setCropEdit(false);
      setImgEdit(false);
      setTxtEdit(true);
      setAddLayer(false);
    });
    /** undo, redo */
    editorIns.on('undoStackChanged', function (length: number) {
      setUndoStack(length);
    });
    editorIns.on('redoStackChanged', function (length: number) {
      setRedoStack(length);
    });
  }, [editorIns]);

  /** undo, redo */
  const handleUndo = () => {
    if (!editorIns) return;
    editorIns.undo();
  };
  const handleRedo = () => {
    if (!editorIns) return;
    editorIns.redo();
  };

  useEffect(() => {
    console.log(undoStack, redoStack);
    if (undoStack <= 1) {
      setUndoSt(true);
    } else {
      setUndoSt(false);
    }
    if (redoStack) {
      setRedoSt(false);
    } else {
      setRedoSt(true);
    }
  }, [undoStack, redoStack]);

  /** remove object */
  const handleRemoveObject = () => {
    if (!editorIns) return;
    editorIns.removeActiveObject();
    setIsActive(false);
  };

  /** crop */
  const handleCrop = () => {
    if (!editorIns) return;
    editorIns.startDrawingMode('CROPPER');
    setCropEdit(true);
    setImgEdit(false);
    setTxtEdit(false);
    setAddLayer(false);
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

  /** img */
  const handleImageEdit = () => {
    editorIns.stopDrawingMode();
    setCropEdit(false);
    setImgEdit(true);
    setTxtEdit(false);
    setAddLayer(false);
  };

  /** add text */
  const handleAddTxt = () => {
    if (!editorIns) return;
    editorIns.stopDrawingMode();
    setCropEdit(false);
    setImgEdit(false);
    setAddLayer(false);

    editorIns
      .addText('더블 클릭')
      .then((props: { id: number }) => {
        setSelectedObjId(props.id);
        setTxtEdit(true);
        setSelectedTxt(props);
        editorIns.changeTextStyle(props.id, {
          fontSize: imgWidth / 10,
        });
      })
      .catch((err: Error) => console.error(err));
  };

  /** add iamge layer */
  const handleOpenAddLayer = () => {
    setCropEdit(false);
    setImgEdit(false);
    setTxtEdit(false);
    setAddLayer(!addLayer);
  };

  /** submit custom Image with Editor */
  const handleSubmitEditor = () => {
    if (!editorIns) return;
    console.log(editorIns.toDataURL());
    const dataUrl = editorIns.toDataURL();
    const file = dataURLtoFile(dataUrl, 'customImage.png');
    console.log(file);
  };
  // dataURL to file
  const dataURLtoFile = (dataurl: any, fileName: string) => {
    if (!dataurl) return;
    const arr = dataurl.split(',');
    const mime = arr[0].match(/:(.*?);/)[1];
    const bstr = atob(arr[1]);
    let n = bstr.length,
      u8arr = new Uint8Array(n);

    while (n--) {
      u8arr[n] = bstr.charCodeAt(n);
    }

    return new File([u8arr], fileName, { type: mime });
  };

  return (
    <>
      {loading && <VisibleBackLoading />}
      <EditorTopSection onSubmit={handleSubmitEditor} />
      <ImageEditorCom editRef={editRef} />
      <EditorCtrlBtnsContainer
        undoSt={undoSt}
        redoSt={redoSt}
        onUndo={handleUndo}
        onRedo={handleRedo}
        isActive={isActive}
        onRemove={handleRemoveObject}
      />
      {cropEdit && (
        <CropEditContainer
          onChange={handleSetCropZone}
          onApply={handleApplyCrop}
          onCancle={handlecancleCrop}
        />
      )}
      {imgEdit && <ImageEditContainer editorIns={editorIns} />}
      {txtEdit && (
        <TextEditContainer
          editorIns={editorIns}
          selectedObjId={selectedObjId}
          selectedTxt={selectedTxt}
          setSelectedTxt={setSelectedTxt}
        />
      )}
      {addLayer && <AddLayerContainer editorIns={editorIns} />}
      <EditorBottomSection
        onCrop={handleCrop}
        onImg={handleImageEdit}
        addTxt={handleAddTxt}
        addLayer={handleOpenAddLayer}
      />
    </>
  );
};

export default ImageEditorContainer;
