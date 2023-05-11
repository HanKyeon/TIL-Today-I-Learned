# ReactHookForm 정리

학습 후기 : **유저 입력을 받는 것이 어려워진다면 어떻게 써야할까? 라는 해답이 담겨있다 생각함.**

`npm install react-hook-form`
`npm install @hookform/devtools`

- 학습 할 때 주로 참고한 글들

  1. 훅폼 독스 : https://react-hook-form.com/get-started

  2. 친절한 훅폼 사용법 설명 : https://velog.io/@leitmotif/Hook-Form%EC%9C%BC%EB%A1%9C-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC%ED%95%98%EA%B8%B0

  3. 훅폼의 강점 등 : https://tech.inflab.com/202207-rallit-form-refactoring/react-hook-form/

  4. 그냥 현재 내 궁금점을 해결 할 수 있을 것으로 보이는 질문

     - https://github.com/orgs/react-hook-form/discussions/9875
     - https://github.com/react-hook-form/react-hook-form/issues/4086

## WHY?

- input의 경우 변경이 잦아 재렌더링이 자주 일어나며, form 데이터를 모으기 난해 할 수 있다.
- 특히, 자율 프로젝트를 진행하며 user의 input이 복잡한 프로젝트를 진행하였기에, 편하게 하려면 필요하다 생각했다.
- 일반적으로 input의 리렌더링을 막기 위해 colocation과 ref를 사용한다. 하지만 훅폼은 간단히 된다.
- 리덕스, local state, context api, ref 네가지를 모두 조정했어야 하지만 formContext만 조정하면 다 되게 된다.

## WHAT?

-

## HOW?

Controller는 name, control, render로 구성.
name : 가리킬 form의 field 명.
control: useForm의 control
render : field에 의존하는 children Node

## WHAT IF?

## 겪으며 중점적으로 추가로 개선하고 정리해야 할 내용들

- 타입 스크립트로 지정해둔 타입을 내가 쿼리키 짠 것처럼, 트리 형태로 뻗어나간다.
- 폼의 가장 바깥에 있는 속성 이름을 name, description 등처럼 지정하여 연결하고, array 형태라면 useFieldArray를 통해 해당 필드 어레이에 이름과 컨트롤을 붙여서 사용해준다.
- 그렇게 어떤 useForm을 control 할 지 알려주면, 해당 이름을 자동으로 찾아들어간다.
- 이름 네이밍 규칙은 `속성이름.속성이름` 이런 형태로 간다.
- 만약 배열이라면 중간에 index 요소가 낀다.
- 컨트롤러를 현재 굉장히 복잡하게 구현하고 있는데, 해당 컨트롤러 하나에서 여러 값을 잡아낼 수 있지 않을까? 싶다.
- 컨트롤러 내부의 input에 이름을 붙여서 관리하는데, onChange 때문에 각각 Controller를 넣어줬었다. 해당 부분을 개선 할 수 있을 것이라 생각함.
- 독스를 좀 더 봐야겠다.

- 이 중에서, FieldArray가 append되고 붙을 때 초기화 되지않는 것은 watch를 사용하라는 말이 있다.
- 조건부 입력 활성화 역시 watch를 사용하라는 말이 있다.
- 나는 현재, value 하나를 onChagne 시에 state 하나에 담도록 해두었고, 해당 state의 변화로 조건부로 select option을 띄워주고 있다.
- 아무래도 watch로 하는 것이 조금 더 가독성이 좋고, 뛰어난 코드일 것으로 보이지만, 해당 input이 select 파트로 결정되는 input이기에, 변화가 그렇게 많지 않을 것이라 생각하였다.

- 근데 select option이 바뀌었을 때, 그냥 reset을 해주면 되겠지..?
