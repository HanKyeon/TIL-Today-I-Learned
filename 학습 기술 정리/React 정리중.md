# React 정리

학습 후기 : **왜 리액트 쓰는지 알겠다. VueJS보다 레퍼런스가 많다는 것도 장점이고, 영어가 대부분이라는 것도 장점. CRA를 이용해서 시작을 했는데, 실제로 빌더부터 만드는 것을 학습해야겠다.**
학습 버전 v18

## WHY?

- 여러가지 이유가 있겠지만, 개인적으로는 가장 많은 사용률을 기록하고 있어 reference를 찾기 좋다는 점이 최고의 강점이라 생각한다.
- 또한, 바닐라 자바스크립트보다 재사용성이 높아진다고 생각한다.

- 컴포넌트 기반 개발 CBD를 사용하여, 다채롭고 복잡한 사용자 인터페이스를 쉽게 구현 할 수 있도록 해주며, 고레벨의 구문을 제공해서 선언형 방식, 선언형 컴포넌트로 개발한다.
- 사용자 지정 html을 만들고, react가 나머지 작업을 사용하며, 재사용성을 높여준다.

## WHAT & HOW?

- 이례적으로, React의 경우 학습할 내용이 많기에 WHAT과 HOW를 깔끔하게 떼어내어 정리하기 어렵기에 두 토픽을 하나로 합쳐서 정리하도록 하겠다.

### What is React?

- Component Base Develop을 도와주는 JS 라이브러리이다.
- 선언형 프로그래밍, 컴포넌트 시스템, 멀티 플랫폼 지원이라는 강점을 가지고 있다.

1. 선언형 프로그래밍

- 선언형 프로그래밍은 일부 명령적 구현에 대한 추상을 사용해 원하는 것이 무엇인지를 기술한다.
- React의 경우 선언형 프로그래밍 방식으로 앱의 UI를 구축 할 수 있다.
- JavaScript+DOM / jQuery 같은 라이브러리는 명령형 프로그래밍이기에, 어떻게 해야하는지 설명한다.

2. 컴포넌트 시스템

- 컴포넌트란, 앱을 구성하는 하나의 블록이다.
- React는 HTML 요소를 반환하는 React 함수 혹은 Class로 컴포넌트를 만든다.
- React에서 모든 컴포넌트는 가상 돔, Virtual DOM의 node로 구성이 된다. Virtual DOM Tree는 브라우저에 렌더링되어 UI를 구성한다.
- CDD Component Driven Develop 컴포넌트 주고 설계가 쉬워진다. 규모가 큰 UI는 깨지기 쉽고, 디버깅이 어려울 뿐더러 제작에도 많은 시간이 필요하다. CDD란, 컴포넌트를 모듈 단위로 개발하여 UI 구축에 도달하는 개발 및 설계 방법론이다. 기본 컴포넌트 단위부터 시작하여 UI 뷰를 구성하기 위한 점진적 결합 방식의 상향적 성향을 띈다. 장점으로는 품질, 내구성, 속도, 효율성이다. 독립적이고 세부적이며, 개발이 빠르고 효율적이다. 재사용성이 높기에.
- React는 컴포넌트를 모듈 형태로 세분화하여 경고하고 유연한 컴포넌트를 구축 할 수 있도록 제공한다.

3. 멀티 플랫폼 지원

- React는 멀티 플랫폼에서 작동하는 앱을 제작하는 공통 방법을 제공한다.
- ReactDOM을 이용해서 웹 사이트와 웹앱을 만들 수 있고, React-Native를 이용해 모바일 네이티브 앱을 사용한다.

4. 추가적으로 깊게 학습하면 좋을 내용들

- 가상 DOM
- ES6
- 전달 유형 검사
- 컴포넌트 및 JSX, Fragment, 컴포넌트와 DOM 요소 접근 관련.
- 속성/메서드 전달 Props
- 조건/리스트 렌더링
- 이벤트 핸들링
- 양방향 데이터 바인딩
- 스타일링
- 클래스 컴포넌트와 상태, 생명주기
- 함수형 컴포넌트와 useState 상태, useEffect의 cleanup과 생명주기, hook을 통한 재사용성 향상.

### 리액트를 어떻게 빌드하고 있는가?

0. 내가 사용하고 있는 React

