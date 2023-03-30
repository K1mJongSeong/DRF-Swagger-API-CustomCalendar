import styled from 'styled-components';

const DefaultTemplate = ({ children }: { children: React.ReactNode }) => {
  return <DefaultTemplateBlock>{children}</DefaultTemplateBlock>;
};

const DefaultTemplateBlock = styled.div`
  width: 100%;
  max-width: 1024px;
  min-height: 100%;
  overflow-y: auto;
  background-color: white;
  position: relative;
  margin: 0 auto;
`;

export const SectionBlock = styled.div`
  width: 100%;
  & + & {
    margin-top: 50px;
  }
`;

export default DefaultTemplate;
