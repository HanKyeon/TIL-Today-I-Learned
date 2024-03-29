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

## Style, CSS Loader 구성

- 웹팩 환경에서는 스크립트 엔트리 파일에서 스타일을 불러와 적용해야 함.
- `public/styles` 디렉토리가 `src` 디렉토리 내부에 포함되도록 변경한 뒤, 스크립트 엔트리 파일에서 호출하는 구문을 작성해야 함.
- `src/main.jsx` or `src/main.tsx` 파일에서 `import './styles/main.css`로 추가하여 관리해야 함.
- 이 때, CSS Style code는 webpack 불러와 해석할 수 없기에 로더 패키지를 설치해줘야 한다.
- `npm install -D style-loader css-loader`
- 이후 `webpack/common.js`에 module을 추가하여 관리해야 한다.

```js
module: {
  rules: [
    // ...
    {
      test: /\.css$/i,
      use: ['style-loader', 'css-loader'],
    },
  ],
},
```

- 이런 식으로 use의 list 항목 설정만으로는 style module을 html 문서에 삽입한 것으로 끝나기에 server 운영에 적합하지 않다.
- 그렇기에 각 모듈의 소스맵이 생성되지 않아 모듈이 복잡해질 경우, 소스를 찾아 수정하기가 어렵다.
- 그렇기에 `use` 리스트 항복에 세부 옵션으로 style source map을 `webpack/common.js`에 설정해야 한다.

```js
module: {
  rules: [
    // ...
    {
		  test: /\.css$/i,
		  use: [
		    'style-loader',
		    {
		      loader: 'css-loader',
		      options: {
		        sourceMap: true,
		      },
		    },
		  ],
		},
  ],
},
```

## PostCSS Loader 구성

- `npm install -D postcss postcss-loader postcss-preset-env`
- 이후 `postcss.config.js` 생성 및 관리.

```js
module.exports = {
  plugins: [
    [
      'postcss-preset-env',
      {
        stage: 2,
        autoprefixer: { grid: true },
        features: {
          'nesting-rules': true,
          'custom-selectors': true,
        },
      },
    ],
  ],
};
```

- 이후 Webpack에도 postcss를 사용함을 알려줘야 하므로, `webpack/common.js`에 `postcss-loader`를 세팅한다.

```js
module: {
  rules: [
    // ...
    {
		  test: /\.css$/i,
		  use: [
		    'style-loader',
		    {
		      loader: 'css-loader',
		      options: {
		        sourceMap: true,
						importLoaders: 1,
		      },
		    },
		    'postcss-loader',
		  ],
		},
  ],
},
```

## CSS Module 구성

- CSS 모듈은 글로벌 CSS와 달리 고유한 키를 넣어주기에 CSS 모듈 파일을 불러오는 컴포넌트에만 적용이 된다.
- 그렇기에 `.module.css` 파일이 작동하도록 `webpack/common.js`에서 관리해줘야 한다.

```js
module: {
  rules: [
    // ...
    {
		  test: /\.css$/i,
		  use: [
		    'style-loader',
		    {
		      loader: 'css-loader',
		      options: {
		        sourceMap: true,
						importLoaders: 1,
		      },
		    },
				'postcss-loader',
		  ],
			exclude: /\.module\.css$/i,
		},
		{
		  test: /\.module\.css$/i,
		  use: [
		    'style-loader',
		    {
		      loader: 'css-loader',
		      options: {
		        sourceMap: true,
						importLoaders: 1,
						modules: {
							localIdentName: '[folder]_[local]__[hash:base64:5]',
						},
		      },
		    },
				'postcss-loader',
		  ],
			include: /\.module\.css$/i,
		},
  ],
},
```

- 이후 사용은 평소 쓰던대로 쓰면 된다.

```js
import styles from './App.module.css';

const App = () => (
  <figure className={styles.container}>
    <a
      className={styles.link}
      href="https://reactjs.org"
      rel="noopener noreferrer"
      target="_blank"
    >
      <img
        className={styles.logo}
        src="assets/react.svg"
        alt="React"
      />
    </a>
    <figcaption className={styles.description}>
      React 툴체인 매뉴얼 구성
    </figcaption>
  </figure>
);

export default App;
```

- 이 때, TypeScript를 사용하는 컴포넌트에서는 CSS 모듈의 파일 타입을 찾을 수 없다는 에러가 뜬다.
- 이것은 TypeScript가 CSS 모듈 파일을 모르기 때문이다. 따라서 `types/style.d.ts` 파일에서 CSS 모듈의 타입을 정의해줘야 한다.

```js
declare module '*.module.css' {
  const styles: { [key: string]: string };
  export default styles;
}
```

