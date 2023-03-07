import EditorTemplate from 'components/editor/EditorTemplate';
import EditorContainer from 'containers/editor';
import ImageEditorContainer from 'containers/editor/imageEditor';
import { useSearchParams } from 'react-router-dom';

const EditorPage = () => {
  const [searchParams] = useSearchParams();

  const isEdit = searchParams?.get('isEdit');

  return (
    <EditorTemplate>
      {isEdit ? <ImageEditorContainer /> : <EditorContainer />}
    </EditorTemplate>
  );
};

export default EditorPage;
