import EditorTemplate from 'components/editor/EditorTemplate';
import EditorContainer from 'containers/editor';
import ImageEditorContainer from 'containers/editor/imageEditor';
import { Renault } from 'data/template/renault';
import { useAppDispatch } from 'hooks';
import { useEffect } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import { getPage, updatePrevLoading } from 'reducer/page';

const EditorPage = () => {
  const dispatch = useAppDispatch();
  const { nansu } = useParams();
  const [searchParams] = useSearchParams();

  const isEdit = searchParams?.get('isEdit');
  /** 첫 렌더링 시 작업리스트 가져오기 */
  useEffect(() => {
    if (!nansu) return;
    dispatch(updatePrevLoading(true));
    Renault.forEach((el) => {
      if (!el.pageName) return;
      dispatch(getPage({ pageName: el.pageName, nansu }));
    });
  }, []);

  return (
    <EditorTemplate>
      {isEdit ? <ImageEditorContainer /> : <EditorContainer />}
    </EditorTemplate>
  );
};

export default EditorPage;
