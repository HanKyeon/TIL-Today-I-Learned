# React 정리

학습 후기 : **왜 리액트 쓰는지 알겠다. VueJS보다 레퍼런스가 많다는 것도 장점이고, 영어가 대부분이라는 것도 장점. CRA를 이용해서 시작을 했는데, 실제로 빌더부터 만드는 것을 학습해야겠다.**

**주의 : 원래 2022 docs를 기반으로 작성중이었으나, 2023 docs가 정식 docs로 변경된 만큼 2023 docs로 정리 할 예정.**
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

### Virtual DOM

- 실제 DOM을 직접 조작하는 것이 아니라, 변경 요청이 발생 할 때 가상 DOM의 before/after 구조를 비교해 변경된 부분만 실제 DOM에 업데이트한다. 실제 DOM을 조작하지 않아 UI의 반응 속도를 높일 수 있다는 장점이 있다.
- 잦은 DOM 조작은 비용이 많이 들고 속도가 느려진다.
- React는 VirtualDOM을 사용해 성능을 향상시키는 방식을 채택했다.
- 가상 DOM의 컴포넌트를 지속적으로 관찰하여 상태 변경을 감지하여 시도한다.
- 가상 DOM의 이전/이후 diff 비교는 재조정 알고리즘을 사용하여 효율적으로 처리한다.
- 비교 결과 차이가 발생하면 실제 DOM에 반영해 UI를 업데이트한다.
- h.js => createElement.js => diff.js => patch.js 순으로 이뤄진다. 모델이 있고, 변동사항이 생긴다면 이전에 생성한 virtualDOM을 저장하고, 새롭게 생성한 virtualDOM을 비교하여 변동사항을 적용한 DOM을 렌더링한다.

**- Virtual DOM 구현**

- 가상 DOM은 실제 DOM 트리를 추상화하여 표현한 것이다.
- 가상 DOM 트리에서 변동사항이 생기면 새로운 가상 DOM 트리가 생성된다.
- 재조정 알고맂므은 새로운 가상 DOM 트리와 이전 가상 DOM 트리를 비교해 실제 DOM에 최소한의 변경만을 적용한다.
- 개인) git의 개념과 비슷한 것 같다. 변동사항만 확인하고 커밋으로 저장하는 것이 git이므로.

- 가상 돔은 실제 돔의 구조를 추상화한 표현이다. 예시를 들자면 아래와 같다.

```html
<ul class="what-is-virtual-dom">
  <li>가상 DOM은 실제 DOM을 추상화 하여 표현한 것을 말합니다.</li>
  <li>가상 DOM 트리에서 무언가 변경되면 새로운 가상 DOM 트리가 생성됩니다.</li>
</ul>
```

- 위의 html을 JS로는 아래와 같이 추상화 한다.

```js
{
	type: 'ul',
	props: { className: 'what-is-virtual-dom' },
	children: [
		{
			type: 'li',
			props: null,
			children: '가상 DOM은 실제 DOM을 추상화 하여 표현한 것을 말합니다.'
		},
		{
			type: 'li',
			props: null,
			children: '가상 DOM 트리에서 무언가 변경되면 새로운 가상 DOM 트리가 생성됩니다.'
		},
	]
}
```

- 이렇게 가상화된 element를 노드라 부르는 것 같다.

- 이 때, 가상 DOM 구조가 복잡해지면 가상 DOM 구조를 손쉽게 생성 할 수 있도록 hyperscript 모듈을 작성한다. `h.js` 모듈을 사용.
- 함수형 컴포넌트를 선언 했을 때, `h(태그, 속성attr, children)` 이런 형태로 선언되도록 `h()` 함수를 통해 생성한다.

- 이 때, 가상 DOM의 구조를 이해하기 편하도록 React는 JSX를 사용한다.
- JSX는 Babel과 같은 컴파일러를 통해 가상 DOM을 생성하는 `React.createElement` 함수 코드로 변환된다.
- `@babel/plugin-transform-react-jsx` 플러그인을 사용하여 JSX 문법을 특정 함수로 처리하여 컴파일이 가능하다.
- 가상 DOM을 생성하는 `h()` 함수를 JSX 문법을 해석하는 함수로 설정하는 등의 세팅이 가능하다. 이러한 행위를 **프라그마** 라고 표현한다.
  = JSX 코드는 바벨에 의해 `h()` 함수로 변경되고 컴파일된다.

