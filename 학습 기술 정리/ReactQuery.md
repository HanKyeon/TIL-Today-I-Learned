## React Query 정리

- 학습 후기
  **리액트 쿼리 진짜 좋은 듯!!! 이전 프로젝트에서 servserState의 상태 관리를 redux로 했을 때, 꼬이는 경험을 했는데 React Query를 사용하게 되면 그럴 일이 없어질 것이다.**
- 학습 진행 버전 : 3.39.3 => 4.28.0
- 이후 업그레이드 예정 => 5버전

- 3버전에서 4버전으로 가며 바뀌는 것

0. QueryKey의 형태가 문자열도 가능 => 오직 배열만 가능으로 변경.
1. import 위치가 react-query에서 @tanstack/react-query로 변경
2. isLoading이 isInitialLoading으로 변경되었음.
3. onSuccess가 캐싱된 데이터를 가져오더라도 실행되도록 변경. 기존 3버전에서 캐시에서 data를 가져오는 것은 데이터의 변경으로 보지 않았기에(캐싱 데이터의 변경이 일어나지 않음), 이제 data의 변경에 따라 무언갈 행하고 싶다면 useEffect를 사용하고 배열에 data를 넣어주면 된다고 함. (기존에는 onSuccess가 실제 data를 가져올 때만 실행되었기에, data가 변경 될 때 실행되는게 확실헀으나, 이제는 캐싱에도 작동을 하기에 달라진 부분 같음.)
4. SSR의 경우, 데이터 캐싱 유효성 기간을 무제한으로 기본 세팅.
5. QueryClientProvider의 import 폴더 명이 react-query에서 react-queryjs로 변경.
6. useMutation의 경우, 인자가 바로 옵션으로 변경. 옵션의 `mutationFn` 으로 `function() {return axios({...})}` promise를 반환하는 함수를 넣어준다.

---

세팅

설치
`npm install react-query` => `npm install @tanstack/react-query @tanstack/react-query-devtools`

이후 index.tsx
`const queryClient = new QueryClient({defaultOptions: {queries: {}, mutations" {}}})`

사용 할 쿼리 클라이언트 객체 생성
`<QueryClientProvider client={queryClient}></QueryClientProvider>`

위의 컴포넌트로 App 컴포넌트를 둘러싸 App에서 사용 할 쿼리 클라이언트를 알려주면 세팅 끝.

테스팅

`npm install @testing-library/react-hooks react-test-renderer --save-dev`
테스트에 testing-library 디펜던시를 가진다.
retry를 false로 해야 진행이 가능하다.
QueryClient의 Network error logging을 꺼야한다.

Jest와 함께 쓰려면 cacheTime을 Infinity로 설정한다.

---

### WHY?

- 기존 redux의 경우, 비동기 통신을 위한 상태 관리 툴이 아니다.
- 그래서 비동기 통신을 위한 boiler plate가 두껍고, 실제로 비동기 통신이 이루어졌을 때 state가 최신이라는 보장이 되지 않고, 예측 가능성이 높지 않았다.
- 그것을 해결하기 위해 등장한 라이브러리.

---

### WHAT?

- 상태를 server state와 client state로 구분하고, server state의 관리를 도와주는 라이브러리
- unique key를 통해 QueryClientProvider 내부에서 같은 unique key를 가진다면 굳이 모아서 선언하지 않아도 알아서 캐싱해주고 데이터를 fetching 해줌.
- 추가로, 동시에 같은 요청이 많이 간다면 그것도 필터링 해준다.

---

### HOW?

- useQuery의 경우, get 처럼 server state에 변화가 없을 때 사용. 타입 지정은 useQuery<데이터타입>() 형태로 지정.
- useMutation의 경우, post put delete 등 server state에 변화가 있을 때 사용.
- useQuery와 useMutation을 Hook으로 모아서 API마다 관리를 하는 것으로 보인다.
- API 정리가 깔끔할수록 작동하기 좋아보인다. => 쿼리 키 설계를 통해 해결.

