import { Icon, styled, Mui } from '@wapl/ui';
import { useEffect, useState } from 'react';
import { observer } from 'mobx-react-lite';
import { RFSTypeFilterForm } from './RFSTypeFilterForm';
import { TypeController } from './type-filter-store';

interface Props {
  Types: Type[];
  typeController: TypeController;
}

function initializeLocalTypeIdFilterSet(Types: Type[]) {
  return new Set(Types.map((Type) => Type.TypeId));
}

export const RFSTypeFilterDropdown = observer(
  ({ Types, typeController }: Props) => {
    const [anchorEl, setAnchorEl] = useState<HTMLButtonElement | null>(null);

    const [localTypeIdFilterSet, setLocalTypeIdFilterSet] = useState(
      initializeLocalTypeIdFilterSet(Types)
    );

    useEffect(() => {
      typeController.updateTypeIdFilterSet(localTypeIdFilterSet);
    }, []);

    const isOpen = Boolean(anchorEl);

    const handleOpen = (e: React.MouseEvent<HTMLButtonElement>) => {
      setAnchorEl(e.currentTarget);
    };

    const handleClose = () => {
      setAnchorEl(null);
    };

    const handleClickOutOfPopover = () => {
      setLocalTypeIdFilterSet(new Set(typeController.TypeIdFilterSet));
      handleClose();
    };

    const firstSelectedTypeName = Types.find((Type) =>
      localTypeIdFilterSet.has(Type.TypeId)
    )?.TypeName;

    const openButtonText = !firstSelectedTypeName
      ? '선택'
      : localTypeIdFilterSet.size === Types.length
      ? '전체'
      : localTypeIdFilterSet.size >= 2
      ? `${firstSelectedTypeName} 외 ${localTypeIdFilterSet.size - 1}`
      : firstSelectedTypeName;

    return (
      <>
        <OpenButton
          type="button"
          onClick={handleOpen}
        >
          {openButtonText}
          {isOpen ? (
            <Icon.ArrowTopLine
              width={16}
              height={16}
            />
          ) : (
            <Icon.ArrowBottomLine
              width={16}
              height={16}
            />
          )}
        </OpenButton>
        <Mui.Popover
          open={isOpen}
          onClose={handleClickOutOfPopover}
          anchorEl={anchorEl}
          anchorOrigin={{
            vertical: 'bottom',
            horizontal: 'left',
          }}
          transformOrigin={{
            vertical: 'top',
            horizontal: 'left',
          }}
          sx={{
            '.MuiPaper-root.MuiPopover-paper': {
              borderRadius: '8px',
              boxShadow: '0px 0px 8px 0px rgba(0, 0, 0, 0.2)',
              marginTop: '8px',
            },
          }}
        >
          <TypeFilterForm
            Types={Types}
            typeController={typeController}
            selectedTypeIdFilterSet={localTypeIdFilterSet}
            onChangeSelectedTypeIdFilterSet={setLocalTypeIdFilterSet}
            onClose={handleClose}
          />
        </Mui.Popover>
      </>
    );
  }
);

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
