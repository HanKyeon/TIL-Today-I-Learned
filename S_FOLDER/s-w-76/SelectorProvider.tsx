// provider 사용 방법 및 방식

import { PropsWithChildren, createContext, useContext } from 'react';
import { SelectorStore } from './selector-store';

interface Props {
  someValue: number;
}

const SelectorContext = createContext<SelectorStore>(new SelectorStore());

export const SelectorProvider = ({
  children,
  someValue,
}: PropsWithChildren<Props>) => {
  if (!someValue) {
    return <div>요구 값 없음</div>;
  }
  return (
    <SelectorContext.Provider value={new SelectorStore(someValue)}>
      {children}
    </SelectorContext.Provider>
  );
};

export const useSelectorStore = (): SelectorStore => {
  const selectorContext = useContext(SelectorContext);
  if (!selectorContext) {
    throw new Error('<SelectorProvider>가 요구됩니다.');
  }
  return selectorContext;
};
