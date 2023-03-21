import styled, { css } from 'styled-components';

interface EditorButtonProps {
  children?: React.ReactNode;
  white?: boolean;
  red?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  fs?: string;
  checked?: boolean;
  isOpacity?: boolean;
  disabled?: boolean;
  p?: string;
}
export const EditorIconButton = (props: EditorButtonProps) => {
  return <EditorButtonBlock {...props} />;
};

export const EditorTextButton = (props: EditorButtonProps) => {
  return <EditorButtonBlock {...props} />;
};

const buttonStyle = css`
  cursor: pointer;
  background: none;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  outline: none;
  color: black;
  &:focus {
    outline: none;
  }

  & + & {
    margin-left: 1rem;
  }

  ${(props: EditorButtonProps) =>
    props.white &&
    css`
      color: white;
    `}
  ${(props: EditorButtonProps) =>
    props.red &&
    css`
      color: #e64c66;
      &:hover {
        color: #ff5370;
      }
    `}
  ${(props: EditorButtonProps) =>
    props.fs &&
    css`
      font-size: ${props.fs}px;
    `}
  ${(props: EditorButtonProps) =>
    props.checked &&
    css`
      background-color: white;
      color: black;
      border-radius: 3px;
    `}
  ${(props: EditorButtonProps) =>
    props.isOpacity &&
    css`
      opacity: 0.7;
    `}
  ${(props: EditorButtonProps) =>
    props.disabled &&
    css`
      opacity: 0.7;
      pointer-events: none;
    `}
  ${(props: EditorButtonProps) =>
    props.p &&
    css`
      padding: ${props.p}px;
    `}
`;

const EditorButtonBlock = styled.button`
  ${buttonStyle}
`;
