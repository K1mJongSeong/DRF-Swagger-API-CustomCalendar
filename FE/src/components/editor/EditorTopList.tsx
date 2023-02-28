import { Renault } from 'data/template/renault';
import { EditorTopProps, ItemProps } from 'interface/editor';
import styled from 'styled-components';

const EditorTopList = (props: EditorTopProps) => {
  const { Swiper, SwiperSlide, setThumbsSwiper, FreeMode, Navigation, Thumbs } =
    props;

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

const EditorTopItem = ({ item }: ItemProps) => {
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
