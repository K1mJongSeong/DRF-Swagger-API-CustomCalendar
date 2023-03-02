import OrderTemplate, {
  StyledInput,
  StyledSearchBtn,
} from 'components/order/OrderTemplate';
import { useAppDispatch, useAppSelector } from 'hooks';
import { PostCodeProps } from 'interface/order';
import { useDaumPostcodePopup } from 'react-daum-postcode';
import { changeFieldOrderForm } from 'reducer/order';
import { RootState } from 'store';

const OrderFormSection = () => {
  const { orderInfo } = useAppSelector((state: RootState) => state.order);
  const dispatch = useAppDispatch();

  const { userName, userPhone, postCode, address, detailAddress } = orderInfo;

  const handleChangeOrderFormField = (
    e: React.ChangeEvent<HTMLInputElement>,
  ) => {
    const { value, name } = e.target;
    const numCheck = /^[0-9]+$/;

    if (name === 'userPhone' && !numCheck.test(value))
      return alert('숫자만 입력하세요.');

    dispatch(
      changeFieldOrderForm({
        key: name,
        value,
      }),
    );
  };

  const open = useDaumPostcodePopup();

  const handleComplete = (data: PostCodeProps) => {
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

    dispatch(
      changeFieldOrderForm({
        key: 'address',
        value: fullAddress,
      }),
    );
    dispatch(
      changeFieldOrderForm({
        key: 'postCode',
        value: zoneCode,
      }),
    );
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
          name="userName"
          autoComplete="name"
          placeholder="주문자 성명을 입력해주세요."
          value={userName ? userName : ''}
          onChange={handleChangeOrderFormField}
        />
        <label>연락처</label>
        <StyledInput
          name="userPhone"
          autoComplete="phone_num"
          placeholder="- 없이 연락처를 입력해주세요."
          value={userPhone ? userPhone : ''}
          onChange={handleChangeOrderFormField}
        />
        <label>주소</label>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <StyledInput
            name="postCode"
            autoComplete="postCode"
            placeholder="유편번호"
            value={postCode ? postCode : ''}
            onChange={handleChangeOrderFormField}
            readOnly
          />
          <StyledSearchBtn onClick={handleClickOpenPopup}>검색</StyledSearchBtn>
        </div>
        <StyledInput
          name="address"
          autoComplete="address"
          placeholder="도로명(ex: 서울시 금천구 디지털로)"
          value={address ? address : ''}
          onChange={handleChangeOrderFormField}
          readOnly
        />
        <StyledInput
          name="detailAddress"
          placeholder="상세주소를 입력해주세요."
          onChange={handleChangeOrderFormField}
          value={detailAddress ? detailAddress : ''}
        />
      </form>
    </OrderTemplate>
  );
};

export default OrderFormSection;