- `React.createElement`를 통해 선언적으로 컴포넌트 생성이 가능하다.
- `document.createTextNode` 역시 마찬가지로 사용이 된다.
- `rootNode`는 하나만 가능하며, 하위 `children`에서 `map()` 혹은 `forEach()`를 사용하여 처리하기 때문에 `bind()`메서드를 활용해 처리하기도 한다.

- 가상 DOM이 업데이트 되었을 때 어떻게 처리가 되는가? => 가상 DOM에서의 변경 사항만을 실제 DOM에 반영한다.
- 만약 새로운 노드가 추가된다면 `appendChild` 등을 통해 추가가 될 것이다. 그렇다면 변경된 점을 가상 DOM에 반영한다. `removeChild`이나 `replaceChild` 등으로 변경이 되어도 마찬가지이다.
- 이 때, `parentNode`, `newVNode`, `oldVNode` 3개의 매개 변수를 통해 `updateElement` 모듈을 작성한다.
- `updateElement` 모듈을 작성 할 때, `diff` 모듈이 사용된다! 변경사항을 파악하기 위해서!
- 이후 재귀적인 호출을 통해 `children`의 노드들을 업데이트하게 된다.

- 그렇다면, 가상 DOM에서 `props`는 어떤 방식으로 내려줄까?
- JSX를 이용한다면 간단하게 prop을 내려줄 수 있다. 그렇지만 **babel을 통해 변경**된 것들이 궁금하다!
- 일반적으로 props의 경우 html attribute처럼 물려주며, key와 value 쌍으로 구성이 된다.
- key와 value를 이용하여 `setProp()`, `setProps()` 등의 함수를 통해 개별 필드의 prop을 설정해준다. key만 있는 경우(selected 등)는 `setBooleanProp()`을 사용하고, 사용자 정의 속성은 `isCustomProp()`을 통해 다뤄진다.
- 이 때 `createElement()` 하는 부분의 코드에 `setProp()`, `setProps()` 부분이 추가가 된다.
- `node.removeAttribute()` 메서드를 통해 props를 제거할 수도 있다.
- `updateProps()` 유틸리티를 `props` 변경

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
  - `const [v, setV] = useState(() => value)`로 변수를 선언하면 리렌더링마다 실행되는 것이 아닌, 한 번만 실행이 된다! => 이것을 이요아면 useInput에 input 컴포넌트와 value만을 담아서 반환이 가능하지 않을까 싶음. 이전에 트라이 하던 훅에서 컴포넌트와 값을 반환하는.

- `useEffect`

  - 파라미터로 콜백함수, dependency array를 받는다. 반환 값은 3종류의 RefObject.
  - 마운트 되거나 dependency 값이 변경 될 때 실행되는 hook. return에 들어가는 cleanup 함수는 중요한 개념이다. 언마운트 될 때 실행되는 함수이다.
  - cleanup 함수의 경우, unmount 될 때 실행되기에 비동기 요청을 취소하는데 주로 사용된다.
  - dependency array를 비울 경우, 변화 있을 때마다 실행된다. 빈 배열을 넣는다면 해당 컴포넌트가 마운트 될 때와 언마운트 될 때만 실행.
  - cleanup 함수는 메모리 누수를 방지하기 위해 UI 컴포넌트를 제거하기 직전 수행된다. 다음 이펙트 함수가 실행 될 때마다 실행되기에 componentWillUnmount와 다르다.

- `useRef`

  - 타입스크립트에서 3가지 형태로 Ref가 정해지기에 따로 정하겠지만, JSX element의 attribute에 연결시켜 해당 element를 찝어내는 것이다.
  - 주로 DOM 노드를 참조하기 위해 사용된다. reference.
  - 특정 값을 지속적으로 참조 할 때 사용한다. current가 변경되어도 컴포넌트가 재렌더링되지 않아 성능 최적화에 좋다.

