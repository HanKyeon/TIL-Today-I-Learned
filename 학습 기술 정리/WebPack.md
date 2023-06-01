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
