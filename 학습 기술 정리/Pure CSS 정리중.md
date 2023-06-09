# CSS 정리

학습 후기 : **가장 내가 마음대로 조작하기 편한 스타일 시트. 알면 알수록 넓은 범위더라. 꾸준히 학습한 내용들을 기록할 예정이다.**

## WHY?

## WHAT?

## HOW?

참고 : https://gahyun-web-diary.tistory.com/80

- perspective 속성

  - 해당 속성은 원근법을 먹이는 속성임. 숫자가 커질수록 멀리서 보는 느낌이 난다.
  - perspective-origin을 통해 기준을 잡아줘야 한다. center, top, left, right를 기준으로 원근법을 먹인다.

- backface-visibility 속성
  - rotate 등으로 돌렸을 때, 뒷면이 보일지 안보일지 결정하는 속성. visible or hidden 등

## WHAT IF?

## 겪은 Side Effect

- keyframes로 animation을 줄 때, forwards 혹은 both를 주게 되면 최종 도착지에서 고정된 상태가 되어서 transition이 먹지 않는다.
- 따라서, AnimationBox에 등장 Effect를 넣고 scale을 하든지, 등장 effect 자체를 transition으로 통일하던지 해야 한다.

## 유용해보이는 CSS 모음

- 이미지 마스킹

```css
.bg-img-gradient {
  -webkit-mask: radial-gradient(
    closest-side at center,
    #000 0%,
    #000 90%,
    transparent 100%
  );
  mask: radial-gradient(
    closest-side at center,
    #000 0%,
    #000 90%,
    transparent 100%
  );
}
```
