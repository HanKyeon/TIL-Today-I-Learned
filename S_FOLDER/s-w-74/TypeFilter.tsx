import { observer } from 'mobx-react-lite';
import { Icon, styled } from '@wapl/ui';
import { useStore } from '@//Provider';
import { TypeFilterDropdown } from './TypeFilterDropdown';
import { TypeController } from './type-filter-store';

interface Props {
  typeController: TypeController;
}

const RFSTypeFilter = observer(({ typeController }: Props) => {
  const Store = useStore();

  if (Store.TypesRequestStatus === 'loading') {
    return (
      <OpenButton
        type="button"
        disabled
      >
        {'로딩...'}
        <Icon.ArrowBottomLine
          width={16}
          height={16}
        />
      </OpenButton>
    );
  }

  return (
    <TypeFilterDropdown
      typeController={typeController}
      Types={Store.TypeList}
    />
  );
});

export default RFSTypeFilter;

const OpenButton = styled.button`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  cursor: pointer;
  background-color: #fff;
  border: 1px solid #bdc1c6;
  border-radius: 6px;
  column-gap: 8px;
  font-weight: 400;
  font-size: 13px;
  line-height: 16px;
`;
