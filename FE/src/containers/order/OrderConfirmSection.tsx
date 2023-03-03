import OrderTemplate from 'components/order/OrderTemplate';

const OrderConfirmSection = () => {
  return (
    <OrderTemplate title="주문완료">
      <div className="order_done_con">
        <h2>
          <span>***님!</span> 캘린더 주문이 <br />
          완료되었습니다.
        </h2>
        <p>해당 링크에서 재주문은 불가능합니다.</p>
        <p>
          배송정보는 빠른 시일 내에
          <br />
          sms로 전달됩니다.
        </p>
      </div>
    </OrderTemplate>
  );
};

export default OrderConfirmSection;
