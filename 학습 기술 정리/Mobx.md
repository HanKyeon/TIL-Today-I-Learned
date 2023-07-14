# Mobx 정리

학습 후기 : **Redux 및 Recoil 등 관련 상태관리 뿐만 아니라 Mobx라는 것이 있다는 것을 알게 됨. 객체지향을 하는 상태관리 라이브러리라는 유니크한 포지션을 갖고 있다 생각함.**

독스 : https://ko.mobx.js.org/README.html
영어 독스 : https://mobx.js.org/README.html

yarn : `yarn add mobx`
npm : `npm install --save mobx`

- 이 때, TypeScript 또는 babel과 함께 사용할 때 클래스를 사용한다면, 클래스 필드에 TC-39 사양을 가진 transpilation을 사용하도록 구성을 업데이트 해야 한다. 그렇지 않으면 클래스 필드가 초기화되기 전에 observable을 만들 수 없다.
- TypeScript의 경우, `useDefineForClassFields`를 `true`로 설정한다.
- Babel의 경우, 7.12 버전 이상에서 사용이 가능하며, 아래와 같이 설정.

```js
{
    "plugins": [["@babel/plugin-proposal-class-properties", { "loose": false }]],
    // Babel >= 7.13.0 (https://babeljs.io/docs/en/assumptions)
    "assumptions": {
        "setPublicClassFields": false
    }
}
```

- 이 때, 검증을 위해 `index.js` 등에 `if (!new class { x }().hasOwnProperty('x')) throw new Error('Transpiler is not configured correctly');` 이러한 코드로 관리를 해줘야 한다.

- 참고 : https://techblog.woowahan.com/2599/

## WHY?

**- Docs 기준**

## WHAT?

## HOW?

- Mobx는 앱을 `상태state`, `동작action`, `파생derivation`의 세가지 개념으로 구분한다.
- 아래는 `상태state`를 `observable`하게 만드는 예제이다.
- **개인 생각** : `this` 키워드 때문에 React가 클래스형 컴포넌트에서 함수형 컴포넌트로의 개선을 하기 위해 hooks를 낸 것인데, this와 클래스로 관리를 하는 것이 신기하다. 비효율적이지 않을까? 오히려 리액트가 함수형이 되어서 헷갈리지 않게 되는 것일까

```js
import { makeObservable, observable, action } from 'mobx';

class Todo {
  id = Math.random();
  title = '';
  finished = false;

  constructor(title) {
    makeObservable(this, {
      title: observable,
      finished: observable,
      toggle: action,
    });
    this.title = title;
  }
  // 아래가 action이다.
  toggle() {
    this.finished = !this.finished;
  }
}
```

- 상태 변화에 따라 변화하는 `파생derivation`은 UI, 남은 todos의 수 등 파생 데이터, BE 데이터 등이 있다. 상태에 따라 값이 변하느.
- MobX는 `computed`와 `reaction`으로 `파생derivation`을 구분한다.
- `computed` : 현재의 `observable state`에서 순수 함수를 사용하여 파생될 수 있는 값
- `reaction` : state가 변경될 때 자동으로 발생해야 하는 side effect. 명령형 프로그래밍과 반응형 프로그래밍 사이를 연결해주는 다리 역할이다.
- MobX를 처음 다루면 reaction을 자주 사용하는 경향이 있다. 가장 좋은 방식은 state 기반으로 값을 생성하려는 경우, 항상 `computed`를 사용하는 것이 권장된다.

```js
// computed 예시.
import { makeObservable, observable, computed } from 'mobx';

class TodoList {
  todos = [];
  get unfinishedTodoCount() {
    return this.todos.filter((todo) => !todo.finished).length;
  }
  constructor(todos) {
    makeObservable(this, {
      todos: observable,
      unfinishedTodoCount: computed,
    });
    this.todos = todos;
  }
}
```

- `observer`를 통해 `reaction`으로 UI 렌더링을 변경하는 형태이다.
- **개인 생각** : 비효율적인 코드로 보이는데.... 굳이 functional Component에 oberver를 붙여야 하나.....?
- 동작 원리는 https://ko.mobx.js.org/react-integration.html 에서.
- `autorun`, `reaction`, `when` 등의 함수를 사용하여 상황에 맞게 커스텀 reaction을 만들 수 있다.

```js
// reaction 예시
import * as React from 'react';
import { render } from 'react-dom';
import { observer } from 'mobx-react-lite';

const TodoListView = observer(({ todoList }) => (
  <div>
    <ul>
      {todoList.todos.map((todo) => (
        <TodoView
          todo={todo}
          key={todo.id}
        />
      ))}
    </ul>
    Tasks left: {todoList.unfinishedTodoCount}
  </div>
));

const TodoView = observer(({ todo }) => (
  <li>
    <input
      type="checkbox"
      checked={todo.finished}
      onClick={() => todo.toggle()}
    />
    {todo.title}
  </li>
));

const store = new TodoList([
  new Todo('Get Coffee'),
  new Todo('Write simpler code'),
]);
render(<TodoListView todoList={store} />, document.getElementById('root'));

// state를 자동으로 관찰하는 함수입니다.
autorun(() => {
  console.log('Tasks left: ' + todos.unfinishedTodoCount);
});
```

## WHAT IF?

**- Docs 기준**

## 참고
