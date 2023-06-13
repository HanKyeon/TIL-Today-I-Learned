# Webpack 정리

학습 후기 : **웹팩으로 빌드된 프로젝트를 다룰 경우가 많을 것이라 판단하여 vite 학습을 하며 함께 학습할 예정.**

독스 링크 : https://webpack.js.org/

## WHY?

## WHAT?

## HOW?

## WHAT IF?

## 참고

https://webpack.js.org/

## **웹팩으로 React APP 구성해보기**

### 1. 시작하기

1. 디렉토리 생성 및 이동

- `mkdir 프로젝트이름 && cd $_`

2. 버전관리

- 깃 시작 : `git init # -b main`
- 깃 이그노어 : `npx add-gitignore osx windows node visualstudiocode`

3. 패키지 매니저 초기화

- 패키지 생성 : `npm init -y`

```json
{
  "private": true,
  "type": "module",
  "name": "testWebpack",
  "version": "1.0.0",
  "description": "",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "react",
    "webpack",
    "eslint",
    "prettier",
    "babel",
    "typescript",
    "jest",
    "testing-library",
    "sass",
    "postcss",
    "svgr"
  ],
  "author": {
    "name": "yamoo9",
    "email": "yamoo9@euid.dev"
  },
  "license": "ISC"
}
```

4. HTML 엔트리

- public 디렉토리 생성 및 index.html 생성

5. JavaScript 엔트리 파일

- src 디렉토리 생성 및 main.js 생성

6. JavaScript 모듈 파일 생성

- src/utils/index.js
  ```jsx
  export * from './test.js';
  export * from './styleLog.js';
  export * from './currency.js';
  export * from './numberWithComma.js';
  ```
- src/utils/slyleLog.js
  ```jsx
  export const styleLog = (message, cssCode) => {
    console.log(`%c${message}`, cssCode);
  };
  ```
- src/utils/numberWithComma.js
  ```jsx
  export const numberWithComma = (number) => {
    return number.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,');
  };
  ```
- src/utils/currency.js

  ```jsx
  import { numberWithComma } from './numberWithComma.js';

  export const currency = (price, currencyUnit = '원') => {
    price = numberWithComma(price);
    return currencyUnit === '원'
      ? `${price}${currencyUnit}`
      : `${currencyUnit}${price}`;
  };
  ```

7. 테스트

- `npx live-server public --host=localhost --port=3000

### 2. 웹팩 명령어 환경 구성

1. Webpack 명령어 혼경 구성

- webpack & cli 설치 : npm i -D webpack webpack-cli

2. 번들 명령

- `package.json` 패키지에 웹팩 번들 명령 등록
  ```json
  {
    "scripts": {
      "webpack:config": "webpack --target=browserslist --entry=./src/main.js --output-path=public",
      "webpack:dev": "npm run webpack:config -- --mode=development"
    }
  }
  ```

3. 타겟 설정

- 프로제트의 루트 위치에 `.browserslistrc` 파일 생성 후 목록 작성. **참고 : https://browsersl.ist/**
  ```
  > 0.5% in KR
  last 2 versions
  not dead
  ie 11
  ```

4. 웹팩 번들링 실행

- `npm run webpack:dev`

5. 빌드 명령

- `package.json`의 `scripts`에 빌드 명령 추가.

```json
{
  "scripts": {
    "webpack:config": "webpack --target=browserslist --entry=./src/main.js --output-path=public",
    "webpack:dev": "npm run webpack:config -- --mode=development",
    "webpack:prod": "npm run webpack:config -- --mode=production"
  }
}
```

6. 빌드 실행

- `npm run webpack:prod`

### 3. Webpack 개발, 빌드 구성

- 기본적인 구성을 사용해 번들링 하기 좋지만, 복잡한 구성에 사용하기 적합하지 않음.
- 그렇기에 별도의 구성 파일을 작성하는 것이 좋다.

1. 공통 구성 파일

- webpack/common.js

```js
import { resolve } from 'node:path';

const commonConfig = {
  target: ['web', 'browserslist'],
  entry: {
    main: resolve('src/main.js'),
  },
  output: {
    path: resolve('public'),
    filename: '[name].bundle.js',
  },
};

export default commonConfig;
```

2. 개발 구성 파일

- webpack/dev.js

```js
import { merge } from 'webpack-merge';
import commonConfig from './common.js';

