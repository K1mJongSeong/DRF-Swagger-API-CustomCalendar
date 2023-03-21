import styled from 'styled-components';

const EditCtrlBtnsWrap = ({ children }: { children: React.ReactNode }) => {
  return <EditCtrlBtnsWrapBlock>{children}</EditCtrlBtnsWrapBlock>;
};

const EditCtrlBtnsWrapBlock = styled.div`
  width: auto;
  display: flex;
  align-items: center;
  background-color: black;
  border-radius: 3px;
  padding: 5px;
  position: fixed;
  top: 53px;
  left: 50%;
  transform: translateX(-50%);

  button {
    padding: 0;
  }
`;

export default EditCtrlBtnsWrap;