- useMutation은 mutate와 mutateAsync를 반환하는데, 데이터 통신 및 invalidate만 할 것이라면 mutate를 한 뒤 접근을 Query로 하는 것이 좋아보인다. mutateAsync를 사용한다면, 훅에서 onSuccess를 달아주는 것이 아닌, 내부에서 직접적으로 처리를 해야 할 경우 사용하면 될 것 같다.
- 즉, mutateAsync는 useMutation을 규격화 한 경우에 성공/실패 등에서 실행 할 함수를 결정하는 방식으로 사용하고, mutate를 기본으로 쓸 때 쓰면 될 것 같다. 직접 데이터 가공은 좋지 못하다 생각한다.
- mutateAsync는 Promise 객체를 내보낸다.
- mutation의 onSuccess는 약간 proxy 개념인 것 같음. onSuccess에 달아둔 쿼리invlidate는 mutateAsync에서나 mutate에서나 실행됨.

- 아래는 내가 사용하는 형태이다. React Hook의 형태로 queries를 관리한다.

```ts
// 현재 사용하고 있는 형태.
// options 객체에 queryKey와 queryFn을 통해 사용한다.

// 반환되는 Data 타입
interface User = {}

// useQuery를 규격화 한 CustomHook
const useUserData = function () {
  return (
    useQuery <User>{
      queryKey: queryKeys.user(),
      queryFn: async function () {
        return apiRequest({
          method: `get`,
          url: `/api/member`,
        }).then((res) => res.data)
      },
    }
  )
}
```

```js
const useGetUserData = function (/* 필요한 정적인 파라미터 */) {
  return useQuery(
    /* unique key 값. 이 값으로 QueryClientProvider에서 server state를 관리하는 것으로 보인다. */
    [`user`], // 특정 값(id 등)으로 캐싱을 원할 때는 배열 형태로 사용. [`user`, 15] 이런 식으로.
    /* async는 선택. 대다수 찾아본 글에서는 사용하지 않았음. */ function () {
      return /* await는 선택. 대다수 찾아본 글에서는 사용하지 않았음. */ axios({
        method: `get`,
        url: `asdfaf`,
      }).then((res) => res.data) // res를 반환해도 좋고 res.data를 반환해도 좋음. but 디스트럭쳐링으로 받을 때 data 라는 이름으로 받아지며, res를 반환할 경우 data.data로 접근해야하기에 바로 data로 반환해줌.
    },
    {
      // 옵셔널 데이터들이 들어가면 됨.
      onSuccess: function (data) {
        // 성공 시 처리 할 함수
        console.log(data)
      },
      onError: function (err) {
        // 실패 시 처리 할 함수
        console.log(data)
      },
    }
  )
}
```

```js
const usePutUserData = function (/* 필요한 정적인 값 */) {
  const queryClient = useQueryClient() // 현재 사용중인 queryClient 객체를 가져오는 것 같음!
  return useMutation(
    function (/* 객체를 받고 싶다면 여기에 넣으면 될 듯. */) {
      return axios({ 객체 })
    },
    {
      onSuccess: function () {
        queryClient.invalidateQueries([`user`]) // user를 unique key로 가진 쿼리에 변경이 생겨 invalid 시켜줌.
      },
      onError: function () {
        console.log("하이요 실패에요")
      },
    }
  )
}
```

```js
// 사용법

// get을 쓰는 useQuery의 경우, hook으로 선언되었기에 이런식으로 선언만 하면 사용 가능.
// 이렇게 되면 `user` key로 get 해오는게 자동으로 된다. 기존에는 useEffect를 통해 데이터를 가져와서 redux || state에 저장하고 사용해야 하지만, data 자체가 data가 된다.
const { isLoading, error, data } = useGetUserData() // isFetching 등 다양한 값이 있으니 필요한 것을 쓰면 됨.
// 훅을 사용하지 않는다면, 아래와 같이 작성.
const { isLoading, error, data } = useQuery([`user`], function () {
  return (
    axios({
      /* AxiosRequestConfig */
    }).then((res) => res.data),
    { onSuccess: function () {}, onError: function () {} }
  )
})

// put post delete 등 server state에 변화를 주는 경우, useMuation을 사용한다.
// 훅을 선언한 경우, 아래와 같이 작성해서 쓰면 됨.
const { mutate, mutateAsync } = usePutUserData() // 이 둘 외에도 많은 것들이 있음.
mutate() // 함수의 인자 값을 받았다면 여기서 넣어주면 된다.
const a = mutateAsync() // Promise 객체를 반환하는 mutateAsync. 하지만 data를 가공 했을 때 server state에 적용이 안되므로, 사용을 지양하는 것이 좋아보인다.
// hook을 사용하지 않는 경우
const queryClient = useQueryClient()
const { mutate, mutateAsync } = useMutation(
  function () {
    return axios({
      /* AxiosRequestConfig */
    })
  },
  {
    /* 옵션 객체+ */
    onSuccess: function () {
      queryClient.invalidateQueries("user")
    },
  }
)

// useQueries
const queries = useQueries(
  books.map((book) => {
    return {
      queryKey: [`book`, book.id],
      queryFn: () => axios({}),
    }
  })
)
```

