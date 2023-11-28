import {
  addDexieData,
  getKey,
  makeDexieEncrypt,
  testDexieEncrypt,
} from '@/utils/indexedDB/dexie-db';
import { useRef, useState } from 'react';

export const SecretIndexedDB = function () {
  const [key, setKey] = useState<string>('testStore');
  const [aesKey, setAesKey] = useState<
    Uint8Array | CryptoKey | ArrayBufferLike | any
  >();
  const inputRef = useRef<HTMLInputElement>(null);
  const getKeyById = async function () {
    const key = await getKey(parseInt(inputRef?.current?.value) || 123);
    console.log(key, '컴포넌트에서 가져온 복호화 키');
    setAesKey(key);
  };
  const setTestRoomDB = function () {
    console.log('디비 세팅');
    if (aesKey)
      makeDexieEncrypt(
        aesKey
        // parseInt(inputRef.current.value ?? '123'),
      );
  };
  const addTestDexieDB = async function () {
    console.log('디비에 값 추가');
    addDexieData(aesKey); //parseInt(aesKey, inputRef.current.value ?? '123')
  };
  const getTestDexieDB = async function () {
    console.log('디비에서 값 가져오기');
    if (aesKey)
      testDexieEncrypt(
        aesKey
        // parseInt(inputRef.current.value ?? '123'),
      );
  };

  return (
    <>
      <div>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            getKeyById();
          }}
        >
          <input
            ref={inputRef}
            type="number"
          />
          <button type="submit">key 가져오기</button>
        </form>
        <div onClick={setTestRoomDB}>Dexie-encrypt 세팅</div>
        <div onClick={addTestDexieDB}>덱시 값 추가</div>
        <div onClick={getTestDexieDB}>추가된 값 name index로 가져오기</div>
      </div>
    </>
  );
};
class MyClass {
  value: string;
  constructor() {
    this.value = 'initial value';
  }
  handleClick = () => {
    console.log(this.value);
  };
}

const myClass = new MyClass();

export const PresentationalComp = function ({
  handleClick,
}: {
  handleClick: VoidFunction;
}) {
  return <div onClick={handleClick}>hello, world!</div>;
};

export const ContainerComp = function () {
  return (
    <>
      <PresentationalComp handleClick={myClass.handleClick} />
    </>
  );
};
// 아래 코드에서 PresentationalComp에서 handleClick이 실행될 때, `this.value`를 출력해야 하는데 this가 undefined로 나오는데 이유가 뭐야?
// ```tsx
// class MyClass {
//   value: string;
//   constructor() {
//     this.value = 'initial value';
//   }
//   handleClick = () => {
//     console.log(this.value);
//   };
// }

// const myClass = new MyClass();

// const PresentationalComp = function ({
//   handleClick,
// }: {
//   handleClick: VoidFunction;
// }) {
//   return <div onClick={handleClick}>hello, world!</div>;
// };

// const ContainerComp = function () {
//   return (
//     <>
//       <PresentationalComp handleClick={myClass.handleClick}/>
//     </>
//   );
// };
// ```
