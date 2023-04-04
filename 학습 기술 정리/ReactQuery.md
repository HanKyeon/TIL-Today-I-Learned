## React Query 정리

- 학습 후기
  **리액트 쿼리 진짜 좋은 듯!!! 이전 프로젝트에서 servserState의 상태 관리를 redux로 했을 때, 꼬이는 경험을 했는데 React Query를 사용하게 되면 그럴 일이 없어질 것이다.**
- 학습 진행 버전 : 3.39.3 => 4.28.0

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
