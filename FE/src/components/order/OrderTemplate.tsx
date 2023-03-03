import Button from 'components/common/Button';
import styled from 'styled-components';

const OrderTemplate = ({
  children,
  title,
  onClick,
}: {
  children: React.ReactNode;
  title: string;
  onClick?: () => void;
}) => {
  return (
    <OrderTemplateBlock>
      <h2>{title}</h2>
      {children}
      <Button $fullWidth $red onClick={onClick}>
        {title === '주문접수' ? '주문' : '확인'}
      </Button>
    </OrderTemplateBlock>
  );
};

const OrderTemplateBlock = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  h2 {
    font-size: 1.125rem;
    text-align: center;
    margin-bottom: 25px;
  }

  form {
    flex: 1;
    margin-bottom: 25px;

    label {
      display: inline-block;
      margin-bottom: 7px;
      font-weight: 800;
    }
  }

  & > button {
    margin-top: 25px;
  }
`;

export const StyledInput = styled.input`
  width: 100%;
  height: 49px;
  outline: none;
  border: none;
  border-bottom: 1px solid #ccc;
  margin-bottom: 20px;
  padding: 10px;
  transition: all 0.3s;

  &::placeholder {
    font-size: 14px;
    color: #ccc;
  }

  &:focus {
    border-bottom: 1px solid #e64c66;
  }
`;

export const StyledSearchBtn = styled(Button)`
  min-width: 102px;
  min-height: 49px;
  border: 1px solid #e64c66;
  color: #e64c66;
  background-color: white;
  margin-left: 10px;

  &:hover {
    background-color: #e64c66;
    color: white;
  }
`;

export default OrderTemplate;
