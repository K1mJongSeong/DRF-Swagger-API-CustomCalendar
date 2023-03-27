import { EditorTextButton } from 'components/editor/EditorButtons';
import EditorTop from 'components/editor/EditorTop';
import { useNavigate, useParams } from 'react-router';
import { BsCartPlus } from 'react-icons/bs';
import { MdArrowBackIos } from 'react-icons/md';
import { useSearchParams } from 'react-router-dom';

const EditorTopSection = ({
  children,
  onSubmit,
}: {
  children?: React.ReactNode;
  onSubmit?: () => void;
}) => {
  const navigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();

  const { nansu } = params;
  const isEdit = searchParams?.get('isEdit');
  const temp = searchParams?.get('temp');
  const year = searchParams?.get('year');
  const page = searchParams?.get('page');
  const pageName = searchParams?.get('pageName');

  const handleClickBackBtn = () => {
    if (isEdit) return navigate(-1);

    navigate(`/${nansu}/list?temp=${temp}&year=${year}`);
  };

  const handlePostPageClick = () => {
    alert(
      `템플릿 이름: ${temp}, 선택 년도: ${year}, 저장 페이지: ${page}, 페이지이름: ${pageName}`,
    );
  };

  const handleGotoOrder = () => {
    navigate(`/${nansu}/order`);
  };

  return (
    <EditorTop>
      {isEdit ? (
        <>
          <EditorTextButton white onClick={handleClickBackBtn}>
            취소
          </EditorTextButton>
          <EditorTextButton red onClick={onSubmit}>
            적용
          </EditorTextButton>
        </>
      ) : (
        <>
          <EditorTextButton white onClick={handleClickBackBtn}>
            <MdArrowBackIos />
          </EditorTextButton>
          <div className="right">
            <EditorTextButton red onClick={handlePostPageClick}>
              저장
            </EditorTextButton>
            <EditorTextButton white onClick={handleGotoOrder}>
              <BsCartPlus />
            </EditorTextButton>
          </div>
        </>
      )}
      {children}
    </EditorTop>
  );
};

export default EditorTopSection;
