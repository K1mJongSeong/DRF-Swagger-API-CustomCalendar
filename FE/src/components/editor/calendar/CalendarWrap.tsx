import styled from 'styled-components';

const CalendarWrap = () => {
  return <CalendarWrapBlock></CalendarWrapBlock>;
};

const CalendarWrapBlock = styled.div`
  width: 67.3992%;
  height: 72.7272%;
  position: absolute;
  border: 1px solid black;
  right: 0;
  bottom: 0;
  z-index: 9;
  right: 3.7851%;
  bottom: 5.3173%;
  display: flex;
  flex-direction: column;
  .row {
    width: 100%;
    height: 20%;
    border: 1px solid green;
  }
`;

export default CalendarWrap;
