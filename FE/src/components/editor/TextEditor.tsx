import styled from 'styled-components';

const TextEditor = ({ children }: { children: React.ReactNode }) => {
  return <TextEditorBlock>{children}</TextEditorBlock>;
};

const TextEditorBlock = styled.div`
  width: 100%;
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

export default TextEditor;