- `useCallback`

  - 함수에 한해 함수를 캐싱하고 사용하는 기능. 메모이제이션이라 한다.
  - 주로 Props로 전달되는 함수가 문제가 되서 리렌더링이 일어나는 경우가 많아서 사용한다. 함수 내부의 함수는 컴포넌트가 업데이트 될 때마다 리렌더링 되기 때문에.
  - 하지만, 상위 컴포넌트가 리렌더링되면 하위 컴포넌트 역시 리렌더링 되기 때문에, `React.memo` 등을 통해 하위 컴포넌트 역시 메모이제이션을 해주어야 불필요한 렌더링을 줄여줄 수 있다. => 이 부분에서 Container Component와 Presentational Component를 구분하는 것이 중요하다 생각.
  - useEffect처럼 의존성 배열을 갖고 있으며, 해당 의존성 배열의 값이 변경될 때 함수를 다시 만든다.

- `useMemo`

  - `useCallback`의 변수 버전이다. 반환되는 값을 캐싱해둔다.
  - 마찬가지로 의존성 배열을 갖고 있으며, 해당 의존성 배열의 값이 변경 될 때 값을 다시 캐싱한다.
  - 컴포넌트 역시 useMemo로 캐싱 할 수 있다. ref 역시 lagged를 걸어줄 수 있음.
  - 자세한 예시는 https://ko.legacy.reactjs.org/docs/hooks-faq.html#how-to-memoize-calculations 참고하면 된다!

- `useCallback` && `useMemo`의 memoization 관련된 내용

  - 2022 docs에서는 해당 값들을 캐싱하는 주된 이유가 컴포넌트 리렌더링 때문으로 정의하며, 특히 Props로 내릴 때의 경우를 걱정한다.
  - 그렇지만 해당 api들로 해결하기 위해서는 `React.memo` 등을 통해 하위 컴포넌트도 메모이제이션을 해야한다.
  - 그렇기에 2022docs에서는 ContextAPI를 통해 내려주는 것을 추천하고 있다.
  - Props가 깊을 때는 Context Provider에서 메모이제이션 한 함수나 값을 내려주는 것을 추천하고 있다.
  - **하지만 애초에 Props로 함수를 깊게 전달하는 것을 추천하지 않는다.**

- `useContext`

  - ContextAPI로 제공되는 값을 가져올 때 사용된다.
  - `createContext` 메서드를 통해 생성된 Context의 `Provider`로 제공되는 가상 돔 컴포넌트로 value를 쏴주는데, 해당 `Provider`의 Context value에 접근하는 훅이다.

- `useReducer`

  - state로 관리하기 까다로운 state들을 관리한다.
  - 주로 Redux를 관리하는 단방향 데이터 흐름 패턴인 Flux Pattern을 따른다. 마찬가지로, reducer 함수를 만들어서 임자로 reducer함수, initialState, initialization을 만들어주면 된다.
  - flux 패턴을 띄고 있기에 사용법이 redux와 유사하다. 리듀서를 모아둔 reducer 함수 (type과 paykoad를 전달하여 type으로 실행시키고 리턴하는 함수)를 받고, 초기값을 받으며, initialization을 통해 상태 초기화를 지연처리한다. 초기 계산 값을 추출하거나, 어떤 동작으로 상태를 초기화 하는 등.

- `useLayoutEffect`

  - `useEffect`와 사용법은 동일하다.
  - 하지만 실행되는 시기, 평가 시점이 달라진다. 페이지 로드 차단을 방지하기 위해 DOM이 렌더링 된 이후 `useEffect()` 훅에 설정된 콜백 함수가 실행되면 위치 및 스타일 적용에 문제가 발생 할 수 있다. 이러한 문제를 해결해야 하는 경우, `useLayoutEffect`를 사용하여 해결 할 수 있따.
  - `useLayoutEffect`는 DOM이 렌더링 되고 페인팅 되기 직전에 실행되고, `useEffect`는 DOM 페인팅이 완료된 이후 실행된다.

- `useImperativeHandle(e)`

  - 명령형 핸들 훅이다.
  - 상위 컴포넌트에서 ref에 의해 참조된 instance 값을 사용자화 할 때는 `useImperativeHandle()` 훅을 사용한다.
  - 일부 명령형 메서드를 상위 컴포넌트에서 사용 할 수 있도록 만들어야 할 때 해당 훅을 사용한다.
  - 파라미터로는 `ref`, `createHandle`, `[deps]`를 받는다. 그렇기에 `forwardRef()` 고차 컴포넌트를 사용해야 한다.
  - 해당 훅은 예시로 보는 것이 이해가 빠를 것 같음. 아래 예제 첨부.
  -

