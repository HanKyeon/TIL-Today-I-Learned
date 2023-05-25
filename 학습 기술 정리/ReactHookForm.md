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

#### 1. 정량적인 이유

- HTMLInputElement의 값이 변경 될 때마다 일어나는 리렌더링 이슈를 해결한다.
- 유연한 input을 받을 수 있다.
- form의 value에 언제든 접근이 가능함.
- name으로 구조화하기에 직관적이다.
- 즉, 코드가 단순해지고 유틸리티 api들이 많다.
- class validation 등이 쉬워지며, input 사용법에 대해 규격화가 가능해진다.

#### 2. 정성적인 이유

- input의 경우 변경이 잦아 재렌더링이 자주 일어나며, form 데이터를 모으기 난해 할 수 있다.
- 특히, 자율 프로젝트를 진행하며 user의 input이 복잡한 프로젝트를 진행하였기에, 편하게 하려면 필요하다 생각했다.
- 일반적으로 input의 리렌더링을 막기 위해 colocation과 ref를 사용한다. 하지만 훅폼은 간단히 된다.
- 리덕스, local state, context api, ref 네가지를 모두 조정했어야 하지만 formContext만 조정하면 다 되게 된다.
- 그냥 input Element를 다루기가 난해했는데, RHF으로 관리되는 input과 단편적인 ref로 관리되는 input을 분리해서 컴포넌트화 하면 좋을 것이라 생각했음.

## WHAT?

- DOCS에서는 이렇게 말한다. Performant, flexible and extensible forms with easy-to-use validation.
- input의 rerendering issue를 해결하고, form의 형태를 구조화하여 쉽게 사용 할 수 있으며, 유효성 검사 역시 쉽게 할 수 있도록 제공하는 라이브러리.

## HOW?

### APIs

- **실제 사용 경험**
  1. `FormProvider` Component로 감싼다. 그 내부 최상단에 form을 달아준다.
  2. 컴포넌트에 input을 달아두는데, formName도 함께 받는다.
  3. 컴포넌트에서 `useFormContext` 훅을 통해 control을 불러온다.
  4. `useController` 훅 혹은 `Controller` 컴포넌트를 통해 form의 값들을 input에 연결해준다.
  5. 만약 reactQuery의 서버 상태가 갱신 된 뒤에 변경 할 것이라면, `reset` 함수를 받아서 `reset(data)` 형태로 useEffect로 queryData를 째려보고 있으면 된다.
  6. 이후 form의 onSubmit에 `handleSubmit`을 달아주는데, `submitHandler` 함수를 선언해서 콜백을 넣어서 실행시켜준다. `submitHandler`에서는 뭐 수동 유효성 검사나 비동기 통신 등을 진행하면 된다.
  7. 적절한 formName을 통해 form을 구성하고 사용한다.

#### 1. useForm

- 가장 근본이 되는 api이다.

```js
const asfadsg = useForm<T>() // 타입 지정이 필요한 경우 이 형태로 지정.
const methods = useForm({ defaultValues: { ...userData } });
const {
  control, // 어떤 form으로 control되고 있는지 선언하기 위해 필요한 control. 다른 컴포넌트에 있는 input이 어떤 폼에서 control하는지 알려주고 결정하는 용도.
  register, // 일반적으로 Controller 혹은 useController를 대신해 input에 직접 register(이름) 이런 식으로 사용 할 때 필요.
  clearErrors,
  formState, // form에 대한 상태를 갖고 있음. isDirty : 사용자가 이미 건드려서 순수하지 않은 경우. dirtyField : 사용자가 수정한 필드가 있는 개체. defaultValues와 비교 할 수 있도록 useForm의 모든 입력의 defaultValues가 필요함.
  getFieldState, // 평가 시점에 가져온다.
  getValues, // 사용시 개발자가 원하는 시점에 특정 값을 뽑아 쓸 때 사용.
  handleSubmit, // 콜백함수를 인자로 받아 form의 onsubmit에 넣어주면 콜백함수의 첫번째 인자에 form의 정보를 넣어준다.
  reset, // 특정 값으로 reset하는 용도로 사용.
  resetField, // 특정 필드에 대한 정보를 확인하거나 defaultValue를 설정한다.
  setError, // validation에서 에러가 뜰 경우 error 메시지를 띄워주는 것 같음.
  setFocus, // 이거 focus 올려주는거인데 명령어로 가능하다.
  setValue, // register된 field 값을 동적으로 설정하고 formState를 확인하고 업데이트한다. 불필요한 렌더링을 최소화함.
  trigger, // 입력의 유효성 검사를 수동으로 트리거한다. 유효성 검사가 의존성이 있는 경우 유용하다고 함. ex 2차비번
  unregister, // 단일 input에 대해 입력을 unregister 할 수 있다. 두번째 인자로 상태를 유지할지말지 정할 수 있다.
  watch, // 사용 시 form 전체 재 렌더링. 따라서 useWatch 등 사용.
} = methods;
```

