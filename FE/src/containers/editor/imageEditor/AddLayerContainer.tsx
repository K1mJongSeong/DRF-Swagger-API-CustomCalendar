/* eslint-disable @typescript-eslint/no-explicit-any */
import VisibleBackLoading from 'components/common/loading/VisibleBack';
import { EditorIconButton } from 'components/editor/EditorButtons';
import SubEditBottom from 'components/editor/SubEditBottom';
import client from 'lib/api/client';
import { useState } from 'react';
import { RiImageAddFill } from 'react-icons/ri';
import styled from 'styled-components';

const AddLayerContainer = ({ editorIns }: { editorIns: any }) => {
  const [loading, setLoading] = useState<boolean>(false);
  const handleAddImageLayer = () => {
    if (!editorIns) return;
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', '.jpg, .png');
    input.click();

    input.onchange = async () => {
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
      console.log(res.data.image);
      editorIns
        .addImageObject(res.data.image)
        .then((props: any) => console.log(props));
      setLoading(false);
    };
  };
  return (
    <>
      {loading && <VisibleBackLoading />}
      <SubEditBottom>
        <CustomButton white onClick={handleAddImageLayer}>
          <RiImageAddFill />
          레이어 추가
        </CustomButton>
      </SubEditBottom>
    </>
  );
};
const CustomButton = styled(EditorIconButton)`
  display: flex;
  flex-direction: column;
  font-size: 12px;

  svg {
    font-size: 24px;
    margin-bottom: 4px;
  }
`;
export default AddLayerContainer;
