# Tailwind 정리

학습 후기 : **정말 최고의 모듈형 CSS 같음. 유틸리티 퍼스트 CSS라더니 진짜 유틸리티 면에서 좋다고 생각함.**

- 사용법

```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

이후, tailwind.config.js에서 적용 폴더 지정.

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // 아래 부분 포함해서 두 부분에 적용.
    "./node_modules/tw-elements/dist/js/**/*.js", //
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

이후, root style sheet에서 테일윈드 사용을 선언

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

- 혹은, 간단히 cdn으로 `<script src="//cdn.tailwindcss.com"></script>`를 추가해서 사용 가능하다.

## WHY?

- 정말 편하다. 일단, css와 컴포넌트를 왔다갔다하지 않아도 된다는 점과, bootstrap과 다르게 내가 원하는 형태의 class들을 정의 할 수 있다는 장점이 크다.
- 부트스트랩 같은 pre Built-in 컴포넌트 방식과 달리, Utility-first 개발 방식을 제공한다.
- 내가 필요한 부분을 조립하는 방식으로 사용자의 입맛에 맞게 커스터마이징이 가능하다.

## WHAT?

- 유틸리티 퍼스트 CSS Framework
- 사용자 입맛에 맞는 커스텀 디자인을 손쉽고 빠르게 구축 할 수 있음.
- 로우레벨 프레임워크. 즉, 사전에 제작된 컴포넌트를 제공하지 않는다.
- 창의성, 재사용성, 생산성이 높아지도록 하는 자율성.

## HOW?

- 내가 사용하는 방식을 정리해보도록 하겠음.

- 우선적으로 독스가 굉장히 잘 되어 있어서 선두에 적어두고 시작함.
  https://tailwindcss.com/docs/theme

1. screens

- 반응형 웹을 만들 때 사용한다.
- 예시로, 부트스랩에서 사용한 sm, md, lg, xl, 2xl 등 breakpoints 설정이 가능하다.
- 예시로 'sm': '640px', 'md': '768px' 등이 있다.

2. colors

- colors key allows you to customize the global color palette for my pjt. 컬러즈는 글로벌 빠레트 설정이 가능. backgroundColor, borderColor, textColor 등 색상과 관련지어질 수 있음.
- 또한, 컬러이름 이후 100, 200, 300 등 강도를 통해 세부 색상 설정이 가능하다. 남들 테일윈드 config 파일 참고.

3. spacing

- spacing key allows you to customize the global spacing and sizing scale for your pjt. 내 플젝의 글로벌 스페이싱을 바꿔줄 수 있다는 것 같음.
- 숫자: 숫자rem 설정, px: 1px 등 설정을 통해 padding, margin, width, height, maxHeight, flex-basis, gap, inset, space, translate, scrollMargin, scrollPadding, textIndent 등 코어 플러그인에도 적용이 된다고 한다.

4. Core plugins

- https://github.com/tailwindlabs/tailwindcss/blob/master/stubs/defaultConfig.stub.js
- 위 링크 참조 필수.
- 내가 이해한 대로라면 각 css 속성(borderRadius, keyeframes, animation 등) 별로 단축을 지정해줄 수 있다는 내용 같음.
- 예시로는

```js
module.exports = {
  theme: {
    borderRadius: {
      none: '0',
      sm: '.125rem',
      DEFAULT: '.25rem',
      lg: '.5rem',
      full: '9999px',
    },
  },
};
```

- 위의 예시가 제시되어 있는데, className을 rounded나 rounded-none rounded-sm 등을 통해 사용한다.

5. extend

- 기본 테마에 추가를 하고 싶을 경우 사용하는 값인 것 같음. 사실 css 쪽 태그에 달아줄 때도 사용 가능.
- 아니 그냥 theme에다가 적어도 오버라이딩 된다고 함.

6. font 사용

- font 사용의 경우, css에 tailwind 선언보다 먼저 font를 선언한 style sheet를 import 해주어야 한다. 이후 tailwind config에서 선언하면 `font-선언한이름` 으로 사용이 가능하다.

7. background image 사용

- 이미지의 경우, url을 통해 css처럼 연결시켜 줄 수 있다.
- extend에서 선언해줘야 하는 위치는 backgroundImage 객체.

8. 실제 사용 예시

- 현재 사용하고 있는 애니메이션들은 아주 길기에, 예시만 몇가지 들도록 함.

```js
/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    './src/**/**/*.{js,jsx,ts,tsx}',
    './src/**/**/**/*.{js,jsx,ts,tsx}',
    './src/**/**/**/**/*.{js,jsx,ts,tsx}',
    './src/**/**/**/**/**/*.{js,jsx,ts,tsx}',
    './node_modules/tw-elements/dist/js/**/*.js',
  ],
  // safelist: [
  //   {
  //     pattern:
  //       /bg-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pinkrose|primary|secondary|tertiaty)-(50|100|200|300|400|500|600|700|800|900)/,
  //     variants: ["hover", "active", "group-hover", "group-active"],
  //   },
  // ],
  theme: {
    extend: {
      screens: {
        mobile: '400px',
      },
      colors: {
        primary: {
          50: '#FFF5EB',
          100: '#FFE6CE',
          200: '#FFD2A7',
        },
      },
      fontFamily: {
        'hongcha-nemo': ['nemo', 'ui-sans-serif'],
      },
      backgroundImage: {
        'tale-nav-logo': "url('/src/assets/images/TaleNavLogo.png')",
      },
      animation: {
        'ppyong-super-fast': 'ppyong 0.11s both',
      },
      spacing: {
        vh: '1vh',
        vw: '1vw',
        pc: '1%',
      },
      keyframes: {
        ppyong: {
          '0%': { transform: 'scale(0%)' },
          '95%': { transform: 'scale(107%)' },
          '100%': { transform: 'scale(100%)' },
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
```

## WHAT IF?

- 작은 커스텀 CSS 파일 용량
- view 중심의 쉬운 디자인 변경 (JSX를 벗어나지 않아도 디자인 변경이 손쉽다.)
- 개발 경험 향상. 정말 깊게 느낀다.
- 모바일 퍼스트 디자인 가능. screens에 원하는 사이즈를 분리하여 반응형을 쉽게 사용 할 수 있다.

## 참고

https://heokknkn.tistory.com/7
https://github.com/tailwindlabs/tailwindcss/blob/master/stubs/defaultConfig.stub.js
https://velog.io/@rrrrrrrrrrrocky/tailwindcss-rem%EB%8C%80%EC%8B%A0-px-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
https://defineall.tistory.com/833

## 경험한 오류들

- tailwindcss에서는 리터럴을 사용하면 안된다. 리터럴이 아닌, 삼항 연산자를 통한 사용은 가능하다.
- 즉, 완성된 className을 사용해야만 한다. 왜냐면 리터럴 같은 경우, 렌더링 이후 적용되는 className인데, tailwindcss는 렌더링 되기 전에 사용되는 css class를 제외하고는 렌더링을 하지 않기 때문.
- 해당 부분을 리터럴로 유지하고 싶다면, extends 혹은 theme에 **safeList(위의 실 사용 코드에서 주석처리 되어 있음. 활성화 하니 컴파일 시간이 꽤나 더 오래 걸리는 것으로 보여 정말 필요한 경우만 작성하는 것이 좋아보임.)**를 작성하여 보관해주어야 한다.

```js
const a = 100
// 아래와 같이 사용하면 적용이 되지 않음.
className={`w-[${a}px]`}
// 아래와 같이 삼항 연산자로의 사용은 가능하다.
className={`${a===100? `w-[100px]` : `w-[200px]`}`}
```

- className들을 모아둔 것을 모듈화해서 사용하는 것이 좋아보인다.
- mask 등의 이펙트는 css와 조합해서 사용했다.
