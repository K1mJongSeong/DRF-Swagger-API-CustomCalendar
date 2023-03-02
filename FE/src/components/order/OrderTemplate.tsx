import Button from 'components/common/Button';
import styled from 'styled-components';

const OrderTemplate = ({ children }: { children: React.ReactNode }) => {
  return (
    <OrderTemplateBlock>
      <h2>주문접수</h2>
      {children}
      <Button $fullWidth $red>
        주문
      </Button>
    </OrderTemplateBlock>
  );
};

const OrderTemplateBlock = styled.div`
  width: 100%;
  height: 100%;

  h2 {
    font-size: 1.125rem;
    text-align: center;
    margin-bottom: 25px;
  }
`;

export default OrderTemplate;