- 이 useForm으로 폼 하나를 정할 수 있음.
- 후에 언급할 FormProvider를 통해 useForm의 methods를 내려줄 수 있고, 해당 form의 control, register 등을 확인 할 수 있음.

```jsx
// 단일 input에 대해 register하기
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { register } = methods;
  return (
    <div>
      <input {...register(`formName.value`)} />
      <input {...register(`formName.nextFormName[${index}]`)} />
    </div>
  );
};
```

- 위 형식으로 단일 input 하나에 form value를 매핑이 가능함.
- 다른 controller와 마찬가지로 `.` 혹은 `[]`를 통해 객체 혹은 배열인덱스에 값을 넣을 수 있다.
- 하지만, 조금 더 세부적인 컨트롤이 난해하며, register를 내려주거나 받아주어야 하기에 hook처럼 선언적으로 쓰기가 어렵다.

#### 2. useController

- 위의 `useForm` 훅에서 반환되는 control을 지정해주고, 특정 input이 해당 control로 관리되고 있다고 명시해주는 훅이다.
- `Controller` 라는 컴포넌트 혹은 `useController` 훅을 통해 form에서 field이름, attribute 이름으로 register 할 수 있다.

```jsx
// Controller Component 사용
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { control } = methods;
  return (
    <div>
      <Controller
        control={control}
        name={`formName.value`}
        rules // 생략
        render={({ field, fieldState }) => (
          <input
            name={`formName`}
            onChange={field.onChange}
            {...field}
          />
        )} // field를 스프레드 해줘도 되고, value ref onChange 등을 직접 연결해줘도 된다.
      />
      <Controller
        control={control}
        name={`formName.nextFormName[${index}]`}
        rules // 생략
        render={({ field, fieldState }) => (
          <input
            name={`formName.nextFormName[${index}]`}
            onChange={field.onChange}
            {...field}
          />
        )} // field를 스프레드 해줘도 되고, value ref onChange 등을 직접 연결해줘도 된다.
      />
    </div>
  );
};
```

- 위 예시는 useForm에서 사용한 register와 동일하다.
- 하지만, formName 이후의 값을 등록 할 때, control과 이름을 변수형태로 매핑해서 각각 하나를 Component화가 가능하다는 장점이 있다.
- 그 뿐만 아니라, AntD, React-Select, MUI 등 외부 라이브러리 등을 사용 할 때 쓰면 편리하다고 한다.

```jsx
// 단일 input에 대해 register하기
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { control } = methods;
  const { field, fieldState } = useController({
    control: control,
    name: `formName.value`,
  });
  const { field: depthField, fieldState: depthFieldState } = useController({
    control: control,
    name: `formName.nextFormName[${index}]`,
  });
  return (
    <div>
      <input {...field} />
      <input
        onChange={depthField.onChange} // 이 onChange의 경우, onChange={(e) => {depthField.onChange(e)}} 이런식으로 e벤트를 바로 넣어주는 callback 함수를 넣어서 추가 작업 실행이 가능하다.
        value={depthField.value}
        ref={depthField.ref}
        onBlur={depthField}
      /> // 더 있는걸로 아는데 이런 식으로 흩뿌려서 선택적으로 넣어도 됨.
    </div>
  );
};
```

- Controller 컴포넌트보다 더 cli적으로 사용하기 좋은, 함수 로직에서도 사용이 가능한 field를 뱉어주는 `useController` 훅이다.
- Controller 컴포넌트보다 코드가 적고 간결하며 상단에 모아주면 어떤 form을 이 컴포넌트에서 관리하는지를 알 수 있다.

