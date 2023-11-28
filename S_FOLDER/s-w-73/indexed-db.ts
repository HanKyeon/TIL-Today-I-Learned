import {
  openDB,
  deleteDB,
  unwrap,
  wrap,
  IDBPDatabase,
  OpenDBCallbacks,
  DeleteDBCallbacks,
  StoreNames,
  StoreKey,
  StoreValue,
} from 'idb';

interface StoreScheme {
  storeName: string;
  keyPath: string;
  values?: any[];
  indexDatas?: {
    name?: string;
    options?: { multiEntry?: boolean; unique?: boolean };
  }[];
}

export class CustomIndexedDB<DBType = unknown> {
  db: IDBPDatabase<DBType>;
  constructor(
    name: string,
    version?: number,
    callbacks?: OpenDBCallbacks<DBType>
  ) {
    this.init(name, version, callbacks);
  }

  async init(
    name: string,
    version?: number,
    callbacks?: OpenDBCallbacks<DBType>
  ) {
    this.db = await openDB(name, version, callbacks);
  }

  async deleteDB(name: string, callbacks?: DeleteDBCallbacks) {
    deleteDB(name, callbacks);
  }

  async get(
    storeName: StoreNames<DBType>,
    key: IDBKeyRange | StoreKey<DBType, StoreNames<DBType>>
  ) {
    const res = await this.db.get(storeName, key);
    return res;
  }
  async set(
    storeName: StoreNames<DBType>,
    value: StoreValue<DBType, StoreNames<DBType>>,
    key: IDBKeyRange | StoreKey<DBType, StoreNames<DBType>>
  ) {
    const res = await this.db.put(storeName, value, key);
    return res;
  }
}

const testData: StoreScheme[] = [
  {
    storeName: 'testStore',
    keyPath: 'id',
    indexDatas: [
      { name: 'id', options: { unique: true } },
      { name: 'name', options: { unique: false } },
      { name: 'description', options: { unique: false } },
    ],
    values: [
      { id: 1, name: '한기현', description: '설명1' },
      { id: 2, name: '두기현', description: '설명2' },
      { id: 3, name: '세기현', description: '설명3' },
      { id: 4, name: '네기현', description: '설명4' },
      { id: 5, name: '설기현', description: '설명5' },
    ],
  },
  // {
  //   storeName: 'storeThatSameAsTestStore',
  //   keyPath: 'id',
  //   indexDatas: [
  //     { name: 'id', options: { unique: true } },
  //     { name: 'name', options: { unique: false } },
  //     { name: 'description', options: { unique: false } },
  //   ],
  //   values: [
  //     { id: 1, name: '한견', description: '설명1' },
  //     { id: 2, name: '두견', description: '설명2' },
  //     { id: 3, name: '세견', description: '설명3' },
  //     { id: 4, name: '네견', description: '설명4' },
  //     { id: 5, name: '설견', description: '설명5' },
  //   ],
  // },
];

export class CustomIDB {
  CustomIDB: IDBDatabase;
  dbName: string;
  version: number;

  constructor(
    dbName = 'CustomIDB',
    version = 1,
    stores = testData // ?: StoreScheme[]
  ) {
    this.dbName = dbName;
    this.version = version;
    if (!('indexedDB' in window)) {
      console.warn("This browser doesn't support IndexedDB");
      throw "This browser doesn't support IndexedDB";
    }
    const openReq = indexedDB.open(dbName, version);
    openReq.onsuccess = (e) => {
      console.log('Open CustomIDB success in constructor : ', e);
      this.CustomIDB = openReq.result;
    };
    openReq.onerror = (e) => {
      console.error('Open CustomIDB error in constructor : ', e);
    };
    openReq.onupgradeneeded = (e) => {
      console.warn('Open CustomIDB upgrade needed in constructor : ', e);
      this.CustomIDB = openReq.result;

      stores?.forEach(({ storeName, keyPath, values, indexDatas }) => {
        const objectStore = this.CustomIDB.createObjectStore(storeName, {
          keyPath,
        });

        indexDatas.forEach(({ name, options }) => {
          console.log('스토어에 인덱스 추가', storeName, name);
          objectStore.createIndex(name, name, options);
        });

        objectStore.transaction.oncomplete = (e) => {
          const indexStore = this.CustomIDB.transaction(
            storeName,
            'readwrite'
          ).objectStore(storeName);
          values.forEach((data) => {
            console.log('스토어에 데이터 추가', storeName, data);
            indexStore.add(data);
          });
        };
      });
    };

    openReq.onblocked = (e) => {
      console.warn('Open CustomIDB blocked in constructor : ', e);
    };
  }