const devConfig = merge(commonConfig, {
  mode: 'development',
  devtool: 'eval-cheap-source-map',
});

export default devConfig;
```

3. 빌드 구성 파일

- webpack/prod.js

```js
import { merge } from 'webpack-merge';
import commonConfig from './common.js';

const prodConfig = merge(commonConfig, {
  mode: 'production',
  devtool: false,
  output: {
    ...commonConfig.output,
    filename: '[name].min.js',
  },
});

export default prodConfig;
```

4. 개발, 빌드 명령 구성

- package.json 관리

```json
{
  "scripts": {
    "bundle": "webpack bundle -c webpack/dev.js",
    "build": "webpack build --progress -c webpack/prod.js"
  }
}
```

- 이 때, 사용자 정의 Browserslist 구성 파일을 설정한다면, `package.json` 또는 `.browserslistrc`에서 관리하기 권장.
- 별도 구성 파일을 특정 디렉토리에서 고나리하고 싶다면, `BROWSERSLIST_CONFIG` 환경 변수를 사용할 수 있다.

```json
{
  "scripts": {
    "bundle": "cross-env BROWSERSLIST_CONFIG=config/.browserslistrc webpack -c config/webpack/config.js"
  },
  "devDependencies": {
    "cross-env": "7.0.3",
    "webpack": "5.75.0",
    "webpack-cli": "4.10.0"
  }
}
```

### 4. Webpack 서버 구성

필요한 모듈

`npm install -D webpack-dev-server`

1. Webpack 개발 서버 구성

- `webpack/server.js`를 관리해줘야 한다.

```js
const devServer = {
  host: 'localhost',
  port: 3000,
  hot: true,
  open: false,
  compress: true,
  liveReload: true,
  static: ['public'],
  historyApiFallback: true,
  client: {
    logging: 'info',
    overlay: true,
    reconnect: 3,
  },
  watchFiles: {
    paths: ['src/**/*.*', 'public/**/*.*'],
  },
};

export default devServer;
```

2. 서버 구성 설정

- `webpack/dev.js` 파일에 개발 서버 구성 파일을 불러와서 개발 서버 구성을 추가한다.

```js
import { merge } from 'webpack-merge';
import commonConfig from './common.js';
import devServer from './server.js';

const devConfig = merge(commonConfig, {
  mode: 'development',
  devtool: 'eval-cheap-source-map',
  devServer,
});

export default devConfig;
```

3. 스크립트 등록

- `package.json` 파일에 npm 스크립트 명령어 추가.

```json
{
  "scripts": {
    "start": "npm run server -- --open",
    "dev": "npm run server",
    "server": "webpack server -c webpack/dev.js",
    "bundle": "webpack bundle -c webpack/dev.js",
    "build": "webpack build -c webpack/prod.js"
  }
}
```

4. HTML 엔트리 수정

- `public/index.html`에 서버 구동 시 번들링 된 파일이 HTML 엔트리 파일에 연결될 수 있도록 한다.

```html
<!DOCTYPE html>
<html lang="ko-KR">
  <head>
    <!-- ... -->
    <script
      type="module"
      src="main.bundle.js"
    ></script>
  </head>
  <!-- ... -->
</html>
```

### 5. React 모듈 구성

1. 리액트를 사용하기 위해 react와 react-dom 설치
   `npm install react@latest react-dom@latest`

2. HTML엔트리 수정

- `public/index.html`에서 HTML 파일에 react 사용을 알려주고 루트 컴포넌트를 생성

```html
<!DOCTYPE html>
<html lang="ko-KR">
  <head>
    <!-- ... -->
    <script
      type="module"
      src="main.bundle.js"
    ></script>
  </head>
  <body>
    <!-- ... -->
    <div id="root"></div>
  </body>
</html>
```

3. React API 사용

- `src/main.js`에 React, ReactDOM Api를 통해 앱이 렌더링되게 명시

```js
import { createElement as h, StrictMode } from 'react';
import { render } from 'react-dom';

const reactFigure = h(
  'figure',
  {
    className: 'react-figure',
  },
  h(
    'a',
    {
      className: 'link',
      href: 'https://reactjs.org',
      target: '_blank',
      rel: 'noopener noreferrer',
    },
    h('img', {
      className: 'logo',
      src: 'assets/react.svg',
      alt: 'React',
    })
  ),
  h(
    'figcaption',
    {
      className: 'description',
    },
    'React 툴체인 매뉴얼 구성'
  )
);

