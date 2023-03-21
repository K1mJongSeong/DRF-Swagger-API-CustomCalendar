import styled from 'styled-components';

const SubEditBottom = ({ children }: { children: React.ReactNode }) => {
  return <SubEditBottomBlock>{children}</SubEditBottomBlock>;
};

const SubEditBottomBlock = styled.div`
  width: 100%;
  min-height: 47px;
  position: fixed;
  padding: 0.7rem 1rem;
  bottom: 56px;
  left: 0;
  color: white;
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export default SubEditBottom;
