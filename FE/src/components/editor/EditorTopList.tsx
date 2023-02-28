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

interface itemProps {
  item: {
    id: number;
    tempSrc: string;
    name: string;
    ctrlItems?: Array<{
      cId: number;
      w: string;
      h: string;
      l: string;
      t?: string;
    }>;
  };
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

const EditorTopItem = ({ item }: itemProps) => {
  return (
    <>
      <div className="top_view_wrap">
        {item.ctrlItems?.map((ci, idx) => (
          <div
            key={idx}
            className="img_viewer"
            style={{
              width: ci.w,
              height: ci.h,
              top: ci.t,
              left: ci.l,
            }}
          ></div>
        ))}
        <img src={item?.tempSrc} />
      </div>
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

    .top_view_wrap {
      margin-bottom: 4px;
      position: relative;
      .img_viewer {
        position: absolute;
      }
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
