import EditorBottom from 'components/editor/EditorBottom';
import {
  EditorIconButton,
  EditorTextButton,
} from 'components/editor/EditorButtons';
import { useAppDispatch, useAppSelector } from 'hooks';
import client from 'lib/api/client';
import { useNavigate, useParams } from 'react-router';
import { useSearchParams } from 'react-router-dom';
import { deleteImg, selectId, updateImg } from 'reducer/images';
import { RootState } from 'store';
import { IoCropSharp } from 'react-icons/io5';
import { RxText } from 'react-icons/rx';
import { SlLayers } from 'react-icons/sl';

const EditorBottomSection = ({
  setLoading,
  onCrop,
  addTxt,
}: {
  setLoading?: React.Dispatch<React.SetStateAction<boolean>>;
  onCrop?: () => void;
  addTxt?: () => void;
}) => {
  const params = useParams();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  const { nansu } = params;

  const isEdit = searchParams?.get('isEdit');

  const { selectedId } = useAppSelector((state: RootState) => state.images);
  const dispatch = useAppDispatch();

  const handleChangeImage = () => {
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', '.jpg, .png');
    input.click();

    input.onchange = async () => {
      if (!setLoading) return;
      const files = input.files;
      const formData = new FormData();
      setLoading(true);

      if (!files) return;
      formData.append('image', files[0]);
      const res = await client.post('/Image/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(selectedId);
      if (selectedId === null) return;
      dispatch(updateImg({ id: selectedId, imgUrl: res.data.image }));
      setLoading(false);
    };
  };

  const handleGotoEdit = () => {
    navigate(`/${nansu}/editor?isEdit=true`);
  };

  const handleDeleteImage = () => {
    console.log(selectedId);
    dispatch(deleteImg({ selectedId }));
    dispatch(selectId(null));
  };

  return (
    <EditorBottom>
      {isEdit ? (
        <>
          <EditorIconButton white fs="20" onClick={onCrop}>
            <IoCropSharp />
          </EditorIconButton>
          <EditorIconButton white fs="22" onClick={addTxt}>
            <RxText />
          </EditorIconButton>
          <EditorIconButton white fs="20">
            <SlLayers />
          </EditorIconButton>
        </>
      ) : (
        <>
          <EditorTextButton white onClick={handleChangeImage}>
            사진변경
          </EditorTextButton>
          <EditorTextButton white onClick={handleGotoEdit}>
            편집
          </EditorTextButton>
          <EditorTextButton white onClick={handleDeleteImage}>
            삭제
          </EditorTextButton>
        </>
      )}
    </EditorBottom>
  );
};

export default EditorBottomSection;
