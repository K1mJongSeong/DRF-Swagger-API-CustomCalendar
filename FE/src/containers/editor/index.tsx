/* eslint-disable camelcase */
/* eslint-disable prefer-const */
import EditorBottomSection from './EditorBottomSection';
import EditorTopList from 'components/editor/EditorTopList';
import EditorTopSection from './EditorTopSection';
import VisibleBackLoading from 'components/common/loading/VisibleBack';

import { useEffect, useRef, useState } from 'react';
import {
  useLocation,
  useNavigate,
  useParams,
  useSearchParams,
} from 'react-router-dom';

// Import Swiper React components
import { Swiper, SwiperRef, SwiperSlide } from 'swiper/react';
import * as SwiperTypes from 'swiper/types';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/free-mode';
import 'swiper/css/navigation';
import 'swiper/css/thumbs';

// import required modules
import { FreeMode, Navigation, Thumbs } from 'swiper';

// api
import client from 'lib/api/client';
// redux
import { useAppDispatch, useAppSelector } from 'hooks';
import { selectId, selectPageNo, updateImg } from 'reducer/images';
import { RootState } from 'store';
import EditorBodyContainer from './EditorBodyContainer';
import { getHolidays, initialHolidayError } from 'reducer/holidays';
import MemoContainer from './memo/MemoContainer';
import {
  changeMemoField,
  getMemoList,
  initialMemoError,
  initialPostResult,
  updateDate,
} from 'reducer/memo';
import { Renault } from 'data/template/renault';
import {
  initialPageError,
  initialUpdatePageResult,
  updatePrevImgs,
  updatePrevLoading,
  updateSavedPages,
  updateTotalPicArr,
} from 'reducer/page';

const EditorContainer = () => {
  const swiperRef = useRef<SwiperRef>(null);
  const [thumbsSwiper, setThumbsSwiper] = useState<SwiperTypes.Swiper | null>(
    null,
  );
  const [searchParams] = useSearchParams();
  const location = useLocation();
  const navigate = useNavigate();
  const params = useParams();

  const page = searchParams?.get('page');
  const temp = searchParams?.get('temp');
  const year = searchParams?.get('year');
  const { pathname } = location;
  const { nansu } = params;

  // redux
  const dispatch = useAppDispatch();
  const { imgs, selectedId } = useAppSelector(
    (state: RootState) => state.images,
  );
  const {
    selectDate,
    loading: memoLoading,
    error: memoError,
  } = useAppSelector((state: RootState) => state.memo);
  const { error: holidayError } = useAppSelector(
    (state: RootState) => state.holidays,
  );
  const {
    loading: pageLoading,
    getPageResult,
    error: pageError,
  } = useAppSelector((state: RootState) => state.page);

  /** 첫 렌더링 시 공휴일 가져오기 */
  useEffect(() => {
    for (let i = 1; i < 13; i++) {
      const str = i.toString();
      if (str.length === 1) {
        dispatch(getHolidays(`0${str}`));
      } else {
        dispatch(getHolidays(str));
      }
    }
  }, []);

  /** 첫 렌더링 시 메모 가져오기 */
  useEffect(() => {
    if (!nansu) return;
    dispatch(getMemoList(nansu));
  }, [nansu]);

  const [loading, setLoading] = useState<boolean>(false);

  const handleChangeSlidePage = (idx: number) => {
    Renault.forEach((el) => {
      if (el.id === idx + 1) {
        navigate(
          `${pathname}?temp=${temp}&year=${year}&page=${idx + 1}&pageName=${
            el.pageName
          }&ctrlNum=${el.ctrlItems ? el.ctrlItems.length : 0}`,
        );
      }
    });
    dispatch(selectId(null));
    dispatch(selectPageNo(null));
  };

  useEffect(() => {
    swiperRef.current?.swiper.slideTo((page as unknown as number) - 1, 1000);
  }, [page]);

  const [imgArr, setImgArr] = useState<Array<number>>([]);
  useEffect(() => {
    const newArr: Array<number> = [];
    imgs.forEach((i) => {
      newArr.push(i.id);
    });
    setImgArr(newArr);
  }, [imgs]);

  const handleClickImage = (cId: number, pageNo: number) => {
    if (imgArr.includes(cId)) {
      dispatch(selectId(cId));
      dispatch(selectPageNo(pageNo));
    } else {
      dispatch(selectId(null));
      dispatch(selectPageNo(null));
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
        await client
          .post('/Image/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          })
          .then((resp) => {
            dispatch(updateImg({ id: cId, imgUrl: resp.data.image, pageNo }));
          })
          .catch((err: Error) => {
            console.log(err);
            alert(err.message);
            return navigate('/');
          });

        setLoading(false);
      };
    }
  };

  useEffect(() => {
    if (holidayError) {
      console.log(`holidayError: ${holidayError}`);
      dispatch(initialHolidayError());
    }
  }, [holidayError]);

  useEffect(() => {
    if (memoError || pageError) {
      if (memoError) alert(`memoError: ${memoError}`);
      if (pageError) alert(`pageError: ${pageError}`);
      dispatch(initialMemoError());
      dispatch(updateDate(null));
      dispatch(changeMemoField(''));
      dispatch(initialPostResult());
      dispatch(initialPageError());
      dispatch(initialUpdatePageResult());
      return navigate(`/${nansu}/list?temp=${temp}&year=${year}`);
    }
  }, [memoError, pageError]);

  useEffect(() => {
    if (memoLoading || pageLoading) {
      setLoading(true);
    } else {
      setLoading(false);
    }
  }, [memoLoading, pageLoading]);

  useEffect(() => {
    if (!getPageResult) return;
    if (
      getPageResult.data &&
      getPageResult.pageName &&
      getPageResult.total_pic
    ) {
      dispatch(
        updatePrevImgs({
          data: getPageResult.data,
          pageName: getPageResult.pageName,
        }),
      );
      const totalPicArrObj = {
        total_pic: getPageResult.total_pic,
        pageName: getPageResult.pageName,
        pageNo: getPageResult.pageNo,
      };
      dispatch(updateTotalPicArr(totalPicArrObj));
      dispatch(updatePrevLoading(false));
      dispatch(updateSavedPages(getPageResult.pageName));
    }
  }, [getPageResult]);

  return (
    <>
      <EditorTopSection>
        <EditorTopList
          Swiper={Swiper}
          SwiperSlide={SwiperSlide}
          setThumbsSwiper={setThumbsSwiper}
          FreeMode={FreeMode}
          Navigation={Navigation}
          Thumbs={Thumbs}
        />
      </EditorTopSection>
      <EditorBodyContainer
        thumbsSwiper={thumbsSwiper}
        Swiper={Swiper}
        SwiperSlide={SwiperSlide}
        FreeMode={FreeMode}
        Navigation={Navigation}
        Thumbs={Thumbs}
        swiperRef={swiperRef}
        onSwiper={handleChangeSlidePage}
        onClickImage={handleClickImage}
      />
      {selectedId !== null && <EditorBottomSection setLoading={setLoading} />}
      {loading && <VisibleBackLoading />}
      {selectDate && <MemoContainer />}
    </>
  );
};

export default EditorContainer;