- setQueryData 및 setQueriesData

쿼리 값을 임의로 정하겠다면 setQueryData 혹은 setQueryKey 등을 사용하면 된다.

```js
const queryClient = useQueryClient()

// data는 저장 할 정보
queryClient.setQueryData([`user`, `list`], { filter: `me` }, data)
// 내 아이디와 같은 모든 목록 업데이트.
queryClient.setQueriesData([`user`, `list`], (prev) =>
  prev.map((user) => (user.id === me.id ? data : user))
)
// 모든 유저 리스트 invalidate
queryClient.invalidateQueries([`user`, `list`])

// 현재 사용중인 값을 즉시 업데이트
queryClient.setQueryData(["todos", "detail", newTodo.id], newTodo)

// 현재 사용중인 값이 담긴 리스트를 즉시 업데이트.
queryClient.setQueryData(["user", "list", { filter }], (previous) =>
  previous.map((user) => (user.id === newTodo.id ? newtodo : user))
)
// 리스트를 invalidate 시키지만 refetch 하지 않음
queryClient.invalidateQueries({
  queryKey: ["user", "list"],
  refetchActive: false,
})
```

- 쿼리 키 관련

1. 쿼리 키는 어차피 내부적으로 배열로 관리되기에, `["user", "list", {filter: "me"}]` 이런 형태로 키를 작성하는 것이 좋다.
2. 쿼리 키를 종속적으로 한 번에 invalidtate 시킬 때, 편리하다.
3. 쿼리 키를 객체 형태로 관리하면 좋을 것이다. 수동으로, 하드코딩으로 작성하면 유지보수가 어렵기 때문.
4. 그렇기에 하나의 기능 당 하나의 key를 객체 형태로 관리하길 권장한다.

```js
{
  ['user', 'list', { filter: 'me' }],
  ['user', 'list', { filter: 'you' }],
  ['user', 'profile', 1],
  ['user', 'profile', 2],
}
```

참고한 글에는 아래처럼 작성되어 있다.

```js
const todoKeys = {
  all: ['todos'] as const,
  lists: () => [...todoKeys.all, 'list'] as const, // todoKeys.lists() 하면 [`todos`, `list`] 반환
  list: (filters: string) => [...todoKeys.lists(), { filters }] as const, // todoKeys.list(필터) 하면 [`todos`, `list`, {필터: 필터}] 반환.
  details: () => [...todoKeys.all, 'detail'] as const, // todoKeys.details() 하면 [`todos`, `detail`] 반환
  detail: (id: number) => [...todoKeys.details(), id] as const, // todoKeys.detail(필터) 하면 [`todos`, `detail`, {필터: 필터}] 반환.
}
```

위를 이용하면 아래와 같이 사용이 가능하다.

```js
// 🕺 모든 todos 삭제
queryClient.removeQueries(todoKeys.all)

// 🚀 모든 리스트 invalidate
queryClient.invalidateQueries(todoKeys.lists())

// 🙌 prefetch 하나의 todo
queryClient.prefetchQueries(todoKeys.detail(id), () => fetchTodo(id))
```

---

### WHAT IF?

