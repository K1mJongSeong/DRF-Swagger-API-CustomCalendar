import { EditorTextButton } from 'components/editor/EditorButtons';
import EditorTop from 'components/editor/EditorTop';
import { useNavigate, useParams } from 'react-router';
import { BsCartPlus } from 'react-icons/bs';
import { MdArrowBackIos } from 'react-icons/md';
import { useSearchParams } from 'react-router-dom';

const EditorTopSection = ({ children }: { children: React.ReactNode }) => {
  const nevigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();

  const { nansu } = params;
  const isEdit = searchParams?.get('isEdit');
  const temp = searchParams?.get('temp');
  const year = searchParams?.get('year');
  const page = searchParams?.get('page');

  const handleClickBackBtn = () => {
    if (isEdit) return nevigate(-1);

    nevigate(`/${nansu}/list?temp=${temp}&year=${year}`);
  };

  const handleTestClick = () => {
    alert(`템플릿 이름: ${temp}, 선택 년도: ${year}, 저장 페이지: ${page}`);
  };

  return (
    <EditorTop>
      <EditorTextButton white onClick={handleClickBackBtn}>
        <MdArrowBackIos />
      </EditorTextButton>
      <div className="right">
        <EditorTextButton red onClick={handleTestClick}>
          저장
        </EditorTextButton>
        <EditorTextButton white>
          <BsCartPlus />
        </EditorTextButton>
      </div>
      {children}
    </EditorTop>
  );
};

export default EditorTopSection;