#### 3. useFormContext

**1. useFormContext**

- `uesFormContext` 훅은 어디서든 `FormProvider`가 제공하는 from context에 접근이 가능하다.
- `useFormContext`의 경우, 호출 위치 즉 평가 시점의 상단의 `FormProvider`에 접근해서 반환한다.
- `useFormContext` 훅은 props drilling이 발생하여 `FormProvider`의 control 형태에 접근하기 어려운 경우에 사용한다.

**2. FormProvider**

- 개인) 독스 기준으로는 `useFormContext` API의 하위 메뉴에 있는데, 이게 상단이지 않나 싶음.

```js
// FormProvider 사용법
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { handleSubmit } = methods;
  const submitHandler = function (data) {
    console.log(data);
  };
  return (
    <FormProvider {...methods}>
      <form onSubmit={handleSubmit(submitHandler)}>{children}</form>
    </FormProvider>
  );
};
```

- 이런 형태로 제공하며, 위의 예시에서 children에 들어가 있는 모든 컴포넌트에서 `useFormContext`를 통해 `FormProvider`의 context에 접근이 가능하다.

#### 4. useWatch

- 개인) 사실 사용해본 적 없음. 정리하고 사용해볼 예정.
- `watch` API와 흡사하지만, `useWatch`는 커스텀 훅 레벨에서는 아주 높은 성능을 자랑한다고 함.
- input의 값을 가져오는데 리렌더링이 일어나지 않는 별개의 상태다! 라는 것 같음.

```jsx
// docs 기반 사용법
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { control } = methods;
  const formNameValue = useWatch({ control: control, name: `formName.value` });
  const { field } = useController({ control, name: `formName.value` });
  return (
    <FormProvider>
      <input {...field} />
      <div>formName의 value 속성 값 : {formNameValue}</div>
    </FormProvider>
  );
};
```

#### 5. useFormState

**1. useFormState**

- 개인) 마찬가지로 사용해본 적은 없음. 하지만 isDirty 등 input의 유효성 같은 곳에서 유용할 것으로 생각했음.
- `useFormState` 훅은 각 폼의 상태를 확인하고, 커스텀 훅 레벨에서 재렌더링을 최적화할 수 있다.
- 이 훅은 바라보고 있는 `formName`의 `formState`에 대해 확인한다.
- 그렇기에 다른 `useFormState` 혹은 `useForm`에는 영향을 주지 않으며, 이 훅을 통해 복잡한 form의 state더라도 재렌더링이 되는 sideEffect를 줄일 수 있다.
- `useFormState`의 `isDirty`가 `true`인지 `false` 인지는 초기 `defaultValues`와 같은지 아닌지로 확인한다.

```jsx
// docs 기반 사용법
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { control } = methods;
  const { field } = useController({ control, name: `formName.value` });
  const { dirtyFields } = useFormState({ control: control });
  return (
    <FormProvider>
      <input {...field} />
      {dirtyFields?.formName?.value && <div>님 값 바꿨음</div>}이 때, dirtyFields는
      빈 객체로 출발한다. 그래서 옵셔널 체이닝을 해주는 것이 좋을 것임.
    </FormProvider>
  );
};
```

**2. ErrorMessage**

- 입력 관련 오류 메시지를 렌더링하는 엘리먼트이다.
- `npm install @hookform/error-message`를 통해 설치.
- 사실 그냥 빨간 줄 컴포넌트임. 앞에 경고 달려있고 특정 값의 errors를 캐치하는.

```jsx
import { ErrorMessage } from '@hookform/error-message';

const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const {
    control,
    formState: { errors },
  } = methods;
  const { field } = useController({
    control,
    name: `formName.value`,
    rules: { required: `에러임?` },
  }); // required에 메시지를 넣으면 해당 메시지가 ErrorMessage 컴포넌트에 들어가게 된다. boolean이면 암것도 안뜬다.
  return (
    <FormProvider>
      <input {...field} />
      <ErrorMessage
        errors={errors}
        name={`formName.value`}
      />
      <ErrorMessage
        errors={errors}
        name="formName.value"
        render={({ message }) => <p>{message}</p>}
      />
    </FormProvider>
  );
};
```

#### 6. useFieldArray

