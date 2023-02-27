import styled from 'styled-components';
import { MdArrowForwardIos } from 'react-icons/md';
import { Link } from 'react-router-dom';
import { Renault } from 'data/template/renault';

interface ItemProps {
  item: { id: number; tempSrc: string; name: string };
}

const TempList = () => {
  return (
    <TempListBlock>
      {Renault?.map((item) => (
        <TempItem key={item?.id} item={item} />
      ))}
    </TempListBlock>
  );
};

const TempItem = ({ item }: ItemProps) => {
  return (
    <li className="item">
      <Link to="/난수/editor">
        {item?.name}
        <MdArrowForwardIos />
      </Link>
    </li>
  );
};

const TempListBlock = styled.ul`
  width: 100%;
  height: 100%;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 8px;

  .item {
    width: 100%;
    border-bottom: 1px solid #ccc;
    transition: all 0.2s;
    &:hover {
      background-color: #eee;
    }

    a {
      display: flex;
      justify-content: space-between;
      padding: 20px;
      font-weight: 800;
    }
  }
`;

export default TempList;
