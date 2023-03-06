import { Renault } from 'data/template/renault';
import { useAppSelector } from 'hooks';
import { EditorTopProps, ImgBlockProps, ItemProps } from 'interface/editor';
import { useEffect, useRef } from 'react';
import { RootState } from 'store';
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
          <ImgBlock key={idx} img={ci} />
        ))}
        <img src={item?.tempSrc} />
      </div>
      {item?.name}
    </>
  );
};

const ImgBlock = ({ img }: ImgBlockProps) => {
  const { imgs } = useAppSelector((state: RootState) => state.images);

  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    imgs.forEach((el) => {
      if (el.id === img.cId && ref.current)
        ref.current.style.background = `url(${el.imgUrl}) no-repeat 50% /cover`;
    });
  }, [imgs]);

  return (
    <div
      className="img_viewer"
      ref={ref}
      style={{
        width: img.w,
        height: img.h,
        top: img.t,
        left: img.l,
      }}
    ></div>
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
    cursor: pointer;

    .top_view_wrap {
      overflow: hidden;
      margin-bottom: 4px;
      position: relative;
      .img_viewer {
        position: absolute;
      }
    }

    &.swiper-slide-thumb-active {
      color: #e64c66;
      .top_view_wrap {
        border: 1px solid #e64c66;
        img {
        }
      }
    }
  }
`;

export default EditorTopList;
