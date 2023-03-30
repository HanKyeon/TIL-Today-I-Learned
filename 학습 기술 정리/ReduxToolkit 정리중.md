# Redux Toolkit 정리

학습 후기 : **리덕스의 불편한 점이 해결된 라이브러리이다. 막스 아저씨 방식으로 action creator를 사용했는데, createThunk & createAsyncThunk 등을 사용하는 방법도 알면 좋았을 것 같다.**

## WHY?

## WHAT?

## HOW?

## WHAT IF?

## 에러 핸들링

1. Redux Toolkit의 initialState는 lazyLoading된다.
   참고 : https://redux-toolkit.js.org/api/createSlice#initialstate
   해결책 : https://stackoverflow.com/questions/72677169/argument-of-type-any-is-not-assignable-to-parameter-of-type-never-array-pa
   해결책 설명 : TS로는 타입을 지정해주면 된다. JS는 if로 에러 잡으면 될 듯.
