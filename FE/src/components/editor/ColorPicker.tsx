/* eslint-disable @typescript-eslint/no-explicit-any */
import { useRef, useEffect } from 'react';
import colorPicker from 'tui-color-picker';
import 'tui-color-picker/dist/tui-color-picker.css';

const ColorPicker = ({ setColPick }: { setColPick: React.Dispatch<any> }) => {
  /** color picker */
  const colorPickerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!colorPickerRef.current) return;
    const instance = colorPicker.create({
      container: colorPickerRef.current,
      color: '#000000',
    });
    setColPick(instance);
  }, []);

  return <div id="color-picker" ref={colorPickerRef} />;
};

export default ColorPicker;
