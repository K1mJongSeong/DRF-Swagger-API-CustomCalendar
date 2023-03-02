import OrderTemplate, {
  StyledInput,
  StyledSearchBtn,
} from 'components/order/OrderTemplate';
import { PostCodeProps } from 'interface/order';
import { useState } from 'react';
import { useDaumPostcodePopup } from 'react-daum-postcode';

const OrderFormSection = () => {
  const [address, setAddress] = useState<string>('');
  const [postCode, setPostCode] = useState<string>('');

  const open = useDaumPostcodePopup();

  const handleComplete = (data: PostCodeProps) => {
    console.log(data);
    let fullAddress = data.address;
    const zoneCode = data.zonecode;
    let extraAddress = '';

    if (data.addressType === 'R') {
      if (data.bname !== '') {
        extraAddress += data.bname;
      }
      if (data.buildingName !== '') {
        extraAddress +=
          extraAddress !== '' ? `, ${data.buildingName}` : data.buildingName;
      }
      fullAddress += extraAddress !== '' ? ` (${extraAddress})` : '';
    }

    console.log(fullAddress); // e.g. '서울 성동구 왕십리로2길 20 (성수동1가)'
    console.log(zoneCode);
    setAddress(fullAddress);
    setPostCode(zoneCode);
  };

  const handleClickOpenPopup = (e: React.MouseEvent<HTMLElement>) => {
    e.preventDefault();
    open({ onComplete: handleComplete });
  };
  return (
    <OrderTemplate title="주문접수">
      <form>
        <label>성명</label>
        <StyledInput
          autoComplete="name"
          placeholder="주문자 성명을 입력해주세요."
        />
        <label>연락처</label>
        <StyledInput
          autoComplete="phone_num"
          type="number"
          placeholder="- 없이 연락처를 입력해주세요."
        />
        <label>주소</label>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <StyledInput
            autoComplete="postCode"
            placeholder="유편번호"
            value={postCode ? postCode : ''}
            readOnly
          />
          <StyledSearchBtn onClick={handleClickOpenPopup}>검색</StyledSearchBtn>
        </div>
        <StyledInput
          autoComplete="address"
          placeholder="도로명(ex: 서울시 금천구 디지털로)"
          value={address ? address : ''}
          readOnly
        />
        <StyledInput placeholder="상세주소를 입력해주세요." />
      </form>
    </OrderTemplate>
  );
};

export default OrderFormSection;
