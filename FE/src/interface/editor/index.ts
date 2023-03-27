import { SwiperProps, SwiperRef, SwiperSlideProps } from 'swiper/react';
import { Swiper, SwiperModule } from 'swiper/types';

export interface EditorTopProps {
  Swiper: React.FunctionComponent<React.RefAttributes<SwiperRef> & SwiperProps>;
  SwiperSlide: React.FunctionComponent<SwiperSlideProps>;
  setThumbsSwiper?: (swiper: Swiper) => void;
  FreeMode: SwiperModule;
  Navigation: SwiperModule;
  Thumbs: SwiperModule;
}

export interface EditorConProps {
  Swiper: React.FunctionComponent<React.RefAttributes<SwiperRef> & SwiperProps>;
  SwiperSlide: React.FunctionComponent<SwiperSlideProps>;
  thumbsSwiper?: Swiper | null;
  FreeMode: SwiperModule;
  Navigation: SwiperModule;
  Thumbs: SwiperModule;
  swiperRef: React.Ref<SwiperRef> | undefined;
  onSwiper: (idx: number) => void;
  onClickImage: (cId: number, pageNo: number) => void;
}

interface basicItemTypes {
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
    isCalendar?: boolean;
    month?: number | Date;
  };
  onClick?: (cId: number, pageNo: number) => void;
}
export interface ItemProps {
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
    isCalendar?: boolean;
    month?: number | Date;
  };
  onClick?: (cId: number, hadImg?: boolean) => void;
}

export interface ItemInBodyProps extends basicItemTypes {
  selectedDate: Date;
  months: Array<Date>;
}

export interface ImgBlockProps {
  img: {
    cId: number;
    w: string;
    h: string;
    l: string;
    t?: string | undefined;
  };
  onClick?: (cId: number, pageNo: number) => void;
  pageNo?: number | null;
}
