import styled from 'styled-components';

const VisibleBackLoading = () => {
  return (
    <VisibleBackLoadingBlock>
      <img src="/assets/images/logo_white.png" alt="logo" />
    </VisibleBackLoadingBlock>
  );
};

const VisibleBackLoadingBlock = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 99;
`;

export default VisibleBackLoading;
