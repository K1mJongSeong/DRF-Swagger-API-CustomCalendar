import styled from 'styled-components';

const EditorBottom = ({ children }: { children: React.ReactNode }) => {
  return (
    <EditorBottomBlock>
      <div className="editor_bot_ctrl">{children}</div>
    </EditorBottomBlock>
  );
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
  padding: 17px;
  .editor_bot_ctrl {
    width: calc(100% - 40px);
    max-width: 500px;
    display: flex;
    justify-content: space-between;
    color: white;
    white-space: nowrap;
    button {
      width: 33.333%;
    }
  }
`;

export default EditorBottom;
