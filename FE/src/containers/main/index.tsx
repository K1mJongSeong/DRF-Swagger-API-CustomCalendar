import FixedButton from 'components/main/FixedButton';
import { useRef } from 'react';
import { useParams } from 'react-router';
import DescriptSections from './DescriptSections';
import MainBannerSection from './MainBannerSection';
import TemplateSection from './TemplateSection';

const MainContainer = () => {
  const param = useParams();
  const { nansu } = param;
  const templateRef = useRef<HTMLDivElement>(null);
  const handleClickToTemp = () => {
    templateRef.current?.scrollIntoView({ behavior: 'smooth' });
  };
  return (
    <>
      <MainBannerSection />
      <DescriptSections />
      <TemplateSection nansu={nansu} templateRef={templateRef} />
      <FixedButton nansu={nansu} onClick={handleClickToTemp} />
    </>
  );
};

export default MainContainer;
