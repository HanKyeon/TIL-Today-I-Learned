# indexedDB

- 브라우저 제공 db이다.

- `localstorage`와 비교되는데, 차이점은 아래와 같다.
  1. `localstorage`
  - 적은 양의 데이터를 저장할 때 유용
  - 문자열만 저장 가능. 즉, `JSON.stringify`, `JSON.parse`같은 함수가 필요.
  - 키밸류에 문자열만 가능.
  - 동기적으로 작동
  2. `indexedDB`
  - 많은 양의 구조화된 데이터를 저장할 때 유용.
  - JS가 인식할 수 있는 자료형과 객체를 저장할 수 있다.
  - 키밸류가 문자열이 아니어도 됨.
  - 비동기적으로 작동

## 특징

- Large Scale NoSQL Storage System 으로서 기본 데이터 쿼리와 트랜잭션 지원 => 범용성
- MB 단위부터 GB 까지 디바이스의 스토리지 크기에 따라 대용 량 저장 관리 => 대용량
- same origin policy 를 따르며 , 온라인 오프라인 환경 모두에서 쿼리 지원 => 항상성?
- Transaction Model 을 사용하여 내부 데이터 변경 연산은 트랜잭션을 통해서 일어남 => 규칙적
- Asyncronous API 제공하여 DB 내부 명령 처리에 대한 지연 없음 => async로 작동 가능하여 빠름
- Index Table System 지향하며 , Index 설정으로 효율적인 데이터 검색 지원 => 빠름
- 하나 이상의 DB 와 테이블을 가질 수 있음 => 큼
- Key Value 한 쌍을 저장하며 , File/Blob 포함 다양한 자바스크립트 데이터 타입 지원 => 범용성, 편리함

## 사용법 일부 정리

- 아래처럼 keyPath를 `string[]`로 잡을 경우

```tsx
const objectStore = this.customIDB.createObjectStore('customers', {
  keyPath: ['name', 'email'],
});
```

- `get` 혹은 `set`, `put` 할 때 key를 `string[]` 형태로 제시해야 함.

```tsx
// async하므로 onsuccess 내에서 result에 접근해야만 함.
objectStore.get(['Bill', 'bill@company.com']).result;
```

- 일반 `string`으로 잡을 경우

```tsx
const objectStore = this.customIDB.createObjectStore('customers', {
  keyPath: 'name',
});
```

- `get` 혹은 `set`, `put` 할 때 key를 `string` 형태로 제시해야 함.

```tsx
// async하므로 onsuccess 내에서 result에 접근해야만 함.
objectStore.get('Bill').result;
```

- `keyPath`를 제공하지 않고 `autoIncreament` 역시 제공하지 않을 경우엔 `add` 할 때 `key` 역시 함께 제공해야 한다. 모든 종류의 값이 가능.
- `keyPath`를 제공하고 `autoIncreament`를 제공하지 않는 경우엔 오직 `object` 형태만 포함할 수 있다.
- `keyPath`가 없고, `autoIncreament`를 제공하는 경우엔 모든 종류의 값이 가능하며 키가 자동으로 생성된다. 특정 키 주입 역시 가능
- `keyPath`가 있고, `autoIncreament`를 제공하는 경우는 오직 `object` 형태만 포함 가능. 일반적으로 key가 자동 생성되고, 생성된 키의 값은 키 경로와 동일한 속성의 객체에 저장된다. 이미 존재한다면 해당 값 사용.

## 참고

