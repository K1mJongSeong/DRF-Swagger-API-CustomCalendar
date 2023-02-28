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

  const handleChangeSlidePage = (idx: number) => {
    navigate(`${pathname}?temp=${temp}&year=${year}&page=${idx + 1}`);
  };

  useEffect(() => {
    swiperRef.current?.swiper.slideTo((page as unknown as number) - 1, 1000);
  }, []);

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
      />
    </>
  );
};

export default EditorContainer;
