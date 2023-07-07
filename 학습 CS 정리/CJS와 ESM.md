# CJS와 ESM

- 참고 : https://toss.tech/article/commonjs-esm-exports-field

## CommonJS (CJS)

```js
// add.js
module.exports.add = (x, y) => x + y;

// main.js
const { add } = require('./add');

add(1, 2);
```

## ECMAScript Modules (ESM)

```js
// add.js
export function add(x, y) {
  return x + y;
}

// main.js
import { add } from './add.js';

add(1, 2);
```

## 차이점

- CJS는 `require` / `module.exports`를 사용하고, ESM은 `import` / `export`를 사용한다.
- CJS module loader는 동기적으로 작동하고, ESM module loader는 비동기적으로 작동한다.
  - ESM은 Top-level Await를 지원하기에 비동기적으로 동작.
- 따라서 ESM에서 CJS를 `import` 할 수는 있지만, CJS에서 ESM을 `require` 할 수는 없다. 왜냐면 CJS는 Top-level Await를 지원하지 않기 때문.
- 이 외에도 두 종류의 module system은 기본적으로 동작이 다르며 호환이 어렵다.

## 이유

- SSR 차원에서 Node.JS에서 주로 쓰이는 문법인 CJS를 지원해야 한다. NextJS에서 쓰이기에.
- Module의 경우 브라우저 환경의 성능에도 관련이 있다. 렌더링을 중단시키는 리소스들 중 하나이므로.
- 따라서 번들 사이즈를 줄여서 렌더링 중단 시간을 최소화해야 한다. 이를 위해 Tree-shaking이 필요하다. 필요하지 않는 코드와 사용되지 않는 코드를 삭제하여 JavaScript 번들의 크기를 가볍게 만드는 것을 말한다.
- 이 때, CJS는 Tree Shaking이 어렵고, ESM은 쉽다.
- CJS는 기본적으로 `require`와 `module.exports`를 동적으로 하는 것에 아무 제약이 없기에, 빌드 타임에 정적 분석을 적용하기 어렵고, 런타임에서만 모듈 관계를 파악할 수 있다.
- 하지만 ESM은 정적 구조로 모듈끼리 의존하도록 강제한다. `import path`에 동적인 값을 사용할 수 없고, `export`는 항상 최상위 스코프에서만 사용이 가능하다.
- 따라서 ESM은 빌드 단계에서 정적 분석을 통해 모듈간 의존 관계를 파악할 수 있고, Tree-Shaking을 쉽게 할 수 있다.