- 상태를 Client / Server로 나누어 관리하기 편해진다. 그래서 Redux의 경우, 전역적인 상태가 아니라 지역적으로 사용하기 더욱 편해지고 비동기로부터 자유로워진다.
- Server State의 캐싱과 최신화를 쉽게 해주며, server state의 최신화 데이터를 라이브러리가 보장해준다.
- 카카오 페이 테크에서는 불필요한 코드의 감소, 업무와 협업의 효율성을 위한 규격화된 방식 제공, 사용자 경험 향상을 위한 다양한 빌트인 기능 세가지의 강점을 꼽았다. 또한 Concurrent UI Pattern의 개념을 도입 할 때 도우밍 되었다고 한다. (https://tech.kakaopay.com/post/react-query-2/)

---

### 추가 정보

**0. 정보를 적어둘테니 상세 사항은 ReactQuery Docs를 확인 바람. https://react-query-v3.tanstack.com/overview**

1. unique key 값을 배열 형태로 하여 [`book`, 12] 이런 식으로 캐싱이 가능하다. 숫자 말고도 객체로도 가능하다. 이해가 어렵다면 useEffect useMemo useCallback의 dependency array를 생각하면 됨.
2. query Function이 들어가는 부분의 경우 axios가 아닌, fetch API 등을 사용 할 수 있음.
3. Dependent Queries로 디벤던시를 지정이 가능하다고 안다.
4. options의 select를 통해 원하는 data 형태 가공이 가능하다.. 고 들었음
5. useQueries를 통해 여러개의 query를 함께 fetch가 가능하다.
6. index.tsx 혹은 app.tsx에서 QueryClient 객체를 생성 할 때 여러가지 옵션을 설정 할 수 있다. queries의 retry 횟수나 에러 바운더리 처리, window Focus Refetching option, infinite queries, paginated queries 등등.
7. 독스에 자료 다 있다.
8. 쿼리 클라이언트에 setQueryData 속성으로 쿼리 캐싱이 가능한듯. 그래서 mutation에 달아줄 수 있음.
9. 쿼리 캔슬도 가능함.
10. filter, testing, suspence, scroll, ssr 등 다양한 기능이 많다! Docs를 보자!
11. mutate나 mutateAsync나 옵션값이 실행된다. mutateAsync로 데이털르 건드리지 말고, 이후 옵션적으로 실행 될 onSuccess 옵션이나 그런걸 적어주는 형태로도 사용이 가능하다.

---

### 참고 자료

https://react-query-v3.tanstack.com/overview => ReactQuery Docs
https://tech.kakaopay.com/post/react-query-1/ => 카카오 테크 블로그 글
https://tech.kakaopay.com/post/react-query-2/ => 카카오 테크 블로그 글 2
https://tech.kakao.com/2022/06/13/react-query/ => Concurrent UI Pattern에 React Query를 사용했다고 해서 참고 예정

https://velog.io/@familyman80/React-Query-%ED%95%9C%EA%B8%80-%EB%A9%94%EB%89%B4%EC%96%BC
https://www.zigae.com/react-query-key/
https://velog.io/@dev_jazziron/react-query-querykey
https://velog.io/@kerem119/React-Query

https://pebblepark.tistory.com/29
https://github.com/ssi02014/react-query-tutorial

### 나는 어떻게 써야 할까?

1. get 요청 같은 경우, hook으로써 불러오기.
2. post, put, delete 등 mutation도 훅으로 쓰고 싶긴 한데 한 번 값을 조정해서 사용해보기.
3. query key들을 모아서 관리하면 좋을 것 같다. 그래서 API가 깔끔하면 query key가 겹치는 경우가 적을 것이고, 이점이 많을 것이다.

### 쿼리 키 관리 형태

쿼리 키 관리

```js
const queryKeys = {
  ////////////
  /* 최상단 */
  ////////////
  user: () => [`user`],
  scene: (taleId, sceneOrder) => [...queryKeys.user(), taleId, sceneOrder], // 최상단

  ///////////////
  /* user 하위 */
  ///////////////
  game: () => [...queryKeys.user(), `game`],
  store: () => [...queryKeys.user(), `store`],

  ///////////////
  /* game 하위 */
  ///////////////
  progress: () => [...queryKeys.game(), `progress`],
  play: () => [...queryKeys.game(), `play`],

  ///////////////////
  /* progress 하위 */
  ///////////////////
  progressList: () => [...queryKeys.progress(), `list`],
  progressDetail: (taleId) => [...queryKeys.progress(), `detail`, taleId],

  ///////////////////
  /* play 하위 */
  ///////////////////
  playList: () => [...queryKeys.play(), `list`],
  playDetail: (taleId) => [...queryKeys.play(), `detail`, taleId],

  ////////////////
  /* store 하위 */
  ////////////////
  storeList: () => [...queryKeys.store(), `list`],
  storeDetail: (taleId) => [...queryKeys.store(), `detail`, taleId],
  reviewList: (taleId) => [...queryKeys.storeDetail(taleId), `reviews`],
}
```

## 추가 내용

### 캐싱 관련

https://darrengwon.tistory.com/1517

- 언제 데이터가 cache되는가? => query를 보내고 데이터를 받아오자마자 cache된다. 그러나 cacheTime은 이 때 발동하지 않는다.
- 그렇다면 cacheTime은 언제부터 시작인가? => unmount된 시점부터. 즉, inactive된 시점부터 시작한다.
- cacheTime이 지나기 전에 다시 쿼리가 발동되면 어떻게 되는가? => cache된 값을 사용하고 background에서 다시 fetching된다.
- cacheTime이 지나면 어떻게 되는가? => 메모리에 존재하는 데이터가 GC에 의해 삭제. 따라서 다시 active되면 hard loading한다.
- cacheTime이 0이라면 어떻게 되는가? => 매번 GC 당하므로 매번 hard loading을 하게 된다.

### 에러 핸들링

- invalidate 되더라도 에러가 뜨면 캐싱된 값을 가져온다.
- removeQueries를 통해 캐싱된 값도 지워주면 된다. 특히, 로그아웃.

### Docs 읽기

- React Query Kit이 있는데 아무래도 보니 ssr쪽에 잘 쓰일거 같음. 예시가 page의 캐싱을 쿼리해둔다.
- useQueries에서 인자로 배열을 받아서 여러개의 쿼리를 받았으나, 새롭게 options에 queries에 배열을 넣어주면 된다.

### Docs를 보며 정리 및 사용 경험 연관 정리 - 추후에 사용해보고 재정립 하자.

1. 개발자 도구 되게 잘 되어있었음. 단, 화면이 깨질 수 있었음.
2. 리액트 쿼리는 에러가 없다..... 뜨면 isError나 error로 알려줌. 뭔가 잘못되면 내 탓임
3. useIsFetching 훅을 사용하면 글로벌에서 페칭을 걸어줄 수 있다.
4. window focus refetching은 useQuery의 options에 refetchOnWindowFocus라는 값을 false로 변경해주면 된다.
5. setData로 쿼리키에 값을 직접 캐싱이 가능하다.
6. enabled를 통한 lazy query를 사용해보고 싶다. 일반적으로 filter에 !!filter를 enabled로 넣어 처리하는 것 같음. 로딩이 되고 나서 쿼리로 받아오게 하려고.
7. pause Queries가 가능하다. 쿼리를 자동으로 허갈하지 않기 위해서는 enabled 값을 false로 주면 된다. 그렇게 되면 state가 success가 되거나 isSuccess state가 완료된다. 캐싱 데이터가 없을 경우, status는 쭉 로딩이 되고, fetchStateus는 idle이 된다.
8. enabled값이 false라면 쿼리가 마운트 될 때 자동 fetch 되지 않는다. background에서 자동으로 refetch되지 않는다.
9. enabled 값이 false라면 일반적으로 선언되는 invalidateQueries와 refetchQueries를 무시한다.
10. useQuery에서 리턴하는 refetch는 쿼리를 fetch하는 트리거로 사용된다.
11. retry 옵션은 false라면 재시도하지 않고, 숫자라면 해당 횟수만큼하고, true라면 무한히 요청한다. (failureCount, error) => {} 형태라면 실패 했을 때 retry를 해당 함수로 진행한다.
12. retryDelay 옵션은 30초 이내의 숫자로 사용이 가능하다. 단위는 ms.
13. paginated Queries & Lagged Queries => 각각의 쿼리는 완전히 새로운 쿼리로 취급되며, success와 loading의 status를 왔다갔다 한다.
14. paginatedQueries는 아무래도 ssr에서 사용하는 것 같은데...

```js
// docs의 예시로 들어가 있는 페이지네이션 코드.
const queryClient = useQueryClient()
const [page, setPage] = React.useState(0) // 페이지네이션 시작은 0

// 이후 페이지네이션의 쿼리
const { status, data, error, isFetching, isPreviousData } = useQuery({
  queryKey: ["projects", page], // 쿼리키
  queryFn: () => fetchProjects(page), // fetch  함수
  keepPreviousData: true, // 쿼리 키가 변경되어서 새로운 데이터를 요청하는 동안에도 마지막 data 값을 유지한다.
  staleTime: 5000, // 유지 시간
})

// Prefetch the next page!
React.useEffect(() => {
  if (!isPreviousData && data?.hasMore) {
    queryClient.prefetchQuery({
      queryKey: ["projects", page + 1],
      queryFn: () => fetchProjects(page + 1),
    })
  }
}, [data, isPreviousData, page, queryClient])
```

### 정리 해야 할 내용들

1. useQuery의 options에 대한 정리.
2. useMutation의 option 정리.
3. QueryClient에 대한 option 정리.

### 쿼리 옵션들

- cacheTime : unused 혹은 inactive 캐시 데이터가 메모리에서 유지 될 시간. 기본 시간은 5분이며, SSR에서는 Infinity로 설정하면 쿼리 데이터는 캐시에서 제거되지 않는다.
- staleTime : 신선도를 의미하며, 쿼리 데이터가 fresh에서 stale로 전환되는데 걸리는 시간. 기본 값은 0이다. Infinity로 설정 시 직접 캐시를 무효화 할 때까지 fresh 상태 유지. 캐시는 메모리에서 관리되므로 브라우저 새로고침 후에는 다시 가져온다.
- onSuccess : 데이터를 성공적으로 가져왔을 때 실행되는 함수.
- onError : 쿼리 함수에서 오류가 발생 했을 때 실행.
- onSettled : 쿼리 함수의 성공, 실패 두 경우에 모두 실행.
- keepPreviousData : 쿼리 키의 변수가 변경 되었을 때, 쿼리 데이터를 유지 할지 안할지 정하는 것.
- isPreviousData : 현재 데이터 값이 현재 쿼리 키의 값에 해당되는 값인지 확인 할 수 있다.
- refetchOnWindowFocus : 윈도우가 다시 포커싱 될 때 데이터 호출 여부. 기본 값은 true.

### Next.js에서의 React Query

- 참조해서 정리 예정

1. DOCS : https://tanstack.com/query/latest/docs/react/guides/ssr
2. 블로그 : https://velog.io/@arthur/React-Query-with-Next.js-%EC%84%9C%EB%B2%84-%EC%82%AC%EC%9D%B4%EB%93%9C-%EB%A0%8C%EB%8D%94%EB%A7%81
3. 블로그 : https://kir93.tistory.com/entry/NextJS%EC%97%90%EC%84%9C-react-query-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

- 주로 initialData를 통해 교통정리를 해서 시작하는 것 같다.

- SSG (Static Generation) 방식, SSR (Server-Side Rendering) 방식 두가지 형태의 pre-rendering 형태가 있다.
- React Query는 두가지 형태의 pre-rendering을 이용 할 수 있도록 지원한다.
- `/app` 폴더를 통해 Next.js를 intefrate 하는 경우, 아래 코드를 따라하세요 라고 나와있다.

1. Using initialData

- Neext.js는 `getStaticProps` 혹은 `getServerSideProps` 속성을 가지고 있다.
- useQuery의 initialData 옵션을 통해 내려줄 수 있다.
- ReactQuery의 입장에서는 같은 방식으로 통합이 가능하다. 아래는 getStaticProps를 통한 방식.

```js
// docs의 코드를 그대로 가져옴.
export async function getStaticProps() {
  const posts = await getPosts()
  return { props: { posts } }
}

function Posts(props) {
  const { data } = useQuery({
    queryKey: ["posts"],
    queryFn: getPosts,
    initialData: props.posts,
  })

  // ...
}
```

2. Using Hydration -- 이부분 docs 보면서 정리 중

- 리액트 쿼리는 동시에 여러 쿼리를 prefetching 할 수 있는 기능을 제공하고 있다. Next.js에서도 가능.
- 가져온 이후, 해당 쿼리들을 QueryClient에서 dehydrating한다.
- 서버의 사전 렌더링 작업 시 페이지 로드 혹은 JS가 동작 할 때 마크업 할 수 있으며, 리액트 쿼리가 다시 해당 쿼리들을 hydrate하여 전부 라이브러리로 사용 가능하다?
- 이는 서버가 페이지 로드 시 즉시 사용 할 수 있는 마크업을 pre-rendering 할 수 있고, JS를 사용 할 수 있는 즉시 React Query가 라이브러리의 전체 기능으로 해당 queryClient를 업그레이드 하거나 functionallity하게 할 수 있다.
- 해당 쿼리들이 렌더링 된 이후 staleTime이 지난 후에 클라에서 해당 쿼리를 다시 가져오는 작업이 포함된다.
- 아래는 hydration을 통한 SSR 구현이다.

```js
// _app.jsx
import {
  Hydrate,
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query"

export default function MyApp({ Component, pageProps }) {
  const [queryClient] = React.useState(() => new QueryClient())

  return (
    <QueryClientProvider client={queryClient}>
      <Hydrate state={pageProps.dehydratedState}>
        <Component {...pageProps} />
      </Hydrate>
    </QueryClientProvider>
  )
}
```
