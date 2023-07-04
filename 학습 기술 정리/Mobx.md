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

## WHAT IF?

**- Docs 기준**

## 참고
