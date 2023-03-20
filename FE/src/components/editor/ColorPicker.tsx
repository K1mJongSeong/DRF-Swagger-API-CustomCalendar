import { useRef, useEffect } from 'react';
import colorPicker from 'tui-color-picker';
import 'tui-color-picker/dist/tui-color-picker.css';

const ColorPicker = () => {
  /** color picker */
  const colorPickerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!colorPickerRef.current) return;
    colorPicker.create({
      container: colorPickerRef.current,
    });
  }, []);

  return <div id="color-picker" ref={colorPickerRef} />;
};

export default ColorPicker;
