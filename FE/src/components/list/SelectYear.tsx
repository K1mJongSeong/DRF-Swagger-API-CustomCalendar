import Button from 'components/common/Button';
import styled from 'styled-components';

const SelectYear = ({
  onChange,
  onClick,
}: {
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  onClick: React.MouseEventHandler<HTMLButtonElement>;
}) => {
  return (
    <SelectYearBlock>
      <div className="select_wrap">
        <select onChange={onChange}>
          <option value={''}>선택</option>
          <option value={2023}>2023</option>
        </select>
        년도
      </div>
      <Button $borderBtn onClick={onClick}>
        선택
      </Button>
    </SelectYearBlock>
  );
};

const SelectYearBlock = styled.div`
  width: 100%;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  .select_wrap {
    display: flex;
    margin-bottom: 23px;
    align-items: center;
    font-weight: 800;
    select {
      flex: 1;
      height: 48px;
      margin-right: 7px;
      outline: none;
      border-radius: 8px;
      border: 1px solid #ccc;
      padding-left: 1rem;
    }
  }
`;

export default SelectYear;
