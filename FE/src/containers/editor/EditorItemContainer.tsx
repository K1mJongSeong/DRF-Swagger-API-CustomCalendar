import { CtrlBlock, ImgBlock } from 'components/editor/EditorConWrap';
import { useAppDispatch, useAppSelector } from 'hooks';
import { ItemInBodyProps } from 'interface/editor';
import { useEffect, useState } from 'react';
import uuid from 'react-uuid';
import { updateImg } from 'reducer/images';
import { initialPrevImgs } from 'reducer/page';
import { RootState } from 'store';
import CalendarContainer from './calendar/CalendarContainer';

const EditorItemContainer = ({
  item,
  onClick,
  selectedDate,
  months,
}: ItemInBodyProps) => {
  const dispatch = useAppDispatch();
  const { prevImgs } = useAppSelector((state: RootState) => state.page);
  const { imgs } = useAppSelector((state: RootState) => state.images);
  const [localData, setLocalData] = useState<{
    data: Array<string>;
    pageName: string;
  } | null>(null);

  const [localLoading, setLocalLoading] = useState<boolean>(false);
  useEffect(() => {
    if (prevImgs.length <= 0) return;
    setLocalLoading(true);
    prevImgs.forEach((el) => {
      if (el.pageName === item.pageName) {
        setLocalData(el);
      }
    });
    setLocalLoading(false);
  }, [prevImgs]);

  useEffect(() => {
    if (!localData || !item.ctrlItems) return;
    if (localLoading) return;
    const ctrlNum = item.ctrlItems?.length;
    item.ctrlItems.forEach((el) => {
      console.log(localData.data);
      for (let i = 1; i < ctrlNum + 1; i++) {
        const imgObj = {
          id: el.cId,
          imgUrl: localData.data[i - 1],
          pageNo: item.id,
        };
        console.log(i);
        console.log(el.cId);
        console.log(localData.data[i - 1]);
        dispatch(updateImg(imgObj));
      }
    });
    setLocalData(null);
    dispatch(initialPrevImgs());
  }, [localData, localLoading]);
  return (
    <div className="item swiper-zoom-container">
      <div className="swiper-zoom-target">
        <div className="ctrl_wrap">
          {item.ctrlItems?.map((ci, idx) => {
            return (
              <CtrlBlock
                onClick={onClick}
                img={ci}
                key={uuid()}
                pageNo={item.id}
                prevImg={localData && localData.data[idx]}
              />
            );
          })}
        </div>
        <div className="page_wrap">
          {item.ctrlItems?.map((ci) => (
            <ImgBlock key={uuid()} img={ci} />
          ))}
          <img
            src={
              (item?.tempSrc && item?.tempSrc) ??
              'https://cdn-icons-png.flaticon.com/512/107/107817.png'
            }
          />
        </div>
        {item.isCalendar && item.month && (
          <CalendarContainer
            month={item.month}
            months={months}
            selectedDate={selectedDate}
          />
        )}
      </div>
    </div>
  );
};

export default EditorItemContainer;
