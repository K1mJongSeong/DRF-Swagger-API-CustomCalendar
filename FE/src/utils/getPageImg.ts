/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable prefer-const */
import html2canvas from 'html2canvas';

export default class GetPageImg {
  async getPageCanvasToImg(id: string, nansu: string) {
    const canvas = await html2canvas(
      document.querySelector(`#item${id ? id : ''}`) as HTMLDivElement,
      // { width: 2457, height: 1749 },
    );
    const dataURL = canvas.toDataURL('image/jpeg');

    console.log('1', dataURL);
    // dataURL to file
    const dataURLtoFile = (dataurl: any, fileName: string) => {
      if (!dataurl) return;
      const arr = dataurl.split(',');
      const mime = arr[0].match(/:(.*?);/)[1];
      const bstr = atob(arr[1]);
      let n = bstr.length,
        u8arr = new Uint8Array(n);

      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }

      return new File([u8arr], fileName, { type: mime });
    };

    const imgFile = dataURLtoFile(dataURL, `${nansu}-${id}.jpg`);
    console.log('2', imgFile);
    return imgFile;
  }
}
