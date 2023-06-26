# Webpack 정리

학습 후기 : **웹팩으로 빌드된 프로젝트를 다룰 경우가 많을 것이라 판단하여 vite 학습을 하며 함께 학습할 예정.**

- 툴체인 요구사항

1. 패키지 매니저
2. 번들러
3. 컴파일러
4. 포매터
5. 린터
6. 테스트 러너
7. 미니마이저
8. 서버

- 앱 개발을 위한 도구들을 모아둔 것이다. 그저 모듈 번들로러써만 일하는 것이 아니다.

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

- `TypeScript`를 사용할 계획이라면 `ts-loader`를 포함한 패키지가 필요함.
  `npm install -D ts-loader typescript @types/node @types/react @types/react-dom`

### TypeScript 구성 파일 생성

- `npx tsc --init`을 통해 TypeScript 컨피그를 만들어준다.

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

### TypeScript 로더 설정

- TypeScript 파일을 Webpack이 읽고 해석할 수 있도록 webpack의 `webpack/common.js` 파일에 ts-loader와 `resolve.extensions`를 설정한다.

```js
import { resolve } from 'node:path';

const commonConfig = {
  // ...
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx', '.json', '.wasm'],
  },
  module: {
    rules: [
      // ...
      {
        test: /\.tsx?$/i,
        exclude: /node_modules/,
        use: 'ts-loader',
      },
    ],
  },
};

export default commonConfig;
```

- 이 때, `tsconfig.json` 파일과 Babel 구성 파일 사이에 문제가 발생할 수 있다.
- 해당 부분은 `tsconfig.json` 파일에서 noEmit 설정을 true로 돌리면 해결이 가능하다.

  ```json
  {
    "compilerOptions": {
      // ...
      "noEmit": true
    }
  }
  ```

- 이후 webpack 개발 서버를 구동하더라도 모듈 빌드에 실패하는 오류 메시지를 확인할 수 있는데, 해당 부분은 모듈을 emit 하지 않아서 그렇다.
- `tsconfig.json` 파일에서의 오류를 해결하기 위해 추가한 `noEmit` 설정이 문제가 된다.
- 이 문제는 Webpack 공통 구성 파일에 설정한 `ts-loader` 옵션을 통해 해결할 수 있다. 오더 구성에 `options` 항목을 설정하면 모듈이 emit 되므로 Webapck이 정상 작동한다.
- `webpack/common.js`

  ```js
  import { resolve } from 'node:path';

  const commonConfig = {
    // ...
    module: {
      rules: [
        // ...
        {
          test: /\.tsx?$/i,
          exclude: /node_modules/,
          use: {
            loader: 'ts-loader',
            options: {
              compilerOptions: {
                noEmit: false,
              },
            },
          },
        },
      ],
    },
  };

  export default commonConfig;
  ```

- 자세한 구동법 참조 : https://github.com/TypeStrong/ts-loader#getting-started

## React Refresh 구성

- `npm install -D react-refresh @pmmmwh/react-refresh-webpack-plugin`

- React Component를 런타임 중 수정하더라도 Hot Reload하는 기능을 활성화하는 플러그인 설치.
- `webpack/config.server.js` 파일에서 조작.

```js
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

const serverConfig = merge(devConfig, {
  devServer: {
    hot: true,
  },
  module: {
    rules: devConfig.module.rules.map((rule) => {
      const { test: regExp } = rule;
      if (regExp.test('.js')) {
        rule.use = [
          {
            loader: 'babel-loader',
            options: {
              plugins: [require.resolve('react-refresh/babel')],
            },
          },
        ];
      }
      return rule;
    }),
  },
  plugins: devConfig.plugins.push(new ReactRefreshWebpackPlugin()),
});

module.exports = serverConfig;
```

## Prettier 구성

- `npm install -D prettier`
- `.prettierrc.cjs` 파일에 구성한다.

