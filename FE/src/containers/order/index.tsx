import PBody from 'components/common/PBody';
import { useState } from 'react';
import OrderConfirmSection from './OrderConfirmSection';
import OrderFormSection from './OrderFormSection';
import OrderTopSection from './OrderTopSection';

const OrderContainer = () => {
  const [isOrdered, setIsOrdered] = useState<boolean>(false);
  return (
    <>
      <OrderTopSection />
      <PBody>
        {!isOrdered ? <OrderFormSection /> : <OrderConfirmSection />}
      </PBody>
    </>
  );
};

export default OrderContainer;
