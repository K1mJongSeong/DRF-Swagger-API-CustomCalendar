/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable react/prop-types */
import Loading from 'components/common/loading';
import VisibleBackLoading from 'components/common/loading/VisibleBack';
import ImageEditorCom from 'components/editor/ImageEditor';
import { useAppSelector } from 'hooks';
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router';
import { RootState } from 'store';
import EditorBottomSection from '../EditorBottomSection';
import EditorTopSection from '../EditorTopSection';
import CropEditContainer from './CropEditContainer';
import EditorCtrlBtnsContainer from './EditorCtrlBtnsContainer';
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
  /** 작업 배경 이미지 */
  const [img, setImg] = useState('');

  /** loading */
  const [loading, setLoading] = useState<boolean>(false);

  /** editor Ref */
  const editRef = useRef<any>(null);
  /** editor instance */
  const [editorIns, setEditorIns] = useState<any>(null);

  /** selected object */
  /** id */
  const [selectedObjId, setSelectedObjId] = useState<number>(0);
  /** text object */
  const [selectedTxt, setSelectedTxt] = useState<any>(null);

  /** crop edit */
  const [cropEdit, setCropEdit] = useState<boolean>(false);
  /** text edit */
  const [txtEdit, setTxtEdit] = useState<boolean>(false);

  /** undo, redo */
  const [undoSt, setUndoSt] = useState<boolean>(true);
  const [redoSt, setRedoSt] = useState<boolean>(true);
  const [undoStack, setUndoStack] = useState<number>(0);

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
          setLoading(false);
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
    /** undo, redo */
    editorIns.on('undoStackChanged', function (length: number) {
      setUndoStack(length);
    });
  }, [editorIns]);

  /** undo, redo */
  const handleUndo = () => {
    if (!editorIns) return;
    editorIns.undo();
    setUndoStack((prev) => prev - 1);
  };
  const handleRedo = () => {
    if (!editorIns) return;
    editorIns.redo();
  };

  useEffect(() => {
    if (!editorIns) return;
    console.log(undoStack);
    if (undoStack === 1) {
      setUndoSt(true);
      setRedoSt(editorIns.isEmptyRedoStack());
      return;
    }
    setUndoSt(editorIns.isEmptyUndoStack());
    setRedoSt(editorIns.isEmptyRedoStack());
    setRedoSt(editorIns.isEmptyRedoStack());
    console.log(undoSt);
    console.log(redoSt);
  }, [undoStack]);

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
        setSelectedObjId(props.id);
        setTxtEdit(true);
        setSelectedTxt(props);
      })
      .catch((err: Error) => console.error(err));
  };

  return (
    <>
      {loading && <VisibleBackLoading />}
      <EditorTopSection />
      <ImageEditorCom editRef={editRef} />
      <EditorCtrlBtnsContainer
        undoSt={undoSt}
        redoSt={redoSt}
        onUndo={handleUndo}
        onRedo={handleRedo}
      />
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
