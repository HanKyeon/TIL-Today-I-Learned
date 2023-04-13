# Redux Toolkit 정리

학습 후기 : **리덕스의 불편한 점이 해결된 라이브러리이다. 막스 아저씨 방식으로 action creator를 사용했는데, createThunk & createAsyncThunk 등을 사용하는 방법도 알면 좋았을 것 같다.**

## WHY?

## WHAT?

## HOW?

## WHAT IF?

## 에러 핸들링 및 경험

1. Redux Toolkit의 initialState는 lazyLoading된다.
   참고 : https://redux-toolkit.js.org/api/createSlice#initialstate
   해결책 : https://stackoverflow.com/questions/72677169/argument-of-type-any-is-not-assignable-to-parameter-of-type-never-array-pa
   해결책 설명 : TS로는 타입을 지정해주면 된다. JS는 if로 에러 잡으면 될 듯.

2. ReduxToolkit 역시 서버 상태, 즉 비동기 상태를 전문적으로 처리하는 라이브러리가 아니다.
3. TypeScript에서 일일이 타입 선언이 귀찮다면 아래처럼 선언해주면 된다.

```js
// Store의 index에서 선언해주는 타입. store는 configureStore로 묶어준 Store.
export type AppDispatch = typeof store.dispatch
export type RootState = ReturnType<typeof store.getState>

export const useStoreSelector: TypedUseSelectorHook<RootState> = useSelector
export const useStoreDispatch = function () {
  return useDispatch<AppDispatch>()
}

// 아래는 dispatch와 selector 둘 다 해당하는 내용이다.
// 커스텀 훅 사용 시 타입 선언 필요 없음.
const example = useStoreSelector((state) => state.example)
// 일반 useSelector 사용 시 RootState 타입 선언 필요.
const example2 = useSelector((state: RootState) => state.example)
```

- Action Creator의 경우, index에 모아서 관리하는 것이 좋다고 생각함.
  Action Creator 예시

```js
const FeatureExampleAction = function () {
  return function (dispatch: AppDispatch) {
    dispatch(ex1Actions.resetState({}));
    dispatch(ex2Actions.resetState({}));
    dispatch(ex3Actions.resetState({}));
  };
};
```

이런식으로 **기능** 별로 실행해줄 Action들을 한 곳에 모아서 관리를 하면 해당 기능 디스패치를 사용 하였을 때, index에서 관리하면 되기에 관리가 편해진다.
