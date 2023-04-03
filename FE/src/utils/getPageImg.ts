/* eslint-disable no-inner-declarations */
/* eslint-disable @typescript-eslint/no-non-null-assertion */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable prefer-const */
import { detect } from 'detect-browser';
import * as htmlToImage from 'html-to-image';
import html2canvas from 'html2canvas';
import client from 'lib/api/client';
import moment from 'moment';
import dataURLtoFile from './datUrlToFile';

export default class GetPageImg {
  async getTotalPage(pageName: string, nansu: string) {
    const browser = detect();
    console.log(browser?.os);
    try {
      if (browser?.os === 'iOS') {
        const canvas = await html2canvas(
          document.querySelector(
            `#item${pageName ? pageName : ''}`,
          ) as HTMLDivElement,
          {
            useCORS: true,
          },
        );

        const dataUrl = canvas.toDataURL('image/jpeg', 0.9);
        const imgFile = dataURLtoFile(
          dataUrl,
          `${nansu}-${pageName}${moment().format('YYMMDDHHMMSS')}-ios.jpeg`,
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
      }
      const dataUrl = await htmlToImage.toJpeg(
        document.querySelector(
          `#item${pageName ? pageName : ''}`,
        ) as HTMLDivElement,
      );

      const imgFile = dataURLtoFile(
        dataUrl,
        `${nansu}-${pageName}${moment().format('YYMMDDHHMMSS')}.jpeg`,
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
      alert(err);
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
