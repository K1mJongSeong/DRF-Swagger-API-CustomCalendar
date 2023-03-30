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

          &.noBorder {
            border: none;
          }
        }
      }

      &.lg {
        min-width: 2457px;
        min-height: 1749px;
        .cl {
          .row {
            .cell {
              font-size: 1.25rem !important;
              &.red {
                .red.txt {
                  zoom: 0.7;
                  margin-top: 0.7rem;
                }
              }
              .memo_con {
                margin-top: 1rem;
                font-size: 1.2rem !important;
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
