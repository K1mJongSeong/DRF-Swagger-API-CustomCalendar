import styled, { css } from 'styled-components';

interface EditorButtonProps {
  children?: React.ReactNode;
  white?: boolean;
  red?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  fs?: string;
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
`;

const EditorButtonBlock = styled.button`
  ${buttonStyle}
`;
