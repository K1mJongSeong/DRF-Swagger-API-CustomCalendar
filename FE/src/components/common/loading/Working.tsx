import styled, { keyframes } from 'styled-components';
import { BsGear } from 'react-icons/bs';

const WorkingLoading = () => {
  return (
    <WorkingLoadingBlock>
      <BsGear />
      페이지 저장중입니다.
      <br />
      잠시만 기다려주세요.
    </WorkingLoadingBlock>
  );
};

const Rotate = keyframes`
    0%{transform: rotate(0)};
    100%{transform: rotate(360deg)};
`;

const WorkingLoadingBlock = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: #120d0d;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  position: fixed;
  top: 0;
  left: 0;
  color: white;
  z-index: 9999;
  text-align: center;
  line-height: 1.5rem;

  svg {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    animation: ${Rotate} infinite 3s;
    transition: all 0.5s;
  }
`;

export default WorkingLoading;
