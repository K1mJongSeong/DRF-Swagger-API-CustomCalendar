import { Renault } from 'data/template/renault';
import styled from 'styled-components';
import { SwiperProps, SwiperRef, SwiperSlideProps } from 'swiper/react';
import { Swiper, SwiperModule } from 'swiper/types';

interface EditorConProps {
  Swiper: React.FunctionComponent<React.RefAttributes<SwiperRef> & SwiperProps>;
  SwiperSlide: React.FunctionComponent<SwiperSlideProps>;
  setThumbsSwiper?: (swiper: Swiper) => void;
  FreeMode: SwiperModule;
  Navigation: SwiperModule;
  Thumbs: SwiperModule;
}

const EditorTopList = ({
  Swiper,
  SwiperSlide,
  setThumbsSwiper,
  FreeMode,
  Navigation,
  Thumbs,
}: EditorConProps) => {
  return (
    <EditorTopListBlock>
      <Swiper
        onSwiper={setThumbsSwiper}
        spaceBetween={28}
        slidesPerView={3}
        freeMode={true}
        watchSlidesProgress={true}
        modules={[FreeMode, Navigation, Thumbs]}
        className="mySwiper"
        breakpoints={{
          470: {
            slidesPerView: 4,
          },
          690: {
            slidesPerView: 5,
          },
          800: {
            slidesPerView: 9,
          },
        }}
      >
        <>
          {Renault?.map((item) => (
            <SwiperSlide key={item?.id}>
              <EditorTopItem item={item} />
            </SwiperSlide>
          ))}
        </>
      </Swiper>
    </EditorTopListBlock>
  );
};

const EditorTopItem = ({
  item,
}: {
  item: { id: number; tempSrc: string; name: string };
}) => {
  return (
    <>
      <img src={item?.tempSrc} />
      {item?.name}
    </>
  );
};

const EditorTopListBlock = styled.div`
  width: 100%;
  position: absolute;
  top: calc(100% + 1px);
  left: 0;
  padding: 9px 12px;
  background-color: black;
  color: white;
  .swiper-slide {
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: all 0.2s;
    font-size: 12px;
    img {
      margin-bottom: 4px;
    }

    &.swiper-slide-thumb-active {
      color: #e64c66;
      img {
        border: 1px solid #e64c66;
      }
    }
  }
`;

export default EditorTopList;
