import React from 'react';
import styled from 'styled-components';

const EditorTemplate = ({ children }: { children: React.ReactNode }) => {
  return <EditorTemplateBlock>{children}</EditorTemplateBlock>;
};

const EditorTemplateBlock = styled.div`
  width: 100%;
  height: 100%;
  background-color: #ccc;
  display: flex;
  align-items: center;
  justify-content: center;

  .swiper-button-next:after,
  .swiper-button-prev:after {
    color: white;
  }
`;

export default React.memo(EditorTemplate);
