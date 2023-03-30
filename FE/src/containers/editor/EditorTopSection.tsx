/* eslint-disable prefer-const */
import { EditorTextButton } from 'components/editor/EditorButtons';
import EditorTop from 'components/editor/EditorTop';
import { useNavigate, useParams } from 'react-router';
import { BsCartPlus } from 'react-icons/bs';
import { MdArrowBackIos } from 'react-icons/md';
import { useSearchParams } from 'react-router-dom';
import { useAppDispatch, useAppSelector } from 'hooks';
import { RootState } from 'store';
import {
  initialUpdatePageResult,
  postPage,
  updatePage,
  updateSavedPages,
} from 'reducer/page';
import { useEffect, useState } from 'react';
import ConfirmPageModal from 'components/editor/ConfirmPageModal';
import { initialPostResult } from 'reducer/memo';

const EditorTopSection = ({
  children,
  onSubmit,
}: {
  children?: React.ReactNode;
  onSubmit?: () => void;
}) => {
  const dispatch = useAppDispatch();
  const { imgs } = useAppSelector((state: RootState) => state.images);
  const { postPageResult, savedPages, updatePageResult } = useAppSelector(
    (state) => state.page,
  );

  const navigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();

  const { nansu } = params;
  const isEdit = searchParams?.get('isEdit');
  const temp = searchParams?.get('temp');
  const year = searchParams?.get('year');
  const page = searchParams?.get('page');
  const pageName = searchParams?.get('pageName');

  const [modalOpen, setModalOpen] = useState<boolean>(false);

  const handleClickBackBtn = () => {
    if (isEdit) return navigate(-1);

    navigate(`/${nansu}/list?temp=${temp}&year=${year}`);
  };

  const handlePostModalOpen = () => {
    setModalOpen(true);
  };

  const handlePostModalClose = () => {
    setModalOpen(false);
  };

  const handlePostPage = () => {
    if (!pageName || !nansu) return;
    const ctrlNum = searchParams?.get('ctrlNum');
    if (!ctrlNum) return;

    let newArr: Array<string> = [];
    imgs.forEach((el) => {
      if (el.pageNo.toString() === page) {
        newArr.push(el.imgUrl);
      }
    });
    if (newArr.length < parseInt(ctrlNum)) return alert('이미지를 넣어주세요');
    const newArrToStr = newArr.join();
    if (savedPages.includes(pageName)) {
      dispatch(
        updatePage({ pageName, pagePayload: { pic: newArrToStr, nansu } }),
      );
    } else {
      dispatch(
        postPage({ pageName, pagePayload: { pic: newArrToStr, nansu } }),
      );
    }
  };

  const handleGotoOrder = () => {
    navigate(`/${nansu}/order`);
  };

  useEffect(() => {
    if (postPageResult) {
      setModalOpen(false);
      dispatch(updateSavedPages(postPageResult.pageName));
      dispatch(initialPostResult());
    }
    if (updatePageResult) {
      setModalOpen(false);
      dispatch(updateSavedPages(updatePageResult.pageName));
      dispatch(initialUpdatePageResult());
    }
  }, [postPageResult, updatePageResult]);

  return (
    <>
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
              <EditorTextButton red onClick={handlePostModalOpen}>
                저장
              </EditorTextButton>
              {imgs?.length > 28 && (
                <EditorTextButton white onClick={handleGotoOrder}>
                  <BsCartPlus />
                </EditorTextButton>
              )}
            </div>
          </>
        )}
        {children}
      </EditorTop>
      {modalOpen && (
        <ConfirmPageModal
          close={handlePostModalClose}
          submit={handlePostPage}
          page={page}
        />
      )}
    </>
  );
};

export default EditorTopSection;
