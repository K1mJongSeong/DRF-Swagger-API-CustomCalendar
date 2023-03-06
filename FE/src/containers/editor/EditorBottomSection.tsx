import EditorBottom from 'components/editor/EditorBottom';
import { useAppDispatch, useAppSelector } from 'hooks';
import client from 'lib/api/client';
import { updateImg } from 'reducer/images';
import { RootState } from 'store';

const EditorBottomSection = () => {
  const { selectedId } = useAppSelector((state: RootState) => state.images);
  const dispatch = useAppDispatch();

  const handleChangeImage = () => {
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', '.jpg, .png');
    input.click();

    input.onchange = async () => {
      const files = input.files;
      const formData = new FormData();

      if (!files) return;
      formData.append('image', files[0]);
      const res = await client.post('/Image/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (!selectedId) return;
      dispatch(updateImg({ id: selectedId, imgUrl: res.data.image }));
    };
  };
  return <EditorBottom change={handleChangeImage} />;
};

export default EditorBottomSection;
