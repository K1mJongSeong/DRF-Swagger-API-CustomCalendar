/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
import EditorConWrap from 'components/editor/EditorConWrap';
import { Renault } from 'data/template/renault';
import { addMonths, format } from 'date-fns';
import { EditorConProps } from 'interface/editor';
import EditorItemContainer from './EditorItemContainer';

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

  let currentDate = new Date();
  let selectedDate = new Date();

  let currentMonth = new Date(format(currentDate, 'yyyy'));
  let months: any[] = [];
  months.push(currentMonth);
  for (let i = 0; i < 11; i++) {
    console.log(i);
    currentMonth = addMonths(currentMonth, 1);
    months.push(currentMonth);
  }

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
            <EditorItemContainer
              item={item}
              onClick={onClickImage}
              selectedDate={selectedDate}
              months={months}
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </EditorConWrap>
  );
};

export default EditorBodyContainer;
function useEffect(arg0: () => void, arg1: any[][]) {
  throw new Error('Function not implemented.');
}
