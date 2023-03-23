## React Query 정리

- 학습 후기
  **리액트 쿼리 진짜 좋은 듯!!! 이전 프로젝트에서 servserState의 상태 관리를 redux로 했을 때, 꼬이는 경험을 했는데 React Query를 사용하게 되면 그럴 일이 없어질 것이다.**
- 학습 진행 버전 : 3.39.3

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

- useQuery의 경우, get 처럼 server state에 변화가 없을 때 사용.
- useMutation의 경우, post put delete 등 server state에 변화가 있을 때 사용.
- useQuery와 useMutation을 Hook으로 모아서 API마다 관리를 하는 것으로 보인다.
- API 정리가 깔끔할수록 작동하기 좋아보인다.
- 아래는 내가 사용하는 형태이다. React Hook의 형태로 queries를 관리한다.

```js
const useGetUserData = function (/* 필요한 정적인 파라미터 */) {
  return useQuery(
    /* unique key 값. 이 값으로 QueryClientProvider에서 server state를 관리하는 것으로 보인다. */
    `user`, // 특정 값(id 등)으로 캐싱을 원할 때는 배열 형태로 사용. [`user`, 15] 이런 식으로.
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
        queryClient.invalidateQueries(`user`) // user를 unique key로 가진 쿼리에 변경이 생겨 invalid 시켜줌.
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
const { isLoading, error, data } = useQuery(`user`, function () {
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

---

### 참고 자료

https://react-query-v3.tanstack.com/overview => ReactQuery Docs
https://tech.kakaopay.com/post/react-query-1/ => 카카오 테크 블로그 글
https://tech.kakaopay.com/post/react-query-2/ => 카카오 테크 블로그 글 2
https://tech.kakao.com/2022/06/13/react-query/ => Concurrent UI Pattern에 React Query를 사용했다고 해서 참고 예정

### 나는 어떻게 써야 할까?

1. get 요청 같은 경우, hook으로써 불러오기.
2. post, put, delete 등 mutation도 훅으로 쓰고 싶긴 한데 한 번 값을 조정해서 사용해보기.