- 개인) 사실 이 기능만 보더라도 react hook form을 사용하는데 충분하다고 생각함. 옵셔널로 편하게 원하는 리스트 입력이 가능하다!
- 동적으로 Array 형태의 입력을 쉽게 만들어주는 훅.
- ux와 성능적인 면에서 최적화를 하기 위해 만들어졌다.
- https://www.youtube.com/watch?v=Q7lrHuUfgIs 해당 유투브를 보면 쉽고 빠르게 성능을 향상 시킬 수 있을 것이다.

```jsx
// 단일 input에 대해 register하기
const ExComponent = function () {
  const methods = useForm({
    defaultValues: { formaName: { value: ``, nextFormName: [] } },
  });
  const { control, register } = methods;
  const { field, fieldState } = useController({
    control: control,
    name: `formName.value`,
  });
  const {
    fields, // 배열의 필드들.
    append, // 뒤에 추가로 값을 붙여넣어준다. 객체를 받아서 붙여주며, focusOptions도 줄 수 있음. 중요! append data가 필수임.
    prepend, // 앞에 붙인다
    remove, // index로 지우기
    swap, // index로 바꾸기
    move, // 옮기기
    insert, // 중간에 넣기
  } = useFieldArray({ control, name: `formName.nextFormName` });
  return (
    <div>
      {fields.map((field, index) => {
        return (
          <input
            key={field.id}
            name={`formName.nextFormName[${index}]`}
          />
        );
      })}
      {fields.map((field, index) => {
        return (
          <input
            key={field.id}
            {...register(`formName.nextFormName[${index}]`)}
          />
        );
      })}
    </div>
  );
};
```

- 위와 같이 `register`로 해도 되고 name value onChange에 직접 매칭해도 됨. `register`가 더 좋은 것 같음.
- formName을 정할 때, `attr[${index}]` 형태가 아닌, `attr.${index}` 형태로 작성해도 됨. JS는 배열도 객체이므로.

**간단한 내용**
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
- 만약 배열이라면 중간에 index 요소가 낀다. `속성이름.배열이름[인덱스].속성이름` 이런 형태. JS의 배열은 객체이기에 `속성이름.배열이름.인덱스.속성이름` 역시 가능하다.
- 컨트롤러를 현재 굉장히 복잡하게 구현하고 있는데, 해당 컨트롤러 하나에서 여러 값을 잡아낼 수 있지 않을까? 싶다.
- 컨트롤러 내부의 input에 이름을 붙여서 관리하는데, onChange 때문에 각각 Controller를 넣어줬었다. 해당 부분을 개선 할 수 있을 것이라 생각함.
- 독스를 좀 더 봐야겠다.
- Controller 컴포넌트 외에도, useController 라는 훅이 있다. 해당 훅을 사용하면 Controller를 줄여 피라미드를 줄일 수 있을 것이다.

- 수정을 하는 hookform에 대해 request와 response 자료형이 다르다면, SSR을 이용한 BFF를 통해 맞춰주는 형태도 좋을 것 같다.
- 혹은 ReactQuery를 두개 짜던가 하는 형태면 좋을 것 같다. 일반 data와 수정용 hookFormData를 두개 만들어서 뿌려서 사용하면 좋을 것 같음.

- 이 중에서, FieldArray가 append되고 붙을 때 초기화 되지않는 것은 watch를 사용하라는 말이 있다.
- 조건부 입력 활성화 역시 watch를 사용하라는 말이 있다.
- 나는 현재, value 하나를 onChagne 시에 state 하나에 담도록 해두었고, 해당 state의 변화로 조건부로 select option을 띄워주고 있다.
- 아무래도 watch로 하는 것이 조금 더 가독성이 좋고, 뛰어난 코드일 것으로 보이지만, 해당 input이 select 파트로 결정되는 input이기에, 변화가 그렇게 많지 않을 것이라 생각하였다.

- 근데 select option이 바뀌었을 때, 그냥 reset을 해주면 되겠지..?

- React Query 데이터로 defaultValues를 넣을 때는, 쿼리 데이터를 바라보는 useEffect를 만들어서 `reset(data)` 형태로 만들어주면 된다.
- 데이터가 변경 될 때, data로 reset 해준다는 의미.
- reset의 option에 대한 내용들 역시 정리해보자.

