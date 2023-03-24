import styled, { css } from 'styled-components';

interface CalendarProps {
  rowLength: number;
}

const CalendarWrap = ({
  children,
  rowLength,
}: {
  children: React.ReactNode;
  rowLength: number;
}) => {
  return (
    <CalendarWrapBlock rowLength={rowLength}>{children}</CalendarWrapBlock>
  );
};

const CalendarWrapBlock = styled.div`
  width: 67.3992%;
  height: 72.7272%;
  position: absolute;
  /* border: 1px solid black; */
  right: 0;
  bottom: 0;
  z-index: 9;
  right: 3.7851%;
  bottom: 5.3173%;
  display: flex;
  flex-direction: column;
  .row {
    width: 100%;

    ${(props: CalendarProps) =>
      props.rowLength &&
      css`
        height: ${100 / props.rowLength}%;
      `}
    /* border: 1px solid green; */
    display: flex;

    .cell {
      width: 14.2857%;
      /* border: 1px solid yellow; */
      padding: 1%;
      font-size: 35%;
      display: flex;
      flex-direction: column;

      &.disabled {
        opacity: 0;
        pointer-events: none;
      }
      &.red {
        span {
          color: #e64c66;
        }
        .red.txt {
          zoom: 0.7;
        }
      }
      &.on {
        border: 1px solid red;
      }
      .cell_top {
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        margin-bottom: 0.15rem;
      }
      .memo_con {
        font-size: 35%;
        zoom: 0.7;
      }
    }
  }
`;

export default CalendarWrap;
