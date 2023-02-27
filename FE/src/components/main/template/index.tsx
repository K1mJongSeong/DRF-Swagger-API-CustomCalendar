import Button from 'components/common/Button';
import styled from 'styled-components';

const Template = ({
  tempBg,
  tempTitle,
  nansu,
}: {
  tempBg: string;
  tempTitle: string;
  nansu?: string;
}) => {
  return (
    <TemplateBlock>
      <img src={tempBg} alt="template background image" />
      <span className="descript">
        ※ 해당 이미지는 예시 이미지로 실제 상품과 다릅니다.
      </span>
      <h3>{tempTitle}</h3>
      <Button to={`/${nansu}/list?temp=${tempTitle}`} $red>
        달력 만들기
      </Button>
    </TemplateBlock>
  );
};

const TemplateBlock = styled.div`
  width: calc(100% - 32px);
  padding: 20px 16px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  margin: 0 auto;

  & + & {
    margin-top: 50px;
  }
  img {
    margin-bottom: 6px;
  }

  .descript {
    font-size: 0.625rem;
    margin-bottom: 15px;
    display: flex;
  }
  h3 {
    font-size: 1rem;
    margin-bottom: 1rem;
    text-align: center;
  }
`;

export default Template;
