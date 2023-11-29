import { Checkbox, styled } from '@wapl/ui';
import { observer } from 'mobx-react-lite';
import { TypeController } from './type-filter-store';

interface ItemProps {
  onClick: () => void;
  isSelected: boolean;
  label: string;
}

const CheckboxFilterListItem = ({ onClick, isSelected, label }: ItemProps) => {
  return (
    <ListItem onClick={onClick}>
      <Checkbox
        sx={{
          '&.Mui-checked': {
            backgroundColor: 'rgba(81, 61, 236, 1)',
          },
        }}
        checked={isSelected}
        checkboxSize={16}
      />
      {label}
    </ListItem>
  );
};

interface Props {
  typeList: any[];
  targetTypeIdSet: Set<any>;
  onChangeSelectedTypeIdFilterSet: (newFilterSet: Set<any>) => void;
  onClose: () => void;
  typeController: TypeController;
}

export const TypeFilterForm = observer(
  ({
    onClose,
    targetTypeIdSet,
    onChangeSelectedTypeIdFilterSet,
    typeList,
    typeController,
  }: Props) => {
    const handleClearFilter = () => {
      onChangeSelectedTypeIdFilterSet(new Set());
    };

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      typeController.updateTypeIdFilterSet(new Set(targetTypeIdSet));
      onClose();
    };

    const isAllTypeIdFilterSelected = targetTypeIdSet.size === typeList.length;

    const toggleAllTypeIdFilter = () => {
      if (isAllTypeIdFilterSelected) {
        onChangeSelectedTypeIdFilterSet(new Set());
        return;
      }
      const TypeIds = typeList.map((Type) => Type.TypeId);
      onChangeSelectedTypeIdFilterSet(new Set(TypeIds));
    };

    return (
      <Form onSubmit={handleSubmit}>
        <ClearButtonBox>
          <ClearButton
            type="button"
            onClick={handleClearFilter}
          >
            {'초기화'}
          </ClearButton>
        </ClearButtonBox>
        <ScrollableBox>
          <CheckboxFilterListItem
            isSelected={isAllTypeIdFilterSelected}
            label="전체"
            onClick={toggleAllTypeIdFilter}
          />
          {typeList.map((Type) => (
            <CheckboxFilterListItem
              key={Type.TypeId}
              isSelected={targetTypeIdSet.has(Type.TypeId)}
              label={Type.TypeName}
              onClick={() => {
                const newFilterSet = new Set(targetTypeIdSet);
                if (newFilterSet.has(Type.TypeId)) {
                  newFilterSet.delete(Type.TypeId);
                } else {
                  newFilterSet.add(Type.TypeId);
                }
                onChangeSelectedTypeIdFilterSet(newFilterSet);
              }}
            />
          ))}
        </ScrollableBox>
        <SubmitButtonBox>
          <SubmitButton
            type="submit"
            disabled={targetTypeIdSet.size === 0}
          >
            {'적용'}
          </SubmitButton>
        </SubmitButtonBox>
      </Form>
    );
  }
);

const ListItem = styled.li`
  list-style: none;
  height: 36px;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  column-gap: 8px;
  cursor: pointer;
  font-size: 13px;
  line-height: 16px;
  &:hover {
    background-color: rgba(0, 0, 0, 0.04);
  }
`;

const ClearButton = styled.button`
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

const ClearButtonBox = styled.div`
  padding: 12px 20px 8px 20px;
`;

const SubmitButtonBox = styled.div`
  padding: 20px;
`;

const SubmitButton = styled.button`
  width: 100%;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  cursor: pointer;
  background-color: rgba(32, 24, 131, 1);
  border: 0;
  border-radius: 6px;
  column-gap: 8px;
  font-weight: 400;
  font-size: 13px;
  line-height: 16px;
  &:disabled {
    background-color: ${({ theme }) => theme.Color.Gray[300]};
    color: ${({ theme }) => theme.Color.Gray[500]};
    cursor: not-allowed;
  }
`;

const Form = styled.form`
  width: 220px;
  display: flex;
  flex-direction: column;
`;

const ScrollableBox = styled.div`
  height: 208px;
  overflow-x: hidden;
  overflow-y: auto;
`;
