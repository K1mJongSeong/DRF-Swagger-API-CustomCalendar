/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
import EditorConWrap from 'components/editor/EditorConWrap';
import { Renault } from 'data/template/renault';
import { addMonths, format } from 'date-fns';
import { useAppDispatch, useAppSelector } from 'hooks';
import { EditorConProps } from 'interface/editor';
import moment from 'moment';
import { useEffect } from 'react';
import { getHolidays } from 'reducer/holidays';
import { RootState } from 'store';
import EditorItemContainer from './EditorItemContainer';

const EditorBodyContainer = (props: EditorConProps) => {
  const dispatch = useAppDispatch();
  const { holidays } = useAppSelector((state: RootState) => state.holidays);

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
    currentMonth = addMonths(currentMonth, 1);
    months.push(currentMonth);
  }

  useEffect(() => {
    return () => {
      for (let i = 1; i < 13; i++) {
        const str = i.toString();
        if (str.length === 1) {
          dispatch(getHolidays(`0${str}`));
        } else {
          dispatch(getHolidays(str));
        }
      }
    };
  }, []);

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
