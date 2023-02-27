import styled from 'styled-components';

const MainBanner = ({ children }: { children: React.ReactNode }) => {
  return (
    <MainBannerBlock>
      <div className="main_bn">
        <div className="banner_txt bg_blur">
          <p>소중한 추억으로 기억하기</p>
          <h2>
            상상 이상의 자유로움,
            <br />
            MAKE CALENDAR
          </h2>
          <img src="/assets/images/logo_white.png" alt="logo" />
        </div>
        <img src="/assets/images/main_bn.jpg" alt="main banner" />
      </div>
      {children}
    </MainBannerBlock>
  );
};

const MainBannerBlock = styled.div`
  width: 100%;
  position: relative;
  min-height: 682px;
  max-height: 682px;
  .main_bn {
    width: 100%;
    max-height: 500px;
    overflow: hidden;
    position: relative;
    border-radius: 0 0 8px 8px;

    .banner_txt {
      width: 100%;
      height: 100%;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      color: white;
      background-color: rgba(0, 0, 0, 0.5);
      word-break: keep-all;
      padding-top: 104px;
      p {
        font-size: 0.875rem;
      }
      h2 {
        font-size: 1.5rem;
      }
      img {
        margin-top: 1rem;
      }
    }
  }
`;

export default MainBanner;
