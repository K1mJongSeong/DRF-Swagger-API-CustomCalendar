import styled from 'styled-components';

const Top = ({ children }: { children: React.ReactNode }) => {
  return <TopBlock>{children}</TopBlock>;
};

const TopBlock = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  font-weight: 800;
  padding: 16px;
  border-bottom: 1px solid #ccc;
  z-index: 99;
`;

export default Top;
