import EditorConWrap, { EditorItem } from 'components/editor/EditorConWrap';
import { Renault } from 'data/template/renault';
import { EditorConProps } from 'interface/editor';

const EditorBodyContainer = (props: EditorConProps) => {
  const {
    Swiper,
    SwiperSlide,
    thumbsSwiper,
    FreeMode,
    Navigation,
    Thumbs,
    swiperRef,
    onSwiper,
    onClickImage,
  } = props;

  return (
    <EditorConWrap>
      <Swiper
        ref={swiperRef}
        spaceBetween={10}
        navigation={true}
        thumbs={{ swiper: thumbsSwiper }}
        modules={[FreeMode, Navigation, Thumbs]}
        className="mySwiper2"
        onSlideChange={(i) => onSwiper(i.activeIndex)}
      >
        {Renault?.map((item) => (
          <SwiperSlide key={item?.id}>
            <EditorItem item={item} onClick={onClickImage} />
          </SwiperSlide>
        ))}
      </Swiper>
    </EditorConWrap>
  );
};

export default EditorBodyContainer;
