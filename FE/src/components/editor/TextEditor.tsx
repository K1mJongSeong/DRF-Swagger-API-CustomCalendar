import styled from 'styled-components';

const TextEditor = () => {
  return <TextEditorBlock>텍스트</TextEditorBlock>;
};

const TextEditorBlock = styled.div`
  width: 100%;
  position: fixed;
  padding: 1rem;
  bottom: 56px;
  left: 0;
  color: white;
  background-color: black;
`;

export default TextEditor;
