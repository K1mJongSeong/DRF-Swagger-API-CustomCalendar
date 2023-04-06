/* eslint-disable camelcase */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable prefer-const */
import { EditorTextButton } from 'components/editor/EditorButtons';
import EditorTop from 'components/editor/EditorTop';
import { useLocation, useNavigate, useParams } from 'react-router';
import { BsCartPlus } from 'react-icons/bs';
import { MdArrowBackIos } from 'react-icons/md';
import { useSearchParams } from 'react-router-dom';
import { useAppDispatch, useAppSelector } from 'hooks';
import { RootState } from 'store';
import {
  getPage,
  initialPostPageResult,
  initialUpdatePageResult,
  postPage,
  updatePage,
  updateSavedPages,
  updateTotalPicArr,
} from 'reducer/page';
import { useEffect, useState } from 'react';
import ConfirmPageModal from 'components/editor/ConfirmPageModal';
import { getMemoList } from 'reducer/memo';
import { Renault } from 'data/template/renault';
import { initialImgs, selectId, selectPageNo } from 'reducer/images';
import GetPageImg from 'utils/getPageImg';
import WorkingLoading from 'components/common/loading/Working';

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

  const getPageImg = new GetPageImg();

  const navigate = useNavigate();
  const { pathname } = useLocation();
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

  // page API modal open
  const handlePostModalOpen = () => {
    dispatch(selectId(null));
    dispatch(selectPageNo(null));
    setModalOpen(true);
  };

  // page API modal close
  const handlePostModalClose = () => {
    setModalOpen(false);
  };

  const [totalPicLoading, setTotalPicLoading] = useState<boolean>(false);
  // page API submit
  const handlePostPage = async () => {
    if (!pageName || !nansu || !page) return;
    const ctrlNum = searchParams?.get('ctrlNum');
    if (!ctrlNum) return;
    let newArr: Array<string> = [];
    imgs.forEach((el) => {
      if (el.pageNo.toString() === page) {
        newArr.push(el.imgUrl);
      }
    });
    if (newArr.length < parseInt(ctrlNum, 10))
      return alert('이미지를 넣어주세요');
    // make total_pic
    setTotalPicLoading(true);
    getPageImg.resizingItem(pageName, 'lg');
    const totalImg: string = await getPageImg.getTotalPage(pageName, nansu);
    console.log(totalImg);
    getPageImg.resizingItem(pageName, 'sm');
    // prev work
    const getRes = await dispatch(
      getPage({ pageName, nansu, pageNo: parseInt(page, 10) }),
    );
    const prevWorks = getRes.payload.data;
    //
    setTotalPicLoading(false);
    if (!totalImg) {
      alert('이미지 저장 실패');
      return false;
    }
    // update, post PAGE
    const newArrToStr: string = newArr.join().split(' ').join();
    if (!newArrToStr) return;
    const body = { pic: newArrToStr, nansu, total_pic: totalImg };
    const pageNo = page ? parseInt(page, 10) : 0;
    if (savedPages.includes(pageName) || prevWorks) {
      dispatch(
        updatePage({
          pageName,
          pagePayload: body,
          pageNo,
        }),
      );
      return;
    }
    dispatch(
      postPage({
        pageName: pageName,
        pagePayload: body,
        pageNo,
      }),
    );
  };

  const handleChangePage = () => {
    if (page && parseInt(page, 10) < Renault.length) {
      Renault.forEach((el) => {
        if (el.id + 1 === parseInt(page, 10) + 1) {
          return navigate(
            `${pathname}?temp=${temp}&year=${year}&page=${el.id + 1}&pageName=${
              el.pageName
            }&ctrlNum=${el.ctrlItems ? el.ctrlItems.length : 0}`,
          );
        }
      });
    }
  };
  const handleInitImgs = () => {
    if (!nansu) return;
    dispatch(initialImgs());
    Renault.forEach((el) => {
      if (!el.pageName) return;
      dispatch(getPage({ pageName: el.pageName, nansu, pageNo: el.id }));
    });
    dispatch(getMemoList(nansu));
  };

  // POST, UPDATE result 처리
  useEffect(() => {
    if (postPageResult || updatePageResult) {
      handleInitImgs();
    }
    if (postPageResult) {
      setModalOpen(false);
      dispatch(updateSavedPages(postPageResult.pageName));
      const totalPicArrObj = {
        total_pic: postPageResult.result.total_pic,
        pageName: postPageResult.pageName,
        pageNo: postPageResult.pageNo,
      };
      dispatch(updateTotalPicArr(totalPicArrObj));
      dispatch(initialPostPageResult());
      handleChangePage();
    }
    if (updatePageResult) {
      setModalOpen(false);
      dispatch(updateSavedPages(updatePageResult.pageName));
      const totalPicArrObj = {
        total_pic: updatePageResult.result.total_pic,
        pageName: updatePageResult.pageName,
        pageNo: updatePageResult.pageNo,
      };
      dispatch(updateTotalPicArr(totalPicArrObj));
      dispatch(initialUpdatePageResult());
      handleChangePage();
    }
  }, [postPageResult, updatePageResult]);

  const handleGotoOrder = () => {
    navigate(`/${nansu}/order`);
  };

  const count = Renault.length - 1;

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
              {page !== '1' && (
                <EditorTextButton red onClick={handlePostModalOpen}>
                  저장
                </EditorTextButton>
              )}
              {savedPages?.length >= count && (
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
      {totalPicLoading && <WorkingLoading />}
    </>
  );
};

export default EditorTopSection;
