import styled from 'styled-components';

const EditorBottom = () => {
  return <EditorBottomBlock>밑에</EditorBottomBlock>;
};

const EditorBottomBlock = styled.div`
  width: 100%;
  background-color: #312b2b;
  position: fixed;
  bottom: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  padding: 17px;
`;

export default EditorBottom;
