# TypeScript 정리

학습 후기 : **학습중... 0410 시작**

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

```js
import Link from "next/link"
import { useRouter } from "next/router"

function Home() {
  const router = useRouter()
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
  )
}

export default Home
```

## WHAT IF?

- 참조한 강의에서 찝은 세가지 장점은 첫째, File-based Routing, SSR을 통한 Search Engine Optimization, 쉽고 강력한 Fullstack app build
- 개인적으로는 File-based Routing을 통해 boilerPlate를 줄일 수 있다는 점이 강점이라 생각함.
- 또한, SSR을 통한 SEO 개선 역시 강한 이점. 노출이 필요한 부분은 SSR을 이용하고, 필요 없는 경우에는 SPA를 이용하면 좋을 것으로 보인다.
