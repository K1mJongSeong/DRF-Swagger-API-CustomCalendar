import EditorConWrap from 'components/editor/EditorConWrap';
import { useEffect, useRef, useState } from 'react';
import EditorTopList from 'components/editor/EditorTopList';
import EditorTopSection from './EditorTopSection';
import { useLocation, useNavigate, useSearchParams } from 'react-router-dom';

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
import { selectId, updateImg } from 'reducer/images';
import { RootState } from 'store';
import EditorBottom from 'components/editor/EditorBottom';

const EditorContainer = () => {
  const swiperRef = useRef<SwiperRef>(null);
  const [thumbsSwiper, setThumbsSwiper] = useState<SwiperTypes.Swiper | null>(
    null,
  );
  const [searchParams] = useSearchParams();
  const location = useLocation();
  const navigate = useNavigate();

  const page = searchParams?.get('page');
  const temp = searchParams?.get('temp');
  const year = searchParams?.get('year');
  const { pathname } = location;

  // redux
  const dispatch = useAppDispatch();
  const { imgs, selectedId } = useAppSelector(
    (state: RootState) => state.images,
  );

  const handleChangeSlidePage = (idx: number) => {
    navigate(`${pathname}?temp=${temp}&year=${year}&page=${idx + 1}`);
  };

  useEffect(() => {
    swiperRef.current?.swiper.slideTo((page as unknown as number) - 1, 1000);
  }, [page]);

  const [imgArr, setImgArr] = useState<Array<number>>([]);
  useEffect(() => {
    imgs.forEach((i) => {
      if (imgArr.includes(i.id)) return;
      setImgArr([...imgArr, i.id]);
    });
  }, [imgs]);

  const handleClickImage = (cId: number) => {
    if (imgArr.includes(cId)) {
      dispatch(selectId(cId));
    } else {
      dispatch(selectId(null));
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

        dispatch(updateImg({ id: cId, imgUrl: res.data.image }));
      };
    }
  };

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
      <EditorConWrap
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
      {selectedId && <EditorBottom />}
    </>
  );
};

export default EditorContainer;
