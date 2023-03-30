import styled from 'styled-components';
import { MdArrowForwardIos } from 'react-icons/md';
import { Link, useLocation, useParams } from 'react-router-dom';
import { Renault } from 'data/template/renault';
import { useAppSelector } from 'hooks';
import { RootState } from 'store';

interface ItemProps {
  item: {
    id: number;
    tempSrc: string;
    name: string;
    ctrlItems?: {
      cId: number;
      w: string;
      h: string;
      t: string;
      l: string;
    }[];
    pageName?: string;
  };
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
  const location = useLocation();
  const param = useParams();
  const { nansu } = param;
  const { search } = location;

  const { savedPages } = useAppSelector((state: RootState) => state.page);

  const hasWorks = savedPages.length > 0 && item.ctrlItems;
  const isWorkPage = item.pageName && savedPages.includes(item.pageName);

  return (
    <li className="item">
      <Link to={`/${nansu}/editor${search}&page=${item.id}`}>
        <b>
          {item?.name}
          {hasWorks && (
            <span className={isWorkPage ? 'blue' : 'red'}>
              [{isWorkPage ? '완료' : '수정'}]
            </span>
          )}
        </b>
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

      span {
        margin-left: 0.3rem;
        &.red {
          color: #e64c66;
        }
        &.blue {
          color: #495bff;
        }
      }
    }
  }
`;

export default TempList;
