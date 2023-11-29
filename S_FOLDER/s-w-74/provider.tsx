import { createContext, useContext, useState, ReactNode } from 'react';
import { RoomSettingUIStore } from './RoomSettingUIStore';

interface Props {
  children: ReactNode;
}

const StoreContext = createContext<RoomSettingUIStore | null>(null);

export const StoreProvider = ({ children }: Props) => {
  const [contextStore] = useState(() => new RoomSettingUIStore());
  return (
    <StoreContext.Provider value={contextStore}>
      {children}
    </StoreContext.Provider>
  );
};

export const useRoomSettingUIStore = (): RoomSettingUIStore => {
  const contextStore = useContext(StoreContext);
  if (!contextStore) {
    throw new Error('useSettingUIStore has to be used within <StoreProvider>');
  }
  return contextStore;
};
