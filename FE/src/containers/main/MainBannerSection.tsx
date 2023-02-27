import { SectionBlock } from 'components/common/DefaultTemplate';
import MainBanner from 'components/main/banner';
import SubBanner from 'components/main/banner/SubBanner';

const MainBannerSection = () => {
  return (
    <SectionBlock>
      <MainBanner>
        <SubBanner />
      </MainBanner>
    </SectionBlock>
  );
};

export default MainBannerSection;
