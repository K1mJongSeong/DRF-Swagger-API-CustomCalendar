import Button from 'components/common/Button';
import styled from 'styled-components';

const FixedButton = ({
  onClick,
}: {
  nansu: string | undefined;
  onClick: () => void;
}) => {
  return (
    <FixedButtonBlock>
      <Button $navi $fullWidth onClick={onClick}>
        템플릿 선택
      </Button>
    </FixedButtonBlock>
  );
};

const FixedButtonBlock = styled.div`
  width: 100%;
  max-width: 1024px;
  background-color: white;
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  padding: 1rem;
`;

export default FixedButton;
