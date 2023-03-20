import styled from 'styled-components';

const TextEditor = ({ children }: { children: React.ReactNode }) => {
  return <TextEditorBlock>{children}</TextEditorBlock>;
};

export const CustomColorBtn = ({ onClick }: { onClick: () => void }) => {
  return (
    <>
      <StyledButton onClick={onClick}>
        <span />
      </StyledButton>
    </>
  );
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

  & > div {
    display: flex;
    align-items: center;
  }
  & > div + div {
    margin-left: 24px;
  }
  .colorBtn_wrap {
    position: relative;

    #color-picker {
      position: absolute;
      bottom: 30px;
      right: 0;
      padding: 1rem;
      background-color: white;
      border-radius: 3px 3px 0 3px;
      box-shadow: 0 3px 22px 6px rgba(0, 0, 0, 0.15);

      &::after {
        content: '';
        width: 0;
        height: 0;
        border-right: 7px solid transparent;
        border-top: 8px solid #fff;
        border-left: 7px solid transparent;
        position: absolute;
        right: 0;
        bottom: 0;
        transform: translateY(100%);
      }
    }
  }
`;

const StyledButton = styled.button`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  white-space: normal;
  background: none;
  border: none;
  font-size: 13px;
  color: white;
  &:focus {
    outline: none;
  }

  & > span {
    display: block;
    min-width: 20px;
    max-width: 20px;
    min-height: 20px;
    max-height: 20px;
    border-radius: 50%;
    background-color: white;
  }
`;

export default TextEditor;