```jsx
import { useState, useRef } from 'react';
function App() {
  const messageDisplayRef = useRef();
  const [messages, setMessages] = useState(allMessages.slice(0, 8));

  const addMessage = () => {
    messages.length < allMessages.length
      ? setMessages(allMessages.slice(0, messages.length + 1))
      : null;
  };

  const removeMessage = () => {
    messages.length > 0
      ? setMessages(allMessages.slice(0, messages.length - 1))
      : null;
  };

  const scrollTop = () => messageDisplayRef.current.scrollTop();
  const scrollBottom = () => messageDisplayRef.current.scrollBottom();

  return (
    <div className="messaging-app">
      <div
        css={`
          display: flex;
          justifycontent: space-between;
        `}
      >
        <button
          type="button"
          onClick={addMessage}
        >
          메시지 추가
        </button>
        <button
          type="button"
          onClick={removeMessage}
        >
          메시지 제거
        </button>
      </div>
      <div
        css={`
          margin-top: 20px;
        `}
      >
        <button
          type="button"
          onClick={scrollTop}
        >
          스크롤 상단 이동
        </button>
        <MessageDisplay
          ref={messageDisplayRef}
          messages={messages}
        />
        <button
          type="button"
          onClick={scrollBottom}
        >
          스크롤 하단 이동
        </button>
      </div>
    </div>
  );
}

// MessageDisplay Componoent
// forwardRef로 감싼 고차함수.
import {
	useRef,
	useLayoutEffect,
	useCallback,
	useImperativeHandle,
	forwardRef
} from 'react';


const MessageDisplay = forwardRef(function MessageDisplay({messages}, ref) {
	const containerRef = useRef();
	useLayoutEffect(() => scrollBottom(), []);
	const scrollTop = useCallback(() => {
		containerRef.current.scrollTop = 0;
	}, []);
	const scrollBottom = useCallback(() => {
		containerRef.current.scrollTop = containerRef.current.scrollHeight;
	}, []);
	useImperativeHandle(ref, () => ({
		scrollTop,
		scrollBottom,
	}), [scrollTop, scrollBottom]);
	return (
		<div ref={containerRef} role="log">
			{messages.map(message, index) => (
				<div key={message.id}>
					<strong>{message.author}</strong>: <span>{message.content}</span>
					{array.length - 1 === index ? null : <hr />}
				</div>
			)}
		</div>
	)
});
```

- `useId()`

  - server - client의 Hydration 작업에 필요하는 고유한 id 값을 생성하는 훅이다.
  - client 개발에서는 label 요소와 input 요소를 명시적으로 연결 할 때 사용하면 편리하다!

- `useTransition`

  - transition 보류 상태 값과 transition을 시작하는 함수를 반환하는 훅이다. 즉, 비동기 처리의 로딩을 처리한다.
  - 트랜지션을 시작하는 함수의 업데이트를 트랜지션으로 표시 할 수 있음.

- `useDeferredValue()`

  - 긴급하지 않은 업데이트의 경우에 사용하며, 긴급한 업데이트(사용자 입력 등)에서 이전 상황을 기억하여 해당 값을 반환한 뒤, 긴급한 렌더링이 완료된 뒤 새로 렌더링 하는 개념이다.
  - Debouncing 혹은 Throttling을 사용해 업데이트를 지연하는 것과 유사하다.
  - 해당 훅을 사용하면 다른 작업이 긑나는 즉시 React가 업데이트를 수행함

## WHAT IF?

- 컴포넌트 주도 설계를 통해서 아래와 같은 이점을 가진다.

1. 품질 : 독립적으로 컴포넌트를 분리하고 관련 상태를 정의하여 UI가 다양한 시나리오에서 작동하는지 확인이 가능하다.
2. 내구성 : 컴포넌트 수준에서 테스트하여 세부 사항까지 버그를 찾아낼 수 있다.
3. 속도 : 컴포넌트 라이브러리 또는 디자인 시스템의 컴포넌트를 재사용하여 UI를 보다 빠르게 재사용할 수 있다.
4. 효율성 : UI를 개별 컴포넌트로 분해한 뒤, 협업을 통해 개발을 병렬적으로 진행하여 효율성을 높일 수 있다.
