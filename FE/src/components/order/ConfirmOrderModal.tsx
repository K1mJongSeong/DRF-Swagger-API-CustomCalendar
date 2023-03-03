import Button from 'components/common/Button';
import styled from 'styled-components';

const ConfirmOrderModal = ({
  close,
  submit,
}: {
  close: () => void;
  submit?: () => void;
}) => {
  return (
    <ConfirmOrderModalBlock>
      <div className="modal_con">
        <p>
          주문이 완료되면
          <br />
          수정 및 재주문이 불가능합니다.
          <br />
          입력하신 정보로 주문을 하시겠습니까?
        </p>
        <div className="btns_wrap">
          <Button $gray onClick={close}>
            취소
          </Button>
          <Button $blue onClick={submit}>
            확인
          </Button>
        </div>
      </div>
    </ConfirmOrderModalBlock>
  );
};

const ConfirmOrderModalBlock = styled.div`
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  .modal_con {
    width: calc(100% - 32px);
    max-width: 328px;
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    p {
      margin-bottom: 30px;
    }
    .btns_wrap {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      button {
        min-height: 30px;
      }
      & > button + button {
        margin-left: 13px;
      }
    }
  }
`;

export default ConfirmOrderModal;
