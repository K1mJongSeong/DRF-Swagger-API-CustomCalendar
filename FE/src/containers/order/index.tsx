/* eslint-disable camelcase */
import PBody from 'components/common/PBody';
import ConfirmOrderModal from 'components/order/ConfirmOrderModal';
import { Renault } from 'data/template/renault';
import { useAppSelector, useAppDispatch } from 'hooks';
import moment from 'moment';
import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router';
import { useSearchParams } from 'react-router-dom';
import { postOrder } from 'reducer/order';
import { RootState } from 'store';
import OrderConfirmSection from './OrderConfirmSection';
import OrderFormSection from './OrderFormSection';
import OrderTopSection from './OrderTopSection';

const OrderContainer = () => {
  const {
    orderInfo,
    postOrderResult,
    error: orderError,
  } = useAppSelector((state: RootState) => state.order);
  const { totalPicArr } = useAppSelector((state: RootState) => state.page);
  const navigate = useNavigate();
  const params = useParams();
  const [searchParams] = useSearchParams();
  const { nansu } = params;

  const dispatch = useAppDispatch();

  const { userName, userPhone, postCode, address, detailAddress } = orderInfo;

  const [modalOpen, setModalOpen] = useState<boolean>(false);
  const [isOrdered, setIsOrdered] = useState<boolean>(false);

  useEffect(() => {
    if (searchParams?.get('isOrdered')) setIsOrdered(true);
  }, [searchParams]);

  const handleOpenModal = () => {
    if (!userName) return alert('성명을 입력해주세요.');
    if (!userPhone) return alert('연락처를 입력해주세요.');
    if (!postCode || !address) return alert('주소를 입력해주세요.');
    if (!detailAddress) return alert('상세주소를 입력해주세요.');
    setModalOpen(true);
  };

  const handleCloseModal = () => {
    setModalOpen(false);
  };

  const count = Renault.length - 1;

  const handleSubmitOrderInfo = () => {
    if (!nansu) return;
    const totalPic = totalPicArr.map((el) => {
      return el.total_pic;
    });
    if (totalPic.length < count) {
      alert('Error: 모든 페이지가 저장되지 않았습니다. 다시 시도해주세요.');
      return;
    }
    dispatch(
      postOrder({
        nansu,
        postOrderPayload: {
          user_name: userName,
          user_phone: userPhone,
          address,
          postcode: postCode,
          nansu,
          detailAddress,
          orderState: '주문신청',
          order_date: moment().format(),
          pic: totalPic.join(),
        },
      }),
    );
  };

  const handleCompleteOrder = () => {
    navigate('/');
  };

  useEffect(() => {
    if (orderError) {
      alert(orderError);
      setModalOpen(false);
      return;
    }
    if (postOrderResult) {
      setModalOpen(false);
      navigate(`/${nansu}/order?isOrdered=true`);
    }
  }, [postOrderResult, orderError]);

  return (
    <>
      <OrderTopSection />
      <PBody>
        {!isOrdered ? (
          <OrderFormSection onClick={handleOpenModal} />
        ) : (
          <OrderConfirmSection onClick={handleCompleteOrder} />
        )}
        {modalOpen && (
          <ConfirmOrderModal
            close={handleCloseModal}
            submit={handleSubmitOrderInfo}
          />
        )}
      </PBody>
    </>
  );
};

export default OrderContainer;