- 이후, TypeScript가 해당 파일을 알 수 있도록 `tsconfig.json`에서 루트에 추가해준다.

```js
{
  "compilerOptions": {
    // ...
    "typeRoots": ["node_modules/@types", "./src/types"],
    "plugins": [{ "name": "typescript-plugin-css-modules" }]
  }
}
```

## SASS Loader 구성

- `npm install -D sass sass-loader`
- 이후 `webpack/common.js`에 sass 모듈을 사용한다고 알려줘야 함.

```js
module: {
  rules: [
    // ...
    {
		  test: /\.(css|s[ac]ss)$/i,
		  use: [
		    'style-loader',
		    {
		      loader: 'css-loader',
		      options: {
		        sourceMap: true,
						importLoaders: 1,
		      },
		    },
				'postcss-loader',
				'sass-loader',
		  ],
			exclude: /\.module\.(css|s[ac]ss)$/i,
		},
		{
		  test: /\.module\.(css|s[ac]ss)$/i,
		  use: [
		    'style-loader',
		    {
		      loader: 'css-loader',
		      options: {
		        sourceMap: true,
						importLoaders: 1,
						modules: {
							localIdentName: '[folder]_[local]__[hash:base64:5]',
						},
		      },
		    },
				'postcss-loader',
				'sass-loader',
		  ],
			include: /\.module\.(css|s[ac]ss)$/i,
		},
  ],
},
```

- 이 때, css 모듈과 마찬가지로 sass 모듈 파일을 사용할 수 없는 경우가 있다. 동일한 방식으로 해결한다.
- 즉, `types/style.d.ts`에서 아래 설정을 추가해준다.

```js
declare module '*.module.scss' {
  const styles = { [key:string]: string };
	export default styles;
}
```

## Assets 로더 구성

- 이미지, 폰트 등의 에셋을 JavaScript 파일에서 모듈로 호출하기 위한 설정을 `webpack/common.js`에 세팅해준다.

```js
{
	//...
	output: {
    path: resolve('public'),
    filename: '[name].bundle.js',
		// 에셋 일괄 설정
    // assetModuleFilename: 'assets/[name].[contenthash][ext][query]',
  },
	module: {
		rules: [
			// ...
			{
			  test: /\.(jpe?g|png|gif|webp|bmp)$/i,
			  type: 'asset/resource',
				// 로더 별, 개별 설정
			  generator: {
			    filename: 'static/[name].[contenthash][ext][query]',
			  },
				parser: {
			    dataUrlCondition: 8 * 1024, // 8kb
			  },
			},
		],
	},
}
```

- 이 때, 다른 로더와 마찬가지로 TypeScript의 경우 호출할 때 에러가 난다. 그렇기에 `types/assets.d.ts` 파일에 타입을 선언해줘야 한다.

```js
declare module '*.jpg' {
  const url: string;
  export default url;
}

declare module '*.jpeg' {
  const url: string;
  export default url;
}

declare module '*.png' {
  const url: string;
  export default url;
}

declare module '*.gif' {
  const url: string;
  export default url;
}

declare module '*.webp' {
  const url: string;
  export default url;
}

declare module '*.svg' {
  const url: string;
  export default url;
}
```

## SVGR 로더 구성

- `npm install -D @svgr/webpack new-url-loader`
- 이후 `new-url-loader`를 통해 `webpack/dev.js`에 구성 코드를 추가한다.
- 참고 : https://github.com/marella/new-url-loader

```js
const devConfig = {
  // ...
  module: {
    rules: [
      // ...
      {
        test: /\.svg$/i,
        oneOf: [
          {
            dependency: { not: ['url'] },
            use: [
              {
                loader: '@svgr/webpack',
                options: {
                  titleProp: true,
                  svgo: true,
                },
              },
              'new-url-loader',
            ],
          },
          {
            type: 'asset/resource',
            generator: {
              filename: 'static/[name].[contenthash][ext][query]',
            },
            parser: {
              dataUrlCondition: 4 * 1024,
            },
          },
        ],
      },
    ],
  },
};
```

- SVG 사용은 아래와 같이 쓴다.

```js
import paperPlane from '../assets/paper-plane.svg'; // 파일로 import
import { ReactComponent as PaperPlane } from '../assets/paper-plane.svg'; // 컴포넌트로 import
```

```css
/* CSS에서 이미지를 불러와 사용할 경우 */
.asset-svg {
  background: url('../assets/paper-plane.svg');
}
```

- 이 또한 마찬가지로 TypeScript를 사용할 경우 문제가 생긴다.
- 마찬가지로 `types/asses.d.js` 파일에서 svg 모듈 코드를 통해 관리한다.