  async getElement<Res>(targetStoreName: string, key: 'all' | any) {
    const openReq = indexedDB.open(this.dbName, this.version);
    return new Promise<Res>((resolve, reject) => {
      openReq.onsuccess = () => {
        let request!: IDBRequest;
        this.CustomIDB = openReq.result;
        if (
          Array.from(this.CustomIDB.objectStoreNames).find(
            (name) => name === targetStoreName
          )
        ) {
          const transaction = this.CustomIDB.transaction(targetStoreName);
          const objectStore = transaction.objectStore(targetStoreName);

          if (key === 'all') request = objectStore.getAll();
          else request = objectStore.get(key);
          request.onerror = (e) => {
            console.error('CustomIDB get Error: ', request.error);
            reject(request.error);
          };
          request.onsuccess = (e) => {
            console.log('CustomIDB get success: ', request.result);
            resolve(request.result);
          };
          transaction.oncomplete = () => this.CustomIDB.close();
        } else {
          indexedDB.deleteDatabase(this.dbName);
        }
      };
    });
  }

  async addElement(targetStoreName: string, payload: any) {
    const openReq = indexedDB.open('data');
    return new Promise<boolean>((resolve, reject) => {
      openReq.onsuccess = () => {
        this.CustomIDB = openReq.result;
        if (
          Array.from(this.CustomIDB.objectStoreNames).find(
            (name) => name === targetStoreName
          )
        ) {
          const transaction = this.CustomIDB.transaction(
            targetStoreName,
            'readwrite'
          );
          const objectStore = transaction.objectStore(targetStoreName);
          const serialized = payload;
          const request = objectStore.add(serialized);
          request.onerror = () => {
            console.error(request.error);
            reject(false);
          };
          transaction.oncomplete = () => {
            this.CustomIDB.close();
            resolve(true);
          };
        } else {
          indexedDB.deleteDatabase('data');
          reject(false);
        }
      };
    });
  }

  async editElement<T>(targetStoreName: string, key: string, payload: object) {
    const openReq = indexedDB.open('data');
    return new Promise<T>((resolve, reject) => {
      openReq.onsuccess = () => {
        let request: IDBRequest;
        this.CustomIDB = openReq.result;
        if (
          Array.from(this.CustomIDB.objectStoreNames).find(
            (name) => name === targetStoreName
          )
        ) {
          const transaction = this.CustomIDB.transaction(
            targetStoreName,
            'readwrite'
          );
          const objectStore = transaction.objectStore(targetStoreName);
          if (key === 'all') request = objectStore.getAll();
          else request = objectStore.get(key);
          request.onerror = (e) => {
            console.error('CustomIDB Get Error: ', e);
            reject(request.error);
          };
          request.onsuccess = () => {
            const serialized = payload;
            const updateRequest = objectStore.put(serialized);
            updateRequest.onsuccess = () => resolve(request.result);
          };
          transaction.oncomplete = () => this.CustomIDB.close();
        } else {
          indexedDB.deleteDatabase('data');
        }
      };
    });
  }

  removeElement = (targetStoreName: string, key: string) => {
    const openReq = indexedDB.open('data');
    openReq.onsuccess = () => {
      let request: IDBRequest;
      this.CustomIDB = openReq.result;
      if (
        Array.from(this.CustomIDB.objectStoreNames).find(
          (name) => name === targetStoreName
        )
      ) {
        const transaction = this.CustomIDB.transaction(
          targetStoreName,
          'readwrite'
        );
        const objectStore = transaction.objectStore(targetStoreName);
        if (key === 'all') request = objectStore.clear();
        else request = objectStore.delete(key);
        request.onerror = () => console.error(request.error);
        transaction.oncomplete = () => this.CustomIDB.close();
      } else {
        indexedDB.deleteDatabase('data');
      }
    };
  };
}
