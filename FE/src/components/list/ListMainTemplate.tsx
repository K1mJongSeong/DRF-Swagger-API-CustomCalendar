import styled from 'styled-components';

const ListMainTemplate = ({ children }: { children: React.ReactNode }) => {
  return <ListMainTemplateBlock>{children}</ListMainTemplateBlock>;
};

const ListMainTemplateBlock = styled.div`
  width: 100%;
  height: calc(100% - 52px);
  padding: 20px 16px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

export default ListMainTemplate;
