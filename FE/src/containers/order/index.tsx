import PBody from 'components/common/PBody';
import OrderTemplate from 'components/order/OrderTemplate';
import OrderTopSection from './OrderTopSection';

const OrderContainer = () => {
  return (
    <>
      <OrderTopSection />
      <PBody>
        <OrderTemplate>
          <>예시</>
        </OrderTemplate>
      </PBody>
    </>
  );
};

export default OrderContainer;
