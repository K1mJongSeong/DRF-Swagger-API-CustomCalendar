import EditorBottom from 'components/editor/EditorBottom';
import { useAppDispatch, useAppSelector } from 'hooks';
import client from 'lib/api/client';
import { useNavigate, useParams } from 'react-router';
import { deleteImg, selectId, updateImg } from 'reducer/images';
import { RootState } from 'store';

const EditorBottomSection = ({
  setLoading,
}: {
  setLoading?: React.Dispatch<React.SetStateAction<boolean>>;
}) => {
  const params = useParams();
  const navigate = useNavigate();

  const { nansu } = params;

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
    <EditorBottom
      onChange={handleChangeImage}
      onEdit={handleGotoEdit}
      onDelete={handleDeleteImage}
    />
  );
};

export default EditorBottomSection;
