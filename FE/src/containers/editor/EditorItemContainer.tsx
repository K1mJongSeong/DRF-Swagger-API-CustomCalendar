/* eslint-disable prefer-const */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { CtrlBlock, ImgBlock } from 'components/editor/EditorConWrap';
import { ItemInBodyProps } from 'interface/editor';
import CalendarContainer from './calendar/CalendarContainer';

const EditorItemContainer = ({
  item,
  onClick,
  selectedDate,
  months,
}: ItemInBodyProps) => {
  return (
    <div className="item swiper-zoom-container">
      <div className="swiper-zoom-target">
        <div className="ctrl_wrap">
          {item.ctrlItems?.map((ci, idx) => (
            <CtrlBlock onClick={onClick} img={ci} key={idx} pageNo={item.id} />
          ))}
        </div>
        <div className="page_wrap">
          {item.ctrlItems?.map((ci, idx) => (
            <ImgBlock key={idx} img={ci} />
          ))}
          <img src={item?.tempSrc} />
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
