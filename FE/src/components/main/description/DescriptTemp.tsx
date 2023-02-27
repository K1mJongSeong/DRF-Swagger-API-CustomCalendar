import styled from 'styled-components';

interface DescriptProps {
  number: number;
  title: string;
  imgSrc: string;
  descript: string;
}

const DescriptTemp = ({ number, title, imgSrc, descript }: DescriptProps) => {
  return (
    <DescriptTempBlock>
      <div className={number / 2 === 1 ? 'des_top right' : 'des_top'}>
        <div className="dex_title">
          <span className={number / 2 === 1 ? 'num red' : 'num'}>
            0{number}
          </span>
          {title}
        </div>
        <span className="descript">{descript}</span>
      </div>
      <img src={imgSrc} alt="exaple image" />
      <span className="img_des">
        ※ 해당 이미지는 예시 이미지로 실제 상품과 다릅니다.
      </span>
    </DescriptTempBlock>
  );
};

const DescriptTempBlock = styled.div`
  width: calc(100% - 32px);
  margin: 0 auto;
  .des_top {
    width: 100%;
    margin-bottom: 60px;
    text-align: left;
    &.right {
      text-align: right;
    }
    .dex_title {
      font-weight: 800;
      font-size: 1.125rem;
      .num {
        font-size: 3.312rem;
        margin-right: 7px;
        color: white;
        -webkit-text-stroke: 1px #345087;

        &.red {
          -webkit-text-stroke: 1px #e64c66;
        }
      }
    }
    .descript {
      word-break: keep-all;
      font-size: 0.875rem;
    }
  }
  .img_des {
    font-size: 0.625rem;
  }
`;

export default DescriptTemp;
