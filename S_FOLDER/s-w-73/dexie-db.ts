import Dexie, { Table } from 'dexie';
import {
  applyEncryptionMiddleware,
  cryptoOptions,
  clearAllTables,
  clearEncryptedTables,
} from 'dexie-encrypted';

export interface RoomListRes {
  // Room
  roomId: number;
  roomName: string;
  roomProfileImagePath: string;
  roomDescription: string;
  roomEmail: string;
  maxPersonaCount: number;
  personaCount: number;
  isEntryRequestApprovable: boolean;
  isEntryPossible: boolean;
  isSearchable: boolean;
  roomLink: string;
  regiPersonaId: number;
  modiPersonaId: number;
  regiDate: string;
  modiDate: string;

  // RoomType
  roomTypeId: number;
  roomTypeName: string;
  description: string;
  capacityLimitStatus: number;
  capacityLimitDefault: number;
  entryMode: number;
  isNonLoginAccessible: boolean;
  isCreatorRoleRetained: boolean;
  isExternalAccessible: boolean;
  isKeepEmpty: boolean;
  profileEditableMode: number;
  isPublicStatusModifiable: boolean;
  publicStatusDefault: boolean;
  roomInfoDisclosureType: number;
  hasRoomEmail: boolean;
  isSystem: boolean;
  isRoomBookmark: boolean;
}

interface DBCons {
  iv?: any;
  dbName?: string;
  version?: number;
  scheme?: {
    [tableName: string]: string;
  };
}

interface KeyDBScheme {
  customId: number;
  buffer: ArrayBufferLike; // 32 길이 for Dexie
  key: CryptoKey; // 크립토 키
  cBuffer: ArrayBufferLike; // 32길이 for key
  // cryptogram: ArrayBuffer; // 크립팅된 값
}

export class KeyIDB extends Dexie {
  keyStore: Table<KeyDBScheme>;
  isDevelop: boolean;

  constructor({ dbName = 'customIDB', version = 1 }) {
    super(dbName);
    this.version(version).stores({
      keyStore: 'customId',
    });
    this.isDevelop =
      process.env.NODE_ENV &&
      process.env.NODE_ENV.trim().toLowerCase() == 'production'
        ? false
        : true;
    console.log(this.isDevelop ? 'Dev Mode' : 'Prod Mode');
  }
}

export const keyDB = new KeyIDB({ dbName: 'customKIDB' });

export const getKey = async function (customId: number) {
  try {
    const { buffer, key, cBuffer } = await keyDB.keyStore.get({ customId });
    if (!buffer) throw new Error('키가 없는데요');
    const decryptedKey = await crypto.subtle.decrypt(
      { name: 'AES-GCM', iv: cBuffer },
      key,
      buffer
    );
    console.log('암호화된 키', new Uint8Array(buffer));
    console.log('암복호화에 필요한 키', cBuffer);
    console.log('복호화된 키', new Uint8Array(decryptedKey));
    return new Uint8Array(decryptedKey);
  } catch (e) {
    const uintForDexie = crypto.getRandomValues(new Uint8Array(32));
    const uintForCrypto = crypto.getRandomValues(new Uint8Array(32));
    const newKey = await crypto.subtle.generateKey(
      { name: 'AES-GCM', length: 256 },
      false,
      ['encrypt', 'decrypt']
    );
    const encryptedKey = await crypto.subtle.encrypt(
      { name: 'AES-GCM', iv: uintForCrypto },
      newKey,
      uintForDexie
    );
    console.log('암호화된 new 키', new Uint8Array(encryptedKey));
    console.log('암복호화에 필요한 키', uintForCrypto);
    console.log('db 접근에 필요한 키', uintForDexie);
    await keyDB.table('keyStore').add({
      customId,
      key: newKey,
      buffer: encryptedKey,
      cBuffer: uintForCrypto,
    });
    return new Uint8Array(uintForDexie);
  }
};

interface DBConsProps {
  iv: Uint8Array;
  storeName: string;
  dbName?: string;
  version?: number;
  scheme: {
    [tableName: string]: string;
  };
}

export class CustomIDB extends Dexie {
  isDevelop: boolean;
  iv: Uint8Array;

  constructor({
    iv,
    storeName,
    dbName = 'customIDB',
    version = 1,
    scheme,
  }: DBConsProps) {
    super(dbName);
    this.iv = iv;
  }
}

export class DexieWrapper {
  idb: CustomIDB;
  constructor(dbCons: DBConsProps) {
    this.idb = new CustomIDB(dbCons);
    // applyEncryptionMiddleware(this.idb, this.idb.iv, )
  }
}

class TestDB extends Dexie {
  isDevelop: boolean;
  iv: Uint8Array;
  friends: Table<{
    name: string;
    age: number;
    street: string;
    picture: string;
  }>;

  constructor({ iv, dbName = 'customIDB', version = 1, scheme }: DBCons) {
    super(dbName);
    this.iv = iv;
  }
}

const db = new TestDB({});

export const makeDexieEncrypt = async function (key: Uint8Array, version = 1) {
  applyEncryptionMiddleware<typeof db>(
    db,
    key,
    {
      friends: cryptoOptions.NON_INDEXED_FIELDS,
    },
    async (db) => {
      console.log('클리어 올 테이블');
      return clearAllTables(db);
    }
  );

  db.version(version).stores({
    friends: 'name',
  });
};

export const addDexieData = async function (key: Uint8Array) {
  const friend = {
    name: '한기현',
    age: 28,
    street: '용광로',
    picture: '꺄르륵.png',
  };
  makeDexieEncrypt(key);
  await db.open();
  await db.friends.add(friend);
  console.log('인덱스 디비 상태', db);
  console.log(
    '인덱스 디비에 접근해보기',
    await db.friends.get({ name: '한기현' })
  );
  db.close();
};

export const testDexieEncrypt = async function (key: Uint8Array) {
  makeDexieEncrypt(key);
  await db.open();
  const data = await db.friends.get({ name: '한기현' });
  console.log(data);
  db.close();
  return data;
};

class RoomListIDB extends Dexie {
  roomList: Table<RoomListRes>;
  isDevelop: boolean;
  iv: Uint8Array;

  constructor({ iv, dbName = 'customIDB', version = 1, scheme }: DBCons) {
    super(dbName);
    this.version(version).stores({
      roomList: 'roomId',
    });
    if (!iv) {
      console.log('iv 없음');
    } else {
      this.iv = iv;
    }
    this.isDevelop =
      process.env.NODE_ENV &&
      process.env.NODE_ENV.trim().toLowerCase() == 'production'
        ? false
        : true;
    console.log(this.isDevelop ? 'Dev Mode' : 'Prod Mode');
  }
}