- 나는 기본적으로 CRA Create React App을 사용해서 개발을 시작했다. 하지만, vite + react라는 기술을 배웠기에 정리를 해보겠다.

1. React는 어떻게 시작해야 할까

- 기존적으로, script에 src로 react.development.js를 crossorigin으로 연결해준다.
- 이후, createRoot()를 통해 루트 컴포넌트를 생성하게 된다. `const root = createRoot(container[, options])` 이후 `root.render(element)` 형태로 root 컴포넌트를 생성해준다.
- 옵션 값으로는 `onRecoverableError`와 `identifierPrefix` 옵션이 존재한다. `onRecoverableError`는 React가 오류를 복구 할 때 자동으로 호출되는 콜백이고, `identifierPrefix`는 React에서 자동으로 생성하는 ID에 사용된다. 동일 페이지에서 여러 루트를 사용해야 할 때 충돌을 방지하는데 유용하며, 서버에서 사용된 것과 동일한 접두사여야 한다. **해당 부분은 사용해본 적이 없기에, 추후 직접 사용해보며 익혀보자.**
- `root`의 경우, `unmount()`메서드를 통해 DOM에서 언마운트가 가능하다.

2. JSX의 개념

- JSX는 JavaScript에서 마크업을 설명하는데 널리 사용되는 구문이다. 대다수 사람들은 React를 사용 할 때 JSX를 사용해 코드를 작성한다.
- JSX의 특징으로는, React 엘리먼트, interpolation을 통한 변수 선언, js의 표현식, xml 문법 준수, html처럼 데이터, aria, 스타일 등 다양한 attribute가 존재한다는 특징이 있다.

3. Babel은?

- 바벨은 컴파일러다. 가상 DOM의 엘리먼트들을 실제 JavaScript로 해석해주는 것이다.
- 바벨 빌드 컴파일러는 React를 만드는데 적합하다.

### 리액트 실 사용법

1. 컴포넌트와 Props

- **함수형 컴포넌트는 props를 인자로 받고, class 컴포넌트는 constructor로 받아서 super(props) 해준다.**
- **함수 역시 일급 객체이기 때문에 props로 내릴 수 있다는 점을 이용해 함수를 내려서 직접 실행한다.**
- 단방향 데이터 흐름을 통해 데이터를 예측 가능하도록 선언적으로 사용한다.
- React에서 컴포넌트에 Props를 내리는 방법은 기본적으로 JSX를 통해 이뤄지기 때문에, function Component라면 함수의 파라미터로 props를 받아줄 수 있다.
- TypeScript의 경우 타입을 지정해야 하는데 FC로 지정해도 되나, PropsWithChildren과 반환 JSX.Element를 사용중이다.
- 클래스 컴포넌트의 경우, constructor로 props를 받아서 super(props) 해주면 된다.
- JS답게 함수가 일급 객체로 동작하기 때문에, 함수를 직접 Props해서 함수를 사용하면 된다.

2. 컴포넌트의 상태. state.

- `import { useState, useReducer } from "react"`를 이용해서 상태를 선언한다.
- reducer의 경우, 나는 잘 사용하지 않았다. 하지만 상태를 조금 더 상세하게 관리 할 수 있기에, reducer 역시 좋은 상태 관리 방법이라고 생각한다. 하지만 복잡한 상태 관리의 경우, redux 등을 사용하는 것이 좋다고 생각한다.
- 타입스크립트의 경우, 타입 어설션을 사용할 수 있다. `const a = useState<string>("")` 처럼.
- state를 사용하지 않는 컴포넌트의 경우, 오직 값을 받아서 실행하기에 presentational component라고도 부른다.
- state를 갖는, 상태를 가지는 컴포넌트의 경우, contatiner 컴포넌트라 칭하며 상태 관리 로직을 가지고 있다.
- props에 defaults 속성을 정의해서 JS에서도 타입 관련 메서드를 사용 할 수 있다.
- 상태를 관리하는 함수를 presentational component에 드릴링 해주어 container의 비즈니스 로직을 실행 시킨다.
- form을 가진 컴포넌트의 경우, event.target.value 혹은 ref를 사용한다.

3. form