const app = h('div', { className: 'App' }, reactFigure);

render(h(StrictMode, null, app), document.getElementById('root'));
```

4. JSX 사용

- `src/main.jsx` React Component App과 JSX를 활용 할 수 있도록 코드 변경. jsx를 사용하므로 JSX 파일로 변경

```jsx
import { createElement as h, StrictMode } from 'react';
import { render } from 'react-dom';

const reactFigure = h(
  'figure',
  {
    className: 'react-figure',
  },
  h(
    'a',
    {
      className: 'link',
      href: 'https://reactjs.org',
      target: '_blank',
      rel: 'noopener noreferrer',
    },
    h('img', {
      className: 'logo',
      src: 'assets/react.svg',
      alt: 'React',
    })
  ),
  h(
    'figcaption',
    {
      className: 'description',
    },
    'React 툴체인 매뉴얼 구성'
  )
);

const app = h('div', { className: 'App' }, reactFigure);

render(h(StrictMode, null, app), document.getElementById('root'));
```

- 이후 .jsx 확장자 없이도 불러올 수 있도록 webpack 공통 파일 `webpack/common.js` 수정

```js
import { resolve } from 'node:path';

const commonConfig = {
  // ...
  resolve: {
    extensions: ['.js', '.jsx', '.json', '.wasm'],
  },
  entry: {
    main: resolve('src/main.jsx'),
  },
};

export default commonConfig;
```

- jsx를 사용하기에 babel을 사용해야 한다.

## 6. Babel 구성

- JSX, TypeScript 등 웹팩이 읽을 수 없는 것들을 babel loaders를 통해 처리하여 앱에서 사용해야 한다.
- Webpack은 JS와 JSON만 읽을 수 있으며, 웹팩의 로더는 test 속성과 use 속성을 가진다. test는 변환이 필요한 파일을 식별하고, use는 변환을 수행하는데 필요한 로더를 지칭한다.
- 그래서 바벨을 사용한다.
- `npm install -D babel-loader @babel/core @babel/preset-env @babel/preset-react`

### 1. Babel 구성 파일

- 프로젝트 루트에 babel 구성 파일 `babel.config.js`를 추가하고 프리셋을 활용하도록 작성해준다.

```js
export default {
  presets: [
    '@babel/preset-env',
    ['@babel/preset-react', { runtime: 'automatic' }],
  ],
};
```

### 2. Babel loader 설정

- 웹팩의 `webpack/common.js` 파일에 babel-loader를 사용한다고 명시.
- 참고 : https://webpack.js.org/loaders/babel-loader/

```js
import { resolve } from 'node:path';

const commonConfig = {
  // ...
  module: {
    rules: [
      {
        test: /\.jsx?$/i,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
    ],
  },
};

export default commonConfig;
```

### 3. TypeScript 설정

- 타입스크립트 역시 웹팩이 읽을 수 없기에 바벨로더로 번역해줘야 한다.
  `npm install -D @babel/preset-typescript typescript`

- 이후 `babel.config.js`에 typescript의 프리셋을 사용하도록 명시한다.

```js
export default {
  presets: [
    '@babel/preset-env',
    ['@babel/preset-react', { runtime: 'automatic' }],
    ['@babel/preset-typescript', { optimizeConstEnums: true }],
  ],
};
```

- 마찬가지로 webpack의 `webpack/common.js`에서 test 부분을 수정해준다. tsx도 읽으라고.

```js
import { resolve } from 'node:path';

const commonConfig = {
  // ...
  module: {
    rules: [
      {
        test: /\.(t|j)sx?$/i,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
    ],
  },
};

export default commonConfig;
```

- 이후 Typescript의 구성파일을 생성한다. 이 레포에서 TS를 쓴다고 명시하는 것이다.
  `npx tsc --init`

- `tsconfig.json` 을 아래처럼 작성

```json
{
  "compilerOptions": {
    "target": "es2015",
    "module": "NodeNext",
    "moduleResolution": "node",

    "jsx": "react-jsx",
    "jsxImportSource": "react",

    "baseUrl": "src",
    "typeRoots": ["node_modules/@types", "src/@types"],

    "allowJs": true,
    "resolveJsonModule": true,

    "noEmit": true,

    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,

    "forceConsistentCasingInFileNames": true,

    "strict": true,

    "skipLibCheck": true
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
```

## 7. 타입스크립트 로더 구성
