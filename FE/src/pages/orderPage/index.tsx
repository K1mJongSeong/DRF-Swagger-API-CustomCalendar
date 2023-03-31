/* eslint-disable camelcase */
import DefaultTemplate from 'components/common/DefaultTemplate';
import OrderContainer from 'containers/order';
import { Renault } from 'data/template/renault';
import { useAppDispatch, useAppSelector } from 'hooks';
import { useEffect } from 'react';
import { useNavigate, useParams } from 'react-router';
import {
  updatePrevLoading,
  getPage,
  updatePrevImgs,
  updateSavedPages,
  updateTotalPicArr,
  initialPageError,
} from 'reducer/page';
import { RootState } from 'store';

const OrderPage = () => {
  const dispatch = useAppDispatch();
  const { getPageResult, error: pageError } = useAppSelector(
    (state: RootState) => state.page,
  );

  const navigate = useNavigate();
  const { nansu } = useParams();
  /** 첫 렌더링 시 작업리스트 가져오기 */
  useEffect(() => {
    if (!nansu) return;
    dispatch(updatePrevLoading(true));
    Renault.forEach((el) => {
      if (!el.pageName) return;
      dispatch(getPage({ pageName: el.pageName, nansu }));
    });
  }, []);

  useEffect(() => {
    if (pageError) {
      alert('에러가 발생했습니다.');
      dispatch(initialPageError());
      return navigate(`/${nansu}`);
    }

    if (!getPageResult) return;
    if (
      getPageResult.data &&
      getPageResult.pageName &&
      getPageResult.total_pic
    ) {
      dispatch(
        updatePrevImgs({
          data: getPageResult.data,
          pageName: getPageResult.pageName,
        }),
      );
      const totalPicArrObj = {
        total_pic: getPageResult.total_pic,
        pageName: getPageResult.pageName,
      };
      dispatch(updateTotalPicArr(totalPicArrObj));
      dispatch(updatePrevLoading(false));
      dispatch(updateSavedPages(getPageResult.pageName));
    }
  }, [getPageResult, pageError]);

  return (
    <DefaultTemplate>
      <OrderContainer />
    </DefaultTemplate>
  );
};

export default OrderPage;
