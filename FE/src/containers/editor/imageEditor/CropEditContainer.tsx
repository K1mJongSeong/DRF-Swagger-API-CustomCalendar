import CropZone from 'components/editor/CropZone';
import { EditorTextButton } from 'components/editor/EditorButtons';

const CropEditContainer = ({
  onChange,
  onApply,
  onCancle,
}: {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onApply: () => void;
  onCancle: () => void;
}) => {
  return (
    <CropZone>
      <div className="select_mode_wrap">
        <label>
          <input
            type="radio"
            name="select_mode"
            value="none"
            onChange={onChange}
            defaultChecked
          />
          <span className="txt">Custom</span>
        </label>
        <label>
          <input
            type="radio"
            name="select_mode"
            value="1"
            onChange={onChange}
          />
          <span className="txt">Square</span>
        </label>
        <label>
          <input
            type="radio"
            name="select_mode"
            value="2"
            onChange={onChange}
          />
          <span className="txt">3:2</span>
        </label>
        <label>
          <input
            type="radio"
            name="select_mode"
            value="3"
            onChange={onChange}
          />
          <span className="txt">4:3</span>
        </label>
        <label>
          <input
            type="radio"
            name="select_mode"
            value="4"
            onChange={onChange}
          />
          <span className="txt">5:4</span>
        </label>
      </div>
      <div className="crop_btns_wrap">
        <EditorTextButton white onClick={onApply}>
          선택
        </EditorTextButton>
        <EditorTextButton red onClick={onCancle}>
          취소
        </EditorTextButton>
      </div>
    </CropZone>
  );
};

export default CropEditContainer;
