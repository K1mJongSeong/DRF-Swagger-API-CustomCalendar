/* eslint-disable @typescript-eslint/no-explicit-any */
import { Link } from 'react-router-dom';
import styled, { css } from 'styled-components';

interface ButtonProps {
  children: React.ReactNode;
  to?: string;
  $fullWidth?: boolean;
  $red?: boolean;
  $navi?: boolean;
  $borderBtn?: boolean;
  $borderRedBtn?: boolean;
  $blue?: boolean;
  $gray?: boolean;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
}

const Button = (props: ButtonProps) => {
  return props?.to ? (
    <StyledLink {...props} />
  ) : (
    <StyledButton type="button" {...props} />
  );
};

const buttonStyle = css`
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  min-width: 120px;
  min-height: 54px;
  border-radius: 8px;
  padding: 7px 1rem;
  font-size: 1.125rem;
  color: #555;
  outline: none;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 800;

  &:hover {
    background-color: #555;
    color: white;
  }
  ${(props: ButtonProps) =>
    props.$fullWidth &&
    css`
      padding-top: 0.75rem;
      padding-bottom: 0.75rem;
      width: 100%;
    `}
  ${(props: ButtonProps) =>
    props.$red &&
    css`
      background-color: #e64c66;
      color: white;
      &:hover {
        background-color: #e64c66;
        opacity: 0.7;
      }
    `}
  ${(props: ButtonProps) =>
    props.$navi &&
    css`
      background-color: #345087;
      color: white;
      &:hover {
        background-color: #345087;
        opacity: 0.7;
      }
    `}
  ${(props: ButtonProps) =>
    props.$blue &&
    css`
      background-color: #495bff;
      color: white;
      &:hover {
        background-color: #495bff;
        opacity: 0.7;
      }
    `}
  ${(props: ButtonProps) =>
    props.$gray &&
    css`
      background-color: #ccc;
      color: white;
      &:hover {
        background-color: #ccc;
        opacity: 0.7;
      }
    `}
  ${(props: ButtonProps) =>
    props.$borderRedBtn &&
    css`
      color: #e64c66;
      background-color: white;
      border: 1px solid #e64c66;
      font-weight: 800;
      &:hover {
        background-color: #e64c66;
        color: white;
      }
    `}
  ${(props: ButtonProps) =>
    props.$borderBtn &&
    css`
      color: black;
      background-color: white;
      border: 1px solid #ccc;
      font-weight: 800;
      &:hover {
        background-color: #eee;
        color: black;
      }
    `}
`;

const StyledButton = styled.button`
  ${buttonStyle}
`;
const StyledLink: any = styled(Link)`
  ${buttonStyle}
`;

export default Button;
