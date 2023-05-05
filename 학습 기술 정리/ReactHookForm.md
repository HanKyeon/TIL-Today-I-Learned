# ReactHookForm 정리

학습 후기 : **유저 입력을 받는 것이 어려워진다면 어떻게 써야할까? 라는 해답이 담겨있다 생각함.**

`npm install react-hook-form`
`npm install @hookform/devtools`

## WHY?

- input의 경우 변경이 잦아 재렌더링이 자주 일어나며, form 데이터를 모으기 난해 할 수 있다.
- 특히, 자율 프로젝트를 진행하며 user의 input이 복잡한 프로젝트를 진행하였기에, 편하게 하려면 필요하다 생각했다.
- 일반적으로 input의 리렌더링을 막기 위해 colocation과 ref를 사용한다. 하지만 훅폼은 간단히 된다.
- 리덕스, local state, context api, ref 네가지를 모두 조정했어야 하지만 formContext만 조정하면 다 되게 된다.

- 참고 : https://tech.inflab.com/202207-rallit-form-refactoring/react-hook-form/

## WHAT?

-

## HOW?

Controller는 name, control, render로 구성.
name : 가리킬 form의 field 명.
control: useForm의 control
render : field에 의존하는 children Node

## WHAT IF?
