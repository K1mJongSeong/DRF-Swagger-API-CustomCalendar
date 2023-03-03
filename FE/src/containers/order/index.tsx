import PBody from 'components/common/PBody';
import ConfirmOrderModal from 'components/order/ConfirmOrderModal';
import { useAppSelector, useAppDispatch } from 'hooks';
import { useState } from 'react';
import { RootState } from 'store';
import OrderConfirmSection from './OrderConfirmSection';
import OrderFormSection from './OrderFormSection';
import OrderTopSection from './OrderTopSection';

const OrderContainer = () => {
  const { orderInfo } = useAppSelector((state: RootState) => state.order);
  const dispatch = useAppDispatch();

  const { userName, userPhone, postCode, address, detailAddress } = orderInfo;

  const [modalOpen, setModalOpen] = useState<boolean>(false);
  const [isOrdered, setIsOrdered] = useState<boolean>(false);

  const handleOpenModal = () => {
    setModalOpen(true);
  };

  const handleCloseModal = () => {
    setModalOpen(false);
  };

  const handleSubmitOrderInfo = () => {
    setModalOpen(false);
    setIsOrdered(true);
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
