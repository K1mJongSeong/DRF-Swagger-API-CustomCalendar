/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
import EditorConWrap from 'components/editor/EditorConWrap';
import { Renault } from 'data/template/renault';
import { addMonths, format } from 'date-fns';
import { useAppSelector } from 'hooks';
import { EditorConProps } from 'interface/editor';
import { useCallback, useEffect, useState } from 'react';
import { RootState } from 'store';
import EditorItemContainer from './EditorItemContainer';

const EditorBodyContainer = (props: EditorConProps) => {
  const {
    Swiper,
    SwiperSlide,
    thumbsSwiper,
    FreeMode,
    Thumbs,
    swiperRef,
    onSwiper,
    onClickImage,
  } = props;

  let currentDate = new Date();
  // 2023년 달력 1월 기준
  let selectedDate = new Date('2023-01-01');

  let currentMonth = new Date(format(currentDate, 'yyyy'));
  let months: any[] = [];
  months.push(currentMonth);
  for (let i = 0; i < 11; i++) {
    currentMonth = addMonths(currentMonth, 1);
    months.push(currentMonth);
  }

  return (
    <EditorConWrap>
      <Swiper
        ref={swiperRef}
        spaceBetween={10}
        thumbs={{ swiper: thumbsSwiper }}
        modules={[FreeMode, Thumbs]}
        zoom={{ maxRatio: 5 }}
        touchRatio={0}
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