- [MDN](https://developer.mozilla.org/ko/docs/Web/API/IndexedDB_API/Using_IndexedDB)
- [FLO 기술 블로그](https://www.blog-dreamus.com/post/indexed-db-%EC%A0%81%EC%9A%A9%EA%B8%B0)
- [티스토리](https://mhui123.tistory.com/53)
- [미디움 블로그](https://medium.com/@KevinBGreene/type-safe-indexeddb-using-typescript-declarative-schema-and-codegen-8708f16ca374)
- [깃헙 참고](https://github.com/falcosan/TS_IndexedDB/blob/main/db/actions.ts)
- [멀티플엔트리 관련](https://stackoverflow.com/questions/25992975/indexeddb-how-to-use-multiple-indexes-along-with-multientry-true)
- [암호화 관련](https://crypto.stackexchange.com/questions/35530/where-and-how-to-store-private-keys-in-web-applications-for-private-messaging-wi)
- [암호화 관련2](https://velog.io/@negu63/%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90-%ED%82%A4%EB%A5%BC-%EC%95%88%EC%A0%84%ED%95%98%EA%B2%8C-%EC%A0%80%EC%9E%A5%ED%95%98%EB%8A%94-%EB%B2%95)

- [idb 라이브러리](https://github.com/jakearchibald/idb)
- `db.js`, `dexie`, `idb`, `loaclforage`, `lokijs` 등 비교하면 사용자풀이 `idb` => `localforage` => `lokijs` => `dexie` => `db.js` 순으로 인기있음.

- [참고 깃](https://github.com/falcosan/TS_IndexedDB/blob/main/db/actions.ts)

- [dexie](https://github.com/dexie/Dexie.js)
- [dexie-encrypted](https://github.com/mark43/dexie-encrypted)
- [dexie-encrypted 암호화관련2와 중복](https://velog.io/@negu63/%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90-%ED%82%A4%EB%A5%BC-%EC%95%88%EC%A0%84%ED%95%98%EA%B2%8C-%EC%A0%80%EC%9E%A5%ED%95%98%EB%8A%94-%EB%B2%95)

## 구성할 때 필요한 조건들

0. 무슨 용도로 사용하려는가?

- 용도에 따라 어떤 형태로 저장할지가 정해질 것임. `index`를 늘려서 사용할 지, 그냥 `key`와 `value` 형태로 다 때려박을지 결정이 가능하다.

1. db 생성 시

- 저장하려는 자료의 형태가 어떤 것인가?
- `keyPath`가 존재하는가? `autoIncreament`가 적용 되어있는가?
- `index`들을 얼마나 잡을 것인가?

2. get / put / set 할 때

- `keyPath`가 존재하는가?
- 존재하지 않는다면, 특정 `index`의 `value`로 값을 찾으려 하는가?
- `keyPath`가 존재한다면 `keyPath`의 값으로 찾으려 하는가?

## 무조건 해야하는 것

1. `keyPath` 설정.

- 여러 형태로 사용 시 사용법이 상당히 난해해져서 `object` 형태만을 사용하는 것이 좋다고 생각함. `get`, `set`, `put` 등의 api 이해가 명확해지기도 하고.
- `keyPath`

```tsx
// 일반 idb 사용법만 첨부
const customerData = [
  { ssn: '444-44-4444', name: 'Bill', age: 35, email: 'bill@company.com' },
  { ssn: '555-55-5555', name: 'Donna', age: 32, email: 'donna@home.org' },
];

interface DefaultIDBData {
  storeName: string;
  value: any;
}

export class CustomIDB {
  customIDB: IDBDatabase;
  dbName: string;
  version: number;

  constructor(dbName = 'CustomIDB', version = 1, datas?: DefaultIDBData[]) {
    this.dbName = dbName;
    this.version = version;
    if (!('indexedDB' in window)) {
      console.warn("This browser doesn't support IndexedDB");
      throw "This browser doesn't support IndexedDB";
    }
    const openReq = indexedDB.open(dbName, version);
    openReq.onsuccess = (e) => {
      console.log('Open CustomIDB success in constructor : ', e);
      this.customIDB = openReq.result;
    };
    openReq.onerror = (e) => {
      console.error('Open CustomIDB error in constructor : ', e);
    };
    openReq.onupgradeneeded = (e) => {
      console.warn('Open CustomIDB upgrade needed in constructor : ', e);
      this.customIDB = openReq.result;

      // datas?.forEach((data) => {
      //   const objectStore = this.customIDB.createObjectStore(data.storeName);
      // })

      const objectStore = this.customIDB.createObjectStore('customers');
      objectStore.createIndex('name', 'name', { unique: false });
      objectStore.createIndex('email', 'email', { unique: true });
      objectStore.transaction.oncomplete = (e) => {
        const customerStore = this.customIDB
          .transaction('customers', 'readwrite')
          .objectStore('customers');
        customerData.forEach((customer) =>
          customerStore.add(customer, customer.age)
        );
      };
    };
    openReq.onblocked = (e) => {
      console.warn('Open CustomIDB blocked in constructor : ', e);
    };
  }

  async getElement<Res>(targetStoreName: string, key: 'all' | string) {
    const openReq = indexedDB.open(this.dbName, this.version);
    return new Promise<Res>((resolve, reject) => {
      openReq.onsuccess = () => {
        let request!: IDBRequest;
        this.customIDB = openReq.result;
        if (
          Array.from(this.customIDB.objectStoreNames).find(
            (name) => name === targetStoreName
          )
        ) {
          const transaction = this.customIDB.transaction(targetStoreName);
          const objectStore = transaction.objectStore(targetStoreName);

          console.log('ㅎㅇ', objectStore.get(['Bill', 'bill@company.com']));
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
          transaction.oncomplete = () => this.customIDB.close();
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
        this.customIDB = openReq.result;
        if (
          Array.from(this.customIDB.objectStoreNames).find(
            (name) => name === targetStoreName
          )
        ) {
          const transaction = this.customIDB.transaction(
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
            this.customIDB.close();
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
        this.customIDB = openReq.result;
        if (
          Array.from(this.customIDB.objectStoreNames).find(
            (name) => name === targetStoreName
          )
        ) {
          const transaction = this.customIDB.transaction(
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
          transaction.oncomplete = () => this.customIDB.close();
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
      this.customIDB = openReq.result;
      if (
        Array.from(this.customIDB.objectStoreNames).find(
          (name) => name === targetStoreName
        )
      ) {
        const transaction = this.customIDB.transaction(
          targetStoreName,
          'readwrite'
        );
        const objectStore = transaction.objectStore(targetStoreName);
        if (key === 'all') request = objectStore.clear();
        else request = objectStore.delete(key);
        request.onerror = () => console.error(request.error);
        transaction.oncomplete = () => this.customIDB.close();
      } else {
        indexedDB.deleteDatabase('data');
      }
    };
  };
}
```
