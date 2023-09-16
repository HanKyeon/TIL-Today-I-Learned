1. `@vitejs/plugin-react`와 `@vitejs/plugin-react-swc`의 차이

   - `swc`쪽이 `swc`+`esbuild`를 써서 dev에서 속도가 빠르다는 것임.
   - 근데 자꾸 내컴에서는 `swc`가 오류가 남. 일반 `@vitejs/plugin-react`를 사용하기로 함. dev server의 속도이며, 그렇게 큰 차이는 보이지 않을 것으로 예상.

2. tsconfig 및 eslintrc, package.json의 module과 main의 경우

   - module: require를 사용하지 않았을 때 자동으로 module을 바라본다. (esm)
   - main : require를 사용한 경우 main을 바라보게 한다.
   - 해당 내용들은 모두 build 이후에 바라보게 된다.
