import { SectionBlock } from 'components/common/DefaultTemplate';
import DescriptTemp from 'components/main/description/DescriptTemp';

const DescriptSections = () => {
  return (
    <>
      <FirstSection />
      <SecondSection />
    </>
  );
};

const FirstSection = () => {
  return (
    <SectionBlock>
      <DescriptTemp
        number={1}
        title={'유일한, 특별한'}
        imgSrc="/assets/images/des_bn_01.png"
        descript="나만의 소중한 사진들로 특별한 달력을 만들어 보세요."
      />
    </SectionBlock>
  );
};
const SecondSection = () => {
  return (
    <SectionBlock>
      <DescriptTemp
        number={2}
        title={'쉽고 편리한 에디터'}
        imgSrc="/assets/images/des_bn_02.png"
        descript="간편한 편의성과 직관적인 UI의 에디터를 사용해 보세요."
      />
    </SectionBlock>
  );
};

export default DescriptSections;
