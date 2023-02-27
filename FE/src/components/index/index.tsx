import styled from 'styled-components';

const Index = () => {
  alert('올바른 링크로 접근해주세요.');
  return <IndexBlock>올바른 접근이 아닙니다</IndexBlock>;
};

const IndexBlock = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
`;

export default Index;
