import styled from 'styled-components';

const TextEditor = ({ children }: { children: React.ReactNode }) => {
  return <TextEditorBlock>{children}</TextEditorBlock>;
};

export const CustomColorBtn = ({
  onClick,
  color,
}: {
  onClick: () => void;
  color: string;
}) => {
  return (
    <>
      <StyledButton onClick={onClick}>
        <span style={{ background: color }} />
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
    position: relative;
  }
  & > div + div {
    margin-left: 2.2rem;
  }

  & > div:last-child::before {
    content: '';
    width: 1px;
    height: 15px;
    background-color: white;
    position: absolute;
    left: -1.1rem;
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

      .tui-colorpicker-clearfix {
        position: relative;
        margin-top: 3px;

        .tui-colorpicker-palette-toggle-slider {
          display: none;
        }
        input[type='text'] {
          height: 30px;
          padding: 0 4px 0 1.7rem;
          width: 100%;
          border: 1px solid #ccc;
          background-color: #eee;
          border-radius: 3px;
          &:focus {
            outline: none;
          }
        }
        span.tui-colorpicker-palette-preview {
          width: 20px;
          height: 20px;
          border-radius: 50%;
          position: absolute;
          z-index: 9;
          top: 50%;
          left: 3px;
          transform: translateY(-50%);
        }
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
    border: 1px solid white;
  }
`;

export default TextEditor;
