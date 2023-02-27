import styled from 'styled-components';

const ListTop = ({ children }: { children: React.ReactNode }) => {
  return <ListTopBlock>{children}</ListTopBlock>;
};

const ListTopBlock = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  font-weight: 800;
  padding: 16px;
  border-bottom: 1px solid #ccc;
  z-index: 99;

  & > button {
    margin-right: 1rem;
  }
`;

export default ListTop;
