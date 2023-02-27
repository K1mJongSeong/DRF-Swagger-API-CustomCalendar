import { Renault } from 'data/template/renault';
import styled from 'styled-components';
import { SwiperProps, SwiperRef, SwiperSlideProps } from 'swiper/react';
import { Swiper, SwiperModule } from 'swiper/types';

interface EditorConProps {
  Swiper: React.FunctionComponent<React.RefAttributes<SwiperRef> & SwiperProps>;
  SwiperSlide: React.FunctionComponent<SwiperSlideProps>;
  thumbsSwiper?: Swiper | null;
  FreeMode: SwiperModule;
  Navigation: SwiperModule;
  Thumbs: SwiperModule;
}

const EditorConWrap = ({
  Swiper,
  SwiperSlide,
  thumbsSwiper,
  FreeMode,
  Navigation,
  Thumbs,
}: EditorConProps) => {
  return (
    <EditorConWrapBlock>
      <Swiper
        spaceBetween={10}
        navigation={true}
        thumbs={{ swiper: thumbsSwiper }}
        modules={[FreeMode, Navigation, Thumbs]}
        className="mySwiper2"
      >
        {Renault?.map((item) => (
          <SwiperSlide key={item?.id}>
            <EditorItem item={item} />
          </SwiperSlide>
        ))}
      </Swiper>
    </EditorConWrapBlock>
  );
};

const EditorItem = ({
  item,
}: {
  item: { id: number; tempSrc: string; name: string };
}) => {
  return <img src={item?.tempSrc} />;
};

const EditorConWrapBlock = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  .swiper-slide {
    display: flex;
    align-content: center;
    justify-content: center;
    img {
      width: calc(100% - 32px);
      max-width: 500px;
    }
  }
`;

export default EditorConWrap;
