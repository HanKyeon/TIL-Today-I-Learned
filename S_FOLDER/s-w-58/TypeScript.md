## 참고 문헌들

- 주로 타입스크립트 공식 독스와 구글링 상단 게시글임.
- https://www.typescriptlang.org/docs/handbook/type-compatibility.html#private-and-protected-members-in-classes
- https://www.typescriptlang.org/docs/handbook/2/objects.html#interfaces-vs-intersections

### enum type

- 아래와 같이 지정하고 사용

```js
export enum Test {
  Hi = '1',
  Hello = '2',
  Lego = '3'
}

console.log(Test.Hi) // 1
console.log(Test.Hello) // 2
console.log(Test.Lego) // 3
```

### intersection types

- 간단히 말해서, `&` 연산자로 새로 생성되는 type이다.

```js
interface AType {
  test1: number;
}
interface BType {
  test2: number;
}
type ABType = Atype & BType;
```

### class 형태의 private 변수 관련

- `class`의 `implements`.

  1. `implements`는 `class`의 구조를 잡아주는 것이 아니다.
  2. `implements`는 `class`가 `implements`된 `interface`의 값을 가지고 있는지 검증하는 용도이다.

- `getter`, `setter` 관련

  0. `getter`와 `setter`를 사용하는 이유는 객체 내부 속성의 직접 접근을 막아 보안을 강화하고, 코드 안정성과 유지보수성을 늘릴 수 있다.
  1. class에 `get test() {return 'test'}`라는 `getter`가 선언되어 있다면, 해당 값은 `interface`에서는 `get test(): string;` 형태로 선언한다.
  2. `setter`는 `return type`이 없다. 즉, `interface`로 `setter`를 검증하고 싶다면 `set setDate(newDate: string)` 이런 형태로 선언하면 된다.
  3. `setter`를 선언 할 때 주의점으로는 `args` 즉 인자를 하나만 받을 수 있다는 것이다.
  4. `getter`는 그냥 변수 쓰듯 쓰면 된다. `SomeClass.test` 이런 형태로.
  5. get은 일종의 변수도 set은 할당 연산자로 실행된다.

  - 참고해보면 좋을 글 : https://lovethefeel.tistory.com/173

- `private` 검증(`implements`) 관련

  1. `private`은 `protected`를 선언한 타입과 유사하다. 하지만, 자식 클래스에서도 `private`을 지키는 점이 다르다. (docs에서는 `subclasses`에서도 access가 불가능하다고 설명.)
  2. `private`변수는 검증하면 안된다. 과거 버전에 명확히 적혀있던 규칙. 현재 독스에는 명확히 적혀있지 않고 약간 추상적으로 적혀있지만 통용되는 내용임.

### 제네릭

- 참고 : https://www.typescriptlang.org/docs/handbook/2/mapped-types.html
- 참고2 : https://inpa.tistory.com/entry/TS-%F0%9F%93%98-%ED%83%80%EC%9E%85%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-Generic-%ED%83%80%EC%9E%85-%EC%A0%95%EB%B3%B5%ED%95%98%EA%B8%B0
- 참고3 : https://www.tutorialsteacher.com/typescript/typescript-generic-interface
- 참고4 : https://hyunseob.github.io/2017/01/14/typescript-generic/
- 참고5 : https://stackoverflow.com/questions/62233382/how-do-i-define-and-call-a-generic-function-parameter-in-typescript

- 아래는 객체 나름 재밌는 제네릭인듯? 자동 제네릭 같음
- 일반적으로 제네릭을 받아서 반환값 등에 쓰면 좋을 것 같음.

```js
type MappedType<T> = {
  [Properties in keyof T]: T[Properties];
};

interface DefaultData<DataType, StoreType, SourceType> {
  data: MappedType<DataType>;
  stores: MappedType<StoreType>;
  source: MappedType<SourceType>;
}
```
