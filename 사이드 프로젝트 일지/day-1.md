## 모노레포 프로젝트 구성

1. 환경
   - `pnpm`과 `vite`를 메인으로 구성하기로 함.
   - `pnpm`은 속도가 빠르며 프로젝트가 커질수록 속도의 개선이 확실하기에 사용하기로 함.
   - `vite`는 그냥 쓰고 싶어서 쓰기로 함. 장점들은 충분할 것으로 봄. `console.log`를 지워준다거나, 코드 스플리팅을 도와준다거나 하는 등에서 이점이 있다. 또한, 최신 유행하는 기술이기에 사용해보고 싶어서 사용하기로 함.
2. packages 전략
   - `frontend`
     1. 메인 사이트를 담당하게 될 폴더. 이름을 모르겠어서 걍 `frontend`라 지정
   - `core`
     1. 프로젝트에서 공용으로 사용 될 `utils`가 들어갈 예정
     2. 코어 라이브러리를 커스텀한 코드가 들어가게 될 것.
   - `api-request`
     1. `axios`의 인스턴스가 들어갈 것.
     2. 추가적으로, `react-query`를 통해 이뤄지는 `hooks`가 정리되어 들어갈 예정.
   - `ui`
     1. 공통으로 자용되는 ui 컴포넌트들이 들어갈 예정.
     2. 아토믹하게 사용하는 방법과 완성된 컴포넌트를 제공하는 두가지 기능을 함께 제공할 예정
3. eslint 및 tsconfig 구성

   1. `workspace root`의 `eslint.cjs`

      - `@tanstack/query`의 `eslint`를 그대로 가져왔다. 특정 부분에서 필요한 내용이 있다면 관리 할 예정
      - 또한, 제대로 하나하나 뜯어보고 가져온 것이 아닌, 일단 긁어온 것이기에 한 줄 한 줄 제대로 정리하며 학습해야 할 것이다.

      ```js
      // eslintrc.cjs
      const config = {
        root: true,
        parser: '@typescript-eslint/parser',
        plugins: ['@typescript-eslint', 'import'],
        extends: [
          'plugin:@typescript-eslint/eslint-recommended',
          'plugin:@typescript-eslint/recommended',
          'plugin:import/recommended',
          'plugin:import/typescript',
          'prettier',
        ],
        env: {
          browser: true,
          es2020: true,
        },
        parserOptions: {
          tsconfigRootDir: __dirname,
          project: './tsconfig.base.json',
          sourceType: 'module',
          ecmaVersion: 2020,
        },
        settings: {
          'import/parsers': {
            '@typescript-eslint/parser': ['.ts', '.tsx'],
          },
          'import/resolver': {
            typescript: true,
          },
          react: {
            version: 'detect',
          },
        },
        rules: {
          '@typescript-eslint/ban-types': 'off',
          '@typescript-eslint/ban-ts-comment': 'off',
          '@typescript-eslint/consistent-type-imports': [
            'error',
            { prefer: 'type-imports' },
          ],
          '@typescript-eslint/explicit-module-boundary-types': 'off',
          '@typescript-eslint/no-empty-interface': 'off',
          '@typescript-eslint/no-explicit-any': 'off',
          '@typescript-eslint/no-non-null-assertion': 'off',
          '@typescript-eslint/no-unnecessary-condition': 'error',
          '@typescript-eslint/no-unused-vars': 'off',
          '@typescript-eslint/no-inferrable-types': [
            'error',
            { ignoreParameters: true },
          ],
          'import/default': 'off',
          'import/export': 'off',
          'import/namespace': 'off',
          'import/newline-after-import': 'error',
          'import/no-cycle': 'error',
          'import/no-duplicates': 'off',
          'import/no-named-as-default-member': 'off',
          'import/no-unresolved': ['error', { ignore: ['^@tanstack/'] }],
          'import/no-unused-modules': ['off', { unusedExports: true }],
          'import/order': [
            'error',
            {
              groups: [
                'builtin',
                'external',
                'internal',
                'parent',
                'sibling',
                'index',
                'object',
                'type',
              ],
            },
          ],
          'no-redeclare': 'off',
          'no-shadow': 'error',
          'sort-imports': ['error', { ignoreDeclarationSort: true }],
        },
        overrides: [
          {
            files: ['**/*.test.{ts,tsx}'],
            rules: {
              '@typescript-eslint/no-unnecessary-condition': 'off',
            },
          },
        ],
      };

      module.exports = config;
      ```

   2. `workspace root`의 `tsconfig.base.json`

      - 마찬가지로, `@tanstack/query`의 틀을 가져왔음.
      - 다른 부분은 `no-unused-vars` 옵션을 전부 `warn` 혹은 `off`로 적용하기로 했음. 추후에 `on`으로 바꿔 마무리할 예정이다.

      ```json
      {
        "compilerOptions": {
          "target": "ES2020",
          "useDefineForClassFields": true,
          "lib": ["ES2020", "DOM", "DOM.Iterable"],
          "module": "ESNext",
          "skipLibCheck": true,

          /* Bundler mode */
          "moduleResolution": "bundler",
          "allowImportingTsExtensions": true,
          "resolveJsonModule": true,
          "isolatedModules": true,
          "noEmit": true,
          "jsx": "react-jsx",
          "allowJs": true,

          /* Linting */
          "strict": true,
          "noImplicitAny": false,
          "noUnusedLocals": false,
          "noUnusedParameters": false,
          "noFallthroughCasesInSwitch": true,

          // null check를 열심히 해서 클린 코드를 써보자
          "noUncheckedIndexedAccess": true,
          "strictNullChecks": true,
          "baseUrl": ".",
          "paths": {
            "@book/core": ["packages/core/src"],
            "@book/frontend": ["packages/frontend/src"],
            "@book/ui": ["packages/ui/src"],
            "@book/api-request": ["packages/api-request/src"]
          }
        }
      }
      ```

4. prettier 구성

   - 기존에 쓰던 내용 그대로 가져옴. 에어 비앤비 유사하게 관리한 prettier임

5. 추후 진행해야 할 것들
   - `npm`에 `publish` 진행하여 제대로 작동하는지 확인
   - 배포하여 확인하기
   - 필요한 상황에 따른 코드 스플리팅
   - `@types`로 묶어줘야 하는지 결정하여 관리하면 좋을 것으로 보임.

:warning: 우선, 제대로 동작하는지 dev server를 돌려본 것은 아님. 그렇기에 진행하며 생기는 `side effect`들을 정리하고 관리해야 함

---

참고 링크 정리

- 모노레포에 테일윈드 넣기 : https://jasonkang14.github.io/react/monorepo-with-tailwind
- 리액트 쿼리 깃 : https://github.com/HanKyeon/query
- 제스트 + 테스팅 라이브러리 : https://gatsbybosungblogmain.gatsbyjs.io/tdd2/
- eslintrc 관련 : https://www.daleseo.com/eslint-config/
- eslintrc 관련2 : https://blog.pumpkin-raccoon.com/79
- package의 esbuild 관련 : https://esbuild.github.io/api/#platform
- pnpm + vite : https://luvstudy.tistory.com/188
- 모노레포 린팅 및 tsconfig 등 공통 모듈 빌드 : https://bepyan.github.io/blog/dev-setting/pnpm-monorepo
- yarn berry를 로컬로 사용하는 모노레포 세팅 : https://minify.tistory.com/40
- npm audit && npm fund 에러 관련 : https://velog.io/@gth1123/npm-fund-npm-audit-fix
- 깃헙 팀프로젝트 만들기 : https://xively.tistory.com/17