```js
declare module '*.svg' {
  import * as React from 'react';

  export const ReactComponent: React.FC<
    React.SVGProps<SVGSVGElement> & { title?: string }
  >;

  const src: string;
  export default src;
}
```

## 절대 경로 설정

- Webpack의 `resolve.alias` 구성을 사용해 `import`나 `require`로 호출하는 특정 모듈의 별칭을 만들 수 있다.
- 절대 경로라고 이름을 붙여줄 수 있다. `webpack/common.js`에서 관리를 하게 된다.

```js
import { resolve } from 'node:path';

const commonConfig = {
  // ...
  resolve: {
    // ...
    alias: {
      '@': resolve('src'),
    },
  },
  // ...
};
```

- vs code에서는 path intelisense 익스텐션을 통해 파일 경로 탐색이 편해질 수 있다. `.vscode/settings.json`에서 관리한다.

```js
{
	"path-intellisense.extensionOnImport": true,
	"path-intellisense.mappings": {
	  "@": "${workspaceRoot}/src",
	},
}
```

## 테스트 환경 구성

- `npm i -D jest jest-environment-jsdom babel-jest @babel/preset-typescript eslint-plugin-jest @testing-library/jest-dom @testing-library/react @testing-library/user-event`
- 설치 이후 `npx jest --init`으로 jest로 관리.
- `jest.config.js` 세팅.

```js
export default {
  clearMocks: true,

  roots: ['<rootDir>/src'],
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],

  transform: {
    '\\.[jt]sx?$': 'babel-jest',
  },
  transformIgnorePatterns: ['<rootDir>/node_modules/', '\\.pnp\\.[^\\/]+$'],

  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json'],
};
```

- jest-dom을 확장하기 위해 `jest.setup.js`을 생성해준다.

```js
import '@testing-library/jest-dom/extend-expect';
```

- `Babel`과 `TypeScript` 프리셋 구성을 위해 `@babel/preset-typescript`를 사용한다. `babel.config.js`에서 관리한다.

```js
module.exports = {
  presets: [
    ['@babel/preset-env', { targets: { node: 'current' } }],
    ['@babel/preset-typescript'],
    ['@babel/preset-react', { runtime: 'automatic' }],
  ],
};
```

- 이후 `ESLint`와 `Jest` 플러그인을 구성한다.
- `eslint-plugin-jest`를 설치하고 문서에 따라 ESLint 파일 `.eslintrc.cjs`을 작성한다.

```js
module.exports = {
  env: {
    // ...
    'jest/globals': true,
  },
  extends: [
    // ...
    'plugin:jest/recommended',
    'prettier',
  ],
  settings: {
    // ...
    jest: { version: require.resolve('jest/package.json').version },
  },
  // ...
  plugins: ['react', '@typescript-eslint', 'jsx-a11y', 'jest'],
  // ...
};
```

- 스타일, 파일, SVG 모의 구성을 한다.
- TDD 환경에서 Script File을 불러오는 **정적 Assets(이미지, css 등)은 정상처리되지 않는다.**
- TDD 환경은 시각적으로 표시되지 않으므로 정적 Assets이 잘 활용되지 않는다.
- 그렇기에 문제 없이 테스트가 수행될 수 있도록 **mock 구성**이 필요하다. CSS와 Sass 모듈의 경우 `className`의 조회가 필요하기에 `Proxy`를 구성해야 한다.
- `npm install -D identity-obj-proxy`. ES6 프록시를 사용해 스타일 파일을 mocking하기 위한 패키지.
- `src/__mocks__/styleMock.js`에 스타일 모킹을 해주고, `src/__mocks__/fileMock.js`에는 파일 등의 모킹을 해주며, `src/__mocks__/svgMock.js`에서는 `SVG` `SVGR` 컴포넌트 모킹을 해준다.

```js
// Style Mocking
import idObj from 'identity-obj-proxy';
export default idObj;
// File Mocking
export default 'test-file-stub';
// SVG Mocking
export default 'SvgrURL';
export const ReactComponent = 'div';
```

- 이후 `jest.config.js`에 `moduleNameMapper` 항목에 모킹 파일을 연결해준다.

```js
export default {
  // ...
  moduleNameMapper: {
    '\\.(css|s[ac]ss)$': '<rootDir>/src/__mocks__/styleMock.js',
    '\\.(ico|jpg|jpeg|png|gif|eot|otf|webp|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$':
      '<rootDir>/src/__mocks__/fileMock.js',
    '\\.svg$': '<rootDir>/src/__mocks__/svg.js',
  },
};
```
