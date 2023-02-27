import styled from 'styled-components';

const Loading = () => {
  return (
    <LoadingBlock>
      <img src="/assets/images/logo.png" alt="logo" />
    </LoadingBlock>
  );
};
const LoadingBlock = styled.div`
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  position: fixed;
  top: 0;
  left: 0;

  img {
    width: calc(100% - 32px);
    max-width: 131px;
  }
`;

export default Loading;
