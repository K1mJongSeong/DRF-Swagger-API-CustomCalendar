import styled from 'styled-components';

const SubBanner = () => {
  return (
    <SubBannerBlock>
      <h2>나만의 달력을 만들어 보세요!</h2>
      <img src="/assets/images/sub_bn.png" alt="sub banner" />
      <span>※ 해당 이미지는 예시 이미지로 실제 상품과 다릅니다.</span>
    </SubBannerBlock>
  );
};

const SubBannerBlock = styled.div`
  width: calc(100% - 32px);
  max-width: 430px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translate(-50%, 0);
  padding: 17px 1rem 20px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  word-break: keep-all;
  h2 {
    font-size: 1.125rem;
    margin-bottom: 10px;
  }
  img {
    margin-bottom: 3px;
  }
  span {
    width: 100%;
    font-size: 0.625rem;
  }
`;

export default SubBanner;
