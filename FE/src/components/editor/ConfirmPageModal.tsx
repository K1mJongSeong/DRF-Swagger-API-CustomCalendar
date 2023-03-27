import Button from 'components/common/Button';
import styled from 'styled-components';

const ConfirmPageModal = ({
  close,
  submit,
  page,
}: {
  close: () => void;
  submit: () => void;
  page: string | null;
}) => {
  return (
    <ConfirmPageModalBlock>
      <div className="modal_con">
        <p>
          르노코리아 2023, {page}페이지
          <br />
          입력하신 정보를 저장 하시겠습니까?
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
    </ConfirmPageModalBlock>
  );
};

const ConfirmPageModalBlock = styled.div`
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 998;
  .modal_con {
    width: calc(100% - 32px);
    max-width: 328px;
    background-color: white;
    border-radius: 8px;
    padding: 28px 20px 20px;
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

export default ConfirmPageModal;
