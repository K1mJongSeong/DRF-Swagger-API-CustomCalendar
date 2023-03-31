/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable prefer-const */
import * as htmlToImage from 'html-to-image';
import client from 'lib/api/client';
import moment from 'moment';

export default class GetPageImg {
  async getTotalPage(pageName: string, nansu: string) {
    try {
      const img = await htmlToImage.toJpeg(
        document.querySelector(
          `#item${pageName ? pageName : ''}`,
        ) as HTMLDivElement,
      );
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

      const imgFile = dataURLtoFile(
        img,
        `${nansu}-${pageName}${moment().format('YYMMDDHHMMSS')}.jpg`,
      );
      const formData = new FormData();
      if (!imgFile) return;
      formData.append('image', imgFile);
      const res = await client.post('/Image/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      return res.data.image;
    } catch (err) {
      console.log(err);
    }
  }

  resizingItem(id: string, size: string) {
    const target = document.querySelector(
      `#item${id ? id : ''}`,
    ) as HTMLDivElement;
    if (size === 'lg') {
      target.classList.add('lg');
    } else if (size === 'sm') {
      target.classList.remove('lg');
    }
  }
}
