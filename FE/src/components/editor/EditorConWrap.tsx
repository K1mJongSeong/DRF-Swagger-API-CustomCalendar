import styled from 'styled-components';
import { FcPlus } from 'react-icons/fc';
import { ImgBlockProps } from 'interface/editor';
import { useRef, useEffect, useState } from 'react';
import { useAppSelector } from 'hooks';
import { RootState } from 'store';

const EditorConWrap = ({ children }: { children: React.ReactNode }) => {
  return <EditorConWrapBlock>{children}</EditorConWrapBlock>;
};

export const CtrlBlock = ({ img, onClick, pageNo }: ImgBlockProps) => {
  const { imgs, selectedId } = useAppSelector(
    (state: RootState) => state.images,
  );

  const [hadImg, setHadImg] = useState<boolean>(false);
  const [isSelect, setIsSelect] = useState<boolean>(false);

  useEffect(() => {
    if (selectedId === img.cId) {
      setIsSelect(true);
    } else {
      setIsSelect(false);
    }
  }, [selectedId]);

  useEffect(() => {
    setHadImg(false);
    imgs.forEach((el) => {
      if (el.id === img.cId) {
        setHadImg(true);
      }
    });
  }, [imgs]);

  const handleClickImg = (cId: number) => {
    if (!onClick || !pageNo) return;
    onClick(cId, pageNo);
  };

  return (
    <div
      onClick={() => handleClickImg(img.cId)}
      className={isSelect ? 'ctrl_handler select' : 'ctrl_handler'}
      style={{
        width: img.w,
        height: img.h,
        top: img.t,
        left: img.l,
      }}
    >
      {hadImg || <FcPlus />}
    </div>
  );
};

export const ImgBlock = ({ img }: ImgBlockProps) => {
  const { imgs } = useAppSelector((state: RootState) => state.images);
  const [hadImg, setHadImg] = useState<boolean>(false);

  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    ref.current.style.background = 'none';
    setHadImg(false);

    imgs.forEach((el) => {
      if (!ref.current) return;
      if (el.id === img.cId) {
        ref.current.style.background = `url(${el.imgUrl}) no-repeat 50% /cover`;
        setHadImg(true);
      }
    });
  }, [imgs]);

  return (
    <div
      ref={ref}
      className={hadImg ? 'img_viewer noBorder' : 'img_viewer'}
      style={{
        width: img.w,
        height: img.h,
        top: img.t,
        left: img.l,
      }}
    ></div>
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
      max-width: 700px;
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
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 2rem;
          cursor: pointer;
          &.select {
            border: 1px solid #e64c66;
          }
        }
      }

      .page_wrap {
        position: relative;
        z-index: 8;

        .img_viewer {
          position: absolute;
          background: inherit;
          border: 1px dashed #999;
          z-index: 7;
          &.noBorder {
            border: none;
          }
        }
        .temp_image {
          width: 100%;
          height: 100%;
          background-color: white;
          position: absolute;
          z-index: 6;
        }
        .temp {
        }
      }

      &.lg {
        min-width: 2000px;
        min-height: 1423.6874px;
        /* min-width: 2457px;
        min-height: 1749px; */
        .cl {
          width: 67.3992%;
          height: 72.7272%;
          .row {
            width: 100%;
            .cell {
              width: 14.2857%;
              font-size: 1.5rem !important;
              &.red {
                .red.txt {
                  zoom: 1;
                  font-size: 1rem !important;
                  margin-top: 0.2rem;
                }
              }
              .cell_top {
                max-width: 100%;
                margin-bottom: 0;
              }
              .memo_con {
                margin-top: 0.3rem;
                font-size: 1rem !important;
                zoom: 1;
                white-space: pre-line;
              }
            }
          }
        }
      }
    }
  }
`;

export default EditorConWrap;
