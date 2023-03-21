import styled from 'styled-components';

const CropZone = ({ children }: { children: React.ReactNode }) => {
  return <CropZoneBlock>{children}</CropZoneBlock>;
};

const CropZoneBlock = styled.div`
  width: 100%;
  height: 47px;
  position: fixed;
  padding: 0.7rem 1rem;
  bottom: 56px;
  left: 0;
  color: white;
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;

  .select_mode_wrap {
    display: flex;
    & > label + label {
      margin-left: 0.7rem;
    }
    label {
      input {
        display: none;
      }
      span.txt {
        color: #919191;
      }

      & > input:checked ~ span.txt {
        color: white;
      }
    }
  }
  .crop_btns_wrap {
    display: flex;
    align-items: center;
    margin-left: 2.2rem;
    position: relative;
    white-space: nowrap;
    &::before {
      content: '';
      width: 1px;
      height: 15px;
      background-color: white;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      left: -1.1rem;
    }
  }
`;

export default CropZone;