```js
module.exports = {
  // 화살표 함수 식 매개변수 () 생략 여부 (ex: (a) => a)
  arrowParens: 'always',
  // 닫는 괄호(>) 위치 설정
  // ex: <div
  //       id="unique-id"
  //       class="contaienr"
  //     >
  htmlWhitespaceSensitivity: 'css',
  bracketSameLine: false,
  // 객체 표기 괄호 사이 공백 추가 여부 (ex: { foo: bar })
  bracketSpacing: true,
  // 행폭 설정 (줄 길이가 설정 값보다 길어지면 자동 개행)
  printWidth: 80,
  // 산문 래핑 설정
  proseWrap: 'preserve',
  // 객체 속성 key 값에 인용 부호 사용 여부 (ex: { 'key': 'xkieo-xxxx' })
  quoteProps: 'as-needed',
  // 세미콜론(;) 사용 여부
  semi: true,
  // 싱글 인용 부호(') 사용 여부
  singleQuote: true,
  // 탭 너비 설정
  tabWidth: 2,
  // 객체 마지막 속성 선언 뒷 부분에 콤마 추가 여부
  trailingComma: 'es5',
  // 탭 사용 여부
  useTabs: false,
};
```

- Prettier의 포멧팅에 제외하고 싶다면, 특히 빌드에 사용되는 파일들에 대해 `.prettierignore`에 무시할 폴더 및 파일들을 프로젝트 루트에 작성해준다.

```
dist
build
coverage
package-lock.json
```

## ESLint 구성 린팅!

- 공식 문서 : https://eslint.org/
- `npm init @eslint/config`로 설치하고, 설치할 때 JavaScript로 세팅하게 되는데 그럴 경우 tsx 파일들이 린팅에 잡히게 된다. 이 때, ESLint 확장이 설치되어야 하고, eslint 패키지가 글로벌 설치되어야 VS code에 표시가 된다.
- 이 린팅 오류는 `extends`, `settings`, `rules` 설정을 변경하면 해결이 가능하다.
- `eslintrc.cjs` 파일

```js
module.exports = {
  // ...
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react/jsx-runtime',
    'plugin:@typescript-eslint/recommended',
  ],
  settings: {
    react: { version: require('react/package.json').version },
  },
  rules: {
    '@typescript-eslint/no-var-requires': 'off',

    'no-console': 'warn',
    'react/prop-types': 'off',
    'react/self-closing-comp': 'warn',
    'padding-line-between-statements': [
      'error',
      { blankLine: 'always', prev: '*', next: 'return' },
      { blankLine: 'always', prev: ['const', 'let', 'var'], next: '*' },
      {
        blankLine: 'any',
        prev: ['const', 'let', 'var'],
        next: ['const', 'let', 'var'],
      },
    ],

    'import/order': [
      'warn',
      {
        pathGroups: [
          {
            pattern: '~/**',
            group: 'external',
            position: 'after',
          },
        ],
        'newlines-between': 'always-and-inside-groups',
      },
    ],
    'react/jsx-sort-props': [
      'warn',
      {
        callbacksLast: true,
        shorthandFirst: true,
        noSortAlphabetically: false,
        reservedFirst: true,
      },
    ],
  },
};
```

- ESLint 플러그인을 확장하기 위해서는 추가 패키지가 필요하다.
- `npm install -D eslint-plugin-react-hooks eslint-plugin-jsx-a11y eslint-plugin-prettier eslint-config-prettier`
- 설치 이후 ESLint 구성 파일 `.exlint.cjs`에 플러그인을 설정하고 추가 규칙을 지정한다.

```js
module.exports = {
  // ...
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react/jsx-runtime',
    'plugin:@typescript-eslint/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:prettier/recommended',
    'prettier',
  ],
  plugins: ['react', '@typescript-eslint', 'jsx-a11y'],
};
```

- 린팅을 제외하고 싶다면, 특히 빌드 파일의 경우에는 무시해야하기에 프로젝트 루트에 `eslintignore`를 작성해준다.

```
dist
build
coverage
```
