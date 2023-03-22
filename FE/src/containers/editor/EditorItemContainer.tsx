import CalendarWrap from 'components/editor/calendar/CalendarWrap';
import { CtrlBlock, ImgBlock } from 'components/editor/EditorConWrap';
import { ItemProps } from 'interface/editor';

const EditorItemContainer = ({ item, onClick }: ItemProps) => {
  return (
    <div className="item">
      <div className="ctrl_wrap">
        {item.ctrlItems?.map((ci, idx) => (
          <CtrlBlock onClick={onClick} img={ci} key={idx} />
        ))}
      </div>
      <div className="page_wrap">
        {item.ctrlItems?.map((ci, idx) => (
          <ImgBlock key={idx} img={ci} />
        ))}
        <img src={item?.tempSrc} />
      </div>
      {item.isCalendar && <CalendarWrap />}
    </div>
  );
};

export default EditorItemContainer;
