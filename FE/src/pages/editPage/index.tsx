import EditorTemplate from 'components/editor/EditorTemplate';
import EditorContainer from 'containers/editor';
import ImageEditorContainer from 'containers/editor/imageEditor';
import { useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';

const EditorPage = () => {
  const [searchParams] = useSearchParams();

  const isEdit = searchParams?.get('isEdit');

  useEffect(() => {
    console.log(isEdit);
  }, [searchParams]);

  return (
    <EditorTemplate>
      {isEdit ? <ImageEditorContainer /> : <EditorContainer />}
    </EditorTemplate>
  );
};

export default EditorPage;
