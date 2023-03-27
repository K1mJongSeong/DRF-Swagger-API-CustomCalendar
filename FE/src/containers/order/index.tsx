/* eslint-disable camelcase */
import PBody from 'components/common/PBody';
import ConfirmOrderModal from 'components/order/ConfirmOrderModal';
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
  const { orderInfo } = useAppSelector((state: RootState) => state.order);
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

  const handleSubmitOrderInfo = () => {
    if (!nansu) return;
    dispatch(
      postOrder({
        nansu,
        postOrderPayload: {
          user_name: userName,
          user_phone: userPhone,
          address,
          postcode: postCode,
          detailAddress,
          orderState: '주문신청',
          order_date: moment().toString(),
        },
      }),
    );
    // setModalOpen(false);

    // navigate(`/${nansu}/order?isOrdered=true`);
    // console.log(userName, userPhone, postCode, address, detailAddress);
  };

  const handleCompleteOrder = () => {
    navigate('/');
  };

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
