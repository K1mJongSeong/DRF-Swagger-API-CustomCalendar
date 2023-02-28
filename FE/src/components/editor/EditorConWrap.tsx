import { Renault } from 'data/template/renault';
import styled from 'styled-components';
import { SwiperProps, SwiperRef, SwiperSlideProps } from 'swiper/react';
import { Swiper, SwiperModule } from 'swiper/types';
import { FcPlus } from 'react-icons/fc';
import { useState } from 'react';

interface EditorConProps {
  Swiper: React.FunctionComponent<React.RefAttributes<SwiperRef> & SwiperProps>;
  SwiperSlide: React.FunctionComponent<SwiperSlideProps>;
  thumbsSwiper?: Swiper | null;
  FreeMode: SwiperModule;
  Navigation: SwiperModule;
  Thumbs: SwiperModule;
  swiperRef: React.Ref<SwiperRef> | undefined;
  onSwiper: (idx: number) => void;
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

const EditorConWrap = ({
  Swiper,
  SwiperSlide,
  thumbsSwiper,
  FreeMode,
  Navigation,
  Thumbs,
  swiperRef,
  onSwiper,
}: EditorConProps) => {
  return (
    <EditorConWrapBlock>
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
            <EditorItem item={item} />
          </SwiperSlide>
        ))}
      </Swiper>
    </EditorConWrapBlock>
  );
};

const EditorItem = ({ item }: itemProps) => {
  const [imgFile, setImgFile] = useState<string | ArrayBuffer | null>('');
  const onClick = (cId: number) => {
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', '.jpg, .png');
    input.click();

    input.onchange = async () => {
      const files = input.files;
      if (files) {
        const file = files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = () => {
          setImgFile(reader.result);
          console.log(imgFile);
        };
        console.log(imgFile);
      }
    };
  };
  return (
    <div className="item">
      <div className="ctrl_wrap">
        {item.ctrlItems?.map((ci, idx) => (
          <div
            onClick={() => onClick(ci.cId)}
            key={idx}
            className="ctrl_handler"
            style={{
              width: ci.w,
              height: ci.h,
              top: ci.t,
              left: ci.l,
            }}
          >
            <FcPlus />
          </div>
        ))}
      </div>
      <div className="page_wrap">
        {item.ctrlItems?.map((ci, idx) => (
          <div
            key={idx}
            id={`view_${ci.cId}`}
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
    </div>
  );
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

    .item {
      width: calc(100% - 32px);
      max-width: 500px;
      position: relative;

      .ctrl_wrap {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        z-index: 9;

        .ctrl_handler {
          position: absolute;
          border: 1px dashed #999;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 2rem;
          cursor: pointer;
        }
      }

      .page_wrap {
        position: relative;
        z-index: 8;

        .img_viewer {
          position: absolute;
          background: inherit;
        }
      }
    }
  }
`;

export default EditorConWrap;