- **form의 경우, value를 이용해 양방향 바인딩을 할 수 있으나, password 등에서 value가 element에 뜨기 때문에 나는 ref를 사용한 방식을 선호한다. event.target.value의 경우는 한 글자가 늦어지기에 setState를 event.target.value로 해주어야 해서 ref를 통한 state 업데이트를 사용한다.**
- form은 유저의 입력이 들어가고, 입력을 상태로 관리한다. 위에서 말했듯, useRef()를 통해 element에 reference를 연결해 state를 갱신하는 방식으로 사용한다. `setState(() => inputRef.current.value)` 이런 식으로.
- 입력 validation의 경우, 정규 표현식을 사용하며, validation 함수를 만들어서 작성한다.
- 작성해둔 정규 표현식은 정말 알차게 써먹고 있다.

4. Context API

- Props, callback을 활용한 단방향 데이터 플로우는 컴포넌트 깊이가 깊어질수록 사용하기가 어렵다.
- 그렇기에 지역적으로 변수를 사용 할 수 있는 context API가 존재한다.
- initial 값을 사용하고, provider를 제공하며, reducer들을 모아둔다. redux와 비슷하나, API이기에 조금 더 JS에 가까운 방식이다.

### React Hook

- 내가 가장 좋아하는 부분이다. 재사용성을 확 끌어올려줄 수 있다.
- hooks는 로직 재사용성이 뛰어나다. 또한 캡슐화 처리를 통해 격리된 지역 상태를 유지한다.

#### react 기본 hook

- `useState`
  - 인자는 초기값이고, 반환 값은 [상태값, 상태 업데이트 함수]
  - 상태 값이 변환될 경우 폭포수처럼 사용하는 것이 변경된다. 아마도 옵저버 패턴이 적용된 것이 아닐지.
  - `setState(() => value)`의 경우, 초기화가 지연되기에 최신 값임을 보장 할 수 있으며, 계산될 동안 기존 값을 유지하기에 나는 웬만해서 해당 형태를 사용한다.
- `useEffect`
  - 파라미터로 콜백함수, dependency array를 받는다. 반환 값은 3종류의 RefObject.
  - 마운트 되거나 dependency 값이 변경 될 때 실행되는 hook. return에 들어가는 cleanup 함수는 중요한 개념이다. 언마운트 될 때 실행되는 함수이다.
  - cleanup 함수의 경우, unmount 될 때 실행되기에 비동기 요청을 취소하는데 주로 사용된다.
  - dependency array를 비울 경우, 변화 있을 때마다 실행된다. 빈 배열을 넣는다면 해당 컴포넌트가 마운트 될 때와 언마운트 될 때만 실행.
  - cleanup 함수는 메모리 누수를 방지하기 위해 UI 컴포넌트를 제거하기 직전 수행된다. 다음 이펙트 함수가 실행 될 때마다 실행되기에 componentWillUnmount와 다르다.
- `useRef`

  - 타입스크립트에서 3가지 형태로 Ref가 정해지기에 따로 정하겠지만, JSX element의 attribute에 연결시켜 해당 element를 찝어내는 것이다.
  - 주로 DOM 노드를 참조하기 위해 사용된다. reference.
  - 특정 값을 지속적으로 ㅊ마조 할 때 사용한다. current가 변경되어도 컴포넌트가 재렌더링되지 않아 성능 최적화에 좋다.

- `useCallback`
- `useMemo`
- `useContext`
- `useReducer`
- `useLayoutEffect`
- `useImperativeHandle(e)`
- `useId()`
- `useTransition`
- `useDeferredValue()`

## WHAT IF?

- 컴포넌트 주도 설계를 통해서 아래와 같은 이점을 가진다.

1. 품질 : 독립적으로 컴포넌트를 분리하고 관련 상태를 정의하여 UI가 다양한 시나리오에서 작동하는지 확인이 가능하다.
2. 내구성 : 컴포넌트 수준에서 테스트하여 세부 사항까지 버그를 찾아낼 수 있다.
3. 속도 : 컴포넌트 라이브러리 또는 디자인 시스템의 컴포넌트를 재사용하여 UI를 보다 빠르게 재사용할 수 있다.
4. 효율성 : UI를 개별 컴포넌트로 분해한 뒤, 협업을 통해 개발을 병렬적으로 진행하여 효율성을 높일 수 있다.
