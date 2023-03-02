import PBody from 'components/common/PBody';
import OrderFormSection from './OrderFormSection';
import OrderTopSection from './OrderTopSection';

const OrderContainer = () => {
  return (
    <>
      <OrderTopSection />
      <PBody>
        <OrderFormSection />
      </PBody>
    </>
  );
};

export default OrderContainer;
