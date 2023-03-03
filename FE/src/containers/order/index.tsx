import PBody from 'components/common/PBody';
import ConfirmOrderModal from 'components/order/ConfirmOrderModal';
import { useAppSelector, useAppDispatch } from 'hooks';
import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router';
import { useSearchParams } from 'react-router-dom';
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
    setModalOpen(true);
  };

  const handleCloseModal = () => {
    setModalOpen(false);
  };

  const handleSubmitOrderInfo = () => {
    setModalOpen(false);
    navigate(`/${nansu}/order?isOrdered=true`);
    console.log(userName, userPhone, postCode, address, detailAddress);
  };

  return (
    <>
      <OrderTopSection />
      <PBody>
        {!isOrdered ? (
          <OrderFormSection onClick={handleOpenModal} />
        ) : (
          <OrderConfirmSection />
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
