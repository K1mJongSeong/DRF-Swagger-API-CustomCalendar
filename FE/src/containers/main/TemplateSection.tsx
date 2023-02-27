import { SectionBlock } from 'components/common/DefaultTemplate';
import Template from 'components/main/template';
import styled from 'styled-components';

const TemplateSection = ({
  nansu,
  templateRef,
}: {
  nansu?: string;
  templateRef: React.RefObject<HTMLDivElement>;
}) => {
  return (
    <StyledSection ref={templateRef}>
      <h2>템플릿 선택</h2>
      <Template
        tempBg="/assets/images/temp_renault_bg.png"
        tempTitle="2023 르노코리아"
        nansu={nansu}
      />
    </StyledSection>
  );
};

const StyledSection = styled(SectionBlock)`
  margin-bottom: 130px;
  display: flex;
  flex-direction: column;
  align-items: center;

  h2 {
    font-size: 1.125rem;
    margin-bottom: 19px;
  }
`;

export default TemplateSection;
