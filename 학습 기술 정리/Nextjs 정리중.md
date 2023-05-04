# NextJS 정리

학습 후기 : **학습중... 0410 시작**

## issue

1. SSR 부분에서 redux persist / next redux wrapper / redux toolkit 세가지를 함께 쓰는 것에 어려움을 느꼈음.
   - 이유는 주로 ssr에서 토큰을 사용 할 때가 문제였음.
   - 그렇기에 token이 필요한 request의 경우, private한 api로 정하고, 해당 api를 ssr에 올려두지 않는 것이 좋다고 생각함.
   - ssr을 할 부분과 하지 않을 부분을 명확하게 나누는 것이 중요하다고 생각함.

## WHY?

- File-based Routung & Page Pre-rendering. 파일 기반 라우팅, 페이지 사전 렌더링.
- 프로젝트에 api를 추가하고 api를 추가해서 데이터 가져오기 기능.

## WHAT?

- The React Framework for the Web
- React 최신 버전, Rust based의 강력한 JS 툴.

## HOW?

1. File-based Routing

- 기본적으로 \_app.ts와 같은 위치에 있는 index를 렌더링 한다. `/` 라우팅.
- 중첩 라우팅의 경우, 폴더를 만들고 해당 폴더의 index.js는 `/해당폴더명` 라우팅을 갖게 된다.
- 해당 폴더의 파일 이름을 만들 경우, `/해당폴더명/파일이름` 의 라우팅을 갖게 된다.
- 폴더 명을 `[]`를 통해 다이나믹 라우팅 하고, index.ts를 주어도 정상 작동 한다. 해당 방식을 통해 다이나믹 라우팅을 nested 시킬 수 있다.
- 다이나믹 라우팅의 경우, 대괄호를 이용하면 된다. (참조 : https://nextjs.org/docs/routing/dynamic-routes)
- `pages/blog/[slug].js` => `/blog/:slug`
- `pages/post/[...all].js` => `/post/*`
- 이 때 해당 라우팅의 쿼리 파라미터나 다이나믹 라우팅을 받아오고 싶은 경우에는 `useRouter()` 훅을 이용한다.
- `useRouter()` 훅의 리턴을 router에 할당하고 `router.push()`를 이용해 이동이 가능하다.

```js
import Link from 'next/link';
import { useRouter } from 'next/router';

function Home() {
  const router = useRouter();
  // => router.query.pid 등으로 읽을 수 있음.
  // 초기에는 undefined 이지만, 렌더링이 된 후에 파라미터의 값이 읽어진다.
  // 이후 데이터를 fetching 하는 등  데이터를 받아온 이후 해당 값을 이용 할 수 있음.
  return (
    <ul>
      <li>
        <Link href="/post/abc">Go to pages/post/[pid].js</Link>
        {/* 이 경우 pid에 abc가 할당. */}
      </li>
      <li>
        <Link href="/post/abc?foo=bar">Also goes to pages/post/[pid].js</Link>
        {/* 이 경우, pid에는 abc가 할당되고, foo에는 bar가 할당됨. */}
      </li>
      <li>
        <Link href="/post/abc/a-comment">
          Go to pages/post/[pid]/[comment].js
          {/* 이 경우 pid에는 abc, comment에는 a-comment가 문자열로 할당. */}
        </Link>
      </li>
      <li>
        <Link href="/post/a/b/c">
          Go to pages/post/[...slug].js
          {/* 이 경우 slug에 배열 형태로 ["a", "b", "c"] 가 할당. */}
        </Link>
      </li>
    </ul>
  );
}

export default Home;
```

2. SEO (Search Engine Optimization) 검색 엔진 최적화

- SSG 혹은 SSR을 통해 SEO가 가능하다.

  1. SSG
     - SSG에서는 getStaticProps 함수를 선언해서 props를 받아올 수 있다.
  2. SSR
     - SSR에서는 getServerSidePRops를 선언해서 props를 받아올 수 있다.

  - 양쪽 다 getStaticPaths가 가능한 것으로 암.

3. NextJS + Redux

- 추후 정리 예정

- NextJS는 빌드 과정에서 처리하거나 서버측에서 만들어서 보내줘야 하기에, 어떤 브라우저가 어떤 store를 참조하고 있는지 모르기 때문에 redux-next-wrapper 라이브러리를 통해 redux를 사용 할 수 있도록 해준다.
- wrapper 객체가 필요함. wrapper를 export해서 app에서 component를 감싸주어서 한다.
- 옛날 버전에서는 withRedux를 썼는데 props에서 특정 훅을 통해 store와 props를 받아서 할당하고 provider에 주입한다.
- 그렇게 되면 getServerSideProps 혹은 getStaticProps에서 store의 사용이 된다.

4. NextJS + React Query

- 추후 정리 예정

- SSG에서는 initialData를 활용한다.
- 세팅은 app에서 해주며, 이전 버전과 다른 특이점은 getServerSideProps 혹은 getStaticProps의 경우에서는 QueryClient를 선언해서 사용한다.
- app의 메인에서는 useState를 이용해 state에 QueryClient 객체를 담아 provider의 client에 주입해주고 dehydrate state를 주입해준다.
- 해당 부분에서 실제로 사용해봐야 알 것들이 많은 것 같다.

## WHAT IF?

- 참조한 강의에서 찝은 세가지 장점은 첫째, File-based Routing, SSR을 통한 Search Engine Optimization, 쉽고 강력한 Fullstack app build
- 개인적으로는 File-based Routing을 통해 boilerPlate를 줄일 수 있다는 점이 강점이라 생각함.
- 또한, SSR을 통한 SEO 개선 역시 강한 이점. 노출이 필요한 부분은 SSR을 이용하고, 필요 없는 경우에는 SPA를 이용하면 좋을 것으로 보인다.

## 만난 문제

1. 페이지 이동 시 store가 초기화됨 : https://hoons-up.tistory.com/68

   - 일반적으로 redux-persist를 사용해 유지시킴.
   - extrareducers를 통해 유지한다.
   - redux toolkit + nextjs + redux-persist : https://velog.io/@baemki/Next.js-redux-toolkit-redux-wrapper-redux-persist-%EC%84%B8%ED%8C%85

2. next/image 의 Image 태그 width height alt src는 required이고, 외부 API의 경우 proxy를 통해 변환해야 한다.

   ```js
   /** @type {import('next').NextConfig} */
   const nextConfig = {
     reactStrictMode: true,
     images: {
       remotePatterns: [
         {
           protocol: `https`,
           hostname: `figma-alpha-api.s3.us-west-2.amazonaws.com`,
           port: ``,
           pathname: `/images/**`,
         },
       ],
     },
   };
   ```

   - 위처럼 작성하면 해당 호스트네임의 path가 /images/모든 것을 받아준다...

3. 외부 API를 가져올 때, CORS 에러가 난다. axios의 proxy는 포트를 반드시 받아야 하기 때문에, rewrites를 재작성하여 관리하거나, API Routes로 우회해서 받아줄 수 있다.
   - 따라서, api routes에서 req에서 내용이 어떻게 나오는지 좀 알아야 할 것 같다.
