import React from 'react';
import styled from 'styled-components';

const EditorTop = ({ children }: { children: React.ReactNode }) => {
  return <EditorTopBlock>{children}</EditorTopBlock>;
};

const EditorTopBlock = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #312b2b;
  padding: 16px;
  border-bottom: 1px solid #ccc;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 99;

  .right {
    display: flex;
    align-items: center;
  }
`;

export default React.memo(EditorTop);