- controller의 rules 속성을 통해 rule을 지정 할 수 있고, validate를 통해 매번 validate가 가능하다. 그래서 fieldState에 따라서 관리를 하면 될 것 같은데, submit 될 때만 확인해서 토스트를 띄워주고 싶은 입장에서 해당 부분은 상당히 불편하다.
- 해결책으로는 해당 field의 value가 변할 때 state 하나가 그 값을 참조하게 onChange를 적용하고, 해당 값을 validate 하는 것이 있을 것이다.
- 혹은, 그냥 validate를 다 제거하고, 데이터가 모이는 부분에서 모아서 validate 하면 될 것이다.

- `useController` 이거 진짜 물건이다! controller를 줄일 수 있음. Form의 형태가 일정하다면 field를 `useController`로 받아서 `field.value` 이후 변수를 호출해 변수에 따른 평가를 실행 할 수 있다.
- 쓰면 쓸수록 훅폼 굉장히 좋은 것 같다.

- 현재 `formName`으로 form에서의 이름을 받아서 `fieldArray`로 연결하는 컴포넌트, 즉시 값을 입력하는 컴포넌트 등을 만들었는데, `formName`을 받고, `field.value`를 통해 뭔가 더 하기 위해 `field.value`에 이어줄 속성명을 받아서 호출해서 사용하는 컴포넌트도 될 것 같긴 한데..

## 간단히 정리해본 내용

1. why?

- input 의 경우, 리렌더링이 자주 일어나며 formData가 흐트러져 있다면 데이터를 한 눈에 알아보기 힘들다.
- 리렌더링을 막고, form의 value에 언제 어디서든 접근이 쉽고 간편하다.

2. What?

- 유연하고, 성능이 좋으며, 확장 가능한 쉬운 validation이 가능한 폼. 독스에서는 이렇게 말한다.
- form의 형태를 구조화하여 쉽게 사용 할 수 있으며, 유효성 검사 역시 쉽게 할 수 있도록 제공하는 라이브러리.

3. how?

- FormContext 라는 컴포넌트가 있다. 일종의 context api 개념으로 보면 좋은데, 감싼 부분에서 formContext에 접근하여 input 을 바로 사용할 수 있다.
- FormContext에 useForm에서 나오는 control로 이 FormContext에서의 control 형태를 알려준다.
- 그렇게 되면 useFormContext 훅으로 바로 상위의 formContext에 접근이 가능하다.
- input 에 매칭하는 것은 name으로 매칭하게 된다.
- 객체 형태라면 name이 해당 속성 명으로 연결이 되며, 배열 형태라면 숫자로 연계가 된다.
- name의 형태는 `속성.속성[index]` 이런 형태로 된다.
- 일반적으로 field.value를 통해 접근이 가능하다.
- input에 매칭하는 것은 Controller를 통해 가능하다. input에 네임만 붙인다고 끝나는 것이 아닌, input에 field.value와 field.onChange 등 속성을 연결시켜야 한다.
- Controller를 컴포넌트 형태가 아닌 선언형으로 쓰고 싶다면 useController를 사용하면 된다. name과 control을 명시하고, defaultValues 등이 명시가 가능하며, 반환은 field와 fieldState를 반환한다.
- 실질적인 값은 field이며, field에 대한 평가가 들어있는 것이 fieldState이다. isDirty 등 다양한 값이 있으나, 해당 값을 제대로 사용해보지는 못했다. 그래서 추후 정리를 해야함.
- 이후 onSubmit에 handleSubmit 함수를 연결시켜주고, handleSubmit의 인자로는 콜백함수를 받는다. 콜백함수는 form의 데이터가 최종적으로 정제된 값이다.
- useForm은 선언 할 때 useForm<T>()을 통해 타입 선언이 가능하다.

4. what if?

- 우선, 가장 간단히 폼을 쉽게 쓸 수 있다.
- 리렌더링 이슈를 최소화 할 수 있다.
- 개인적으로는, useFieldArray를 통해 배열 형태의 입력 역시 쉽게 가능하다.
- form을 구조화하여 응답 데이터만 잘 가공해서 defaultValues에 집어 넣는 로직만 짜면 자동으로 form 사용이 편해진다.
- 또한, handleSubmit의 콜백 함수에서 form 데이터 역시 가공이 가능하기 때문에 data를 최상위에 모으는 것도 쉽다.
