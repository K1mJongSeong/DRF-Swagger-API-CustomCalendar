/* eslint-disable @typescript-eslint/no-non-null-assertion */
/* eslint-disable prefer-const */
const dataURLtoFile = (dataurl: string, fileName: string) => {
  if (!dataurl) return;
  const arr = dataurl.split(',');
  alert(arr[1]);
  console.log('arr', arr);
  alert(arr);
  const obj = arr[0].match(/:(.*?);/);
  if (!obj) return;
  const mime = obj[1];
  const bstr = atob(arr[1]);
  let n = bstr.length,
    u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new File([u8arr], fileName, { type: mime });
};
export default dataURLtoFile;
