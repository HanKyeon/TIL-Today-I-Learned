# CSS in js 모듈 비교 및 정리

## Mui

- Mui의 경우 CSS in JS를 통해 만들어진 것으로 암
- monorepo 구조로 패키지가 많이 갈라져 있어서 보기가 어렵다... ;ㅣ
- 어쨌든 styledComponent와 자체적인 core를 통해 만들어진 ui lib으로 알고 있음.

## Headless UI

- 폴더 구조가 멀티레포에다가, 자신들의 코어를 배포?는 모르겠는데 아무튼 빌드된 코어 파일을 import 하도록 작성되어 있음.
- 즉, tailwindCSS애 dependency를 제거하고 tailwindCSS를 사용하는 것 같은 느낌인듯. 이 구조 신박하다. 근데 사실상 코어에 peerDependency로 tailwindCSS가 걸려 있어서 같은 것 같음.
- 그러니까 이 모듈을 추가하려면 tailwindCSS가 필요하고, tailwind prettier 같은 것을 통해 조금 완성을 해주어야 할 것 같음.

## Ant Design

- rc 머시기를 쓰는데 잘 모르겠음.
- 마찬가지로 css in js 형태를 사용하는 것으로 아는데, 마찬가지로 styledComponent를 통해서 사용이 가능할 것으로 보임.

## TailwindCSS

- class 형태를 사용하며, css in js라기엔 class Name을 주로 이용한다. className이 길어지면 읽는 것이 어려워질 수 있다는 단점도 있을 것으로 보이는데, css in js처럼 컴포넌트가 그득그득 들어차는 것보다는 선호한다.

## 내가 생각하는 각각의 장단점 요약

- Mui & AntD: Docs가 잘 되어있고, 대부분의 상황에 대응이 가능하다. 커스텀이 어려운 부분들이 존재한다. 특히 Props를 넣어서 실행하는 경우 난해하다.
- Headless UI & TailwindCSS : 주로 className을 통해 구성하는 TailwindCSS이기에, id 등을 통해 css를 덮기 쉬울 것으로 보인다. 헤드리스는 실제 사용해보지 않아서 모름. 또한 실제 렌더링 되는 css 클래스 이름들만 파일로 만드는 tailwindCSS 특성상, 가벼울 것으로 예측한다. 세부적으로 커스텀을 하고 싶은 경우, 백틱화 ${}를 통한 변수가 불가능하여 조금 딱딱하게 하거나 수많은 css 이름들을 렌더링 시켜야 한다. 근데 사실 그 부분은 그때그때 변수로 높이나 너비를 잡으면 Mui 같은 경우도 className을 다시 만들면서 렉이 굉장히 심해질 가능성이 높다. 랜덤 제너레이트를 수행하는 클래스 이름을 생성했다 지웠다 해야하기에. 이런 경우 inline으로 처리하긴 할ㄷ스.
