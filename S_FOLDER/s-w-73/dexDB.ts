import Dexie, { Table, Collection } from 'dexie';
import {
  ENCRYPT_LIST,
  UNENCRYPTED_LIST,
  NON_INDEXED_FIELDS,
  applyEncryptionMiddleware,
  clearAllTables,
  clearEncryptedTables,
  cryptoOptions,
} from 'dexie-encrypted';
import { encryption } from 'dexie-easy-encrypt';

interface DBCons {
  iv?: any;
  dbName: string;
  version?: number;
  scheme: {
    [tableName: string]: string;
  };
}

export const generageSchemeWithId = function (obj: object) {
  let ret = '';
  Object.keys(obj).forEach(v => {
    v === 'id' ? (ret += `++${v},`) : (ret += `${v},`);
  });
  return ret.substring(0, ret.length - 1);
};

/**
 * sceme은 friends: "++id,name,age" 형태
 */
export class DefaultDB<DataType, DataKeyType = number> extends Dexie {
  // public data!: Table<DataType, DataKeyType>;
  keyStore: Table<DataType, DataKeyType>;
  private isDevelop: boolean;
  iv: Uint8Array;

  constructor({ iv, dbName = 'WaplIDB', version = 1, scheme }: DBCons) {
    // Dexie BoilerPlate
    super(dbName);
    // this.version(version).stores(scheme);
    this.version(version).stores({ keyStore: '++id, key, waplId' });
    // Object.keys(scheme).forEach(schemeKey => {
    //   this[schemeKey] = new Table();
    // });
    if (!iv) {
      console.log('iv 없음');
    } else {
      this.iv = iv;
    }
    // 환경 확인
    this.isDevelop =
      process.env.NODE_ENV &&
      process.env.NODE_ENV.trim().toLowerCase() == 'production'
        ? false
        : true;
    console.log(this.isDevelop ? 'Dev Mode' : 'Prod Mode');
  }
}

// 아래는 키 저장 및 get을 IDB에서 해오는 것

// export const keyDB = new DefaultDB<{
//   id: number;
//   waplId: number;
//   key: Uint8Array;
// }>({
//   dbName: 'WaplKIDB',
//   scheme: { keyStore: '++id,key,waplId' },
// });

// export const getKey = async function (waplId: number) {
//   try {
//     const { key } = await keyDB['keyStore'].get({ waplId });
//     if (key) return key;
//   } catch {
//     const newKey = crypto.getRandomValues(new Uint8Array(32));
//     await keyDB.table('keyStore').add({ waplId, key: newKey });
//     return await keyDB['keyStore'].get({ waplId, key: newKey });
//   }
// };

// async function encryptWithAESKey() {
//   iv.current = crypto.getRandomValues(new Uint8Array(16)); // create new iv
//   const encoder = new TextEncoder();
//   const key = (await db.key.limit(1).toArray())[0].key as CryptoKey;
//   const encrypted: ArrayBuffer = await crypto.subtle.encrypt(
//     {
//       name: "AES-CBC",
//       iv: iv.current,
//     },
//     key,
//     encoder.encode(text) // string to bytes
//   );
//   setCryptogram(Buffer.from(new Uint8Array(encrypted)).toString("base64")); // bytes to base64 string
// }

// async function decryptWithAESKey(cryptogram: string) {
//   const decoder = new TextDecoder();
//   const key = (await db.key.limit(1).toArray())[0].key as CryptoKey;
//   const encrypted = Buffer.from(cryptogram, "base64"); // base64 string to bytes
//   const decrypted: ArrayBuffer = await crypto.subtle.decrypt(
//     { name: "AES-CBC", iv: iv.current },
//     key,
//     encrypted
//   );
//   setPlainText(decoder.decode(decrypted));
// }
