## 공통

1. 쉘에서 각 팝업이 쏘는 postMessage에 따른 행동을 명확하게 구분해야 함

### 1. postMessage

- 특징: window.open()을 실행 할 경우, 열어준 창의 WindowProxy 객체를 반환함.
- 부모 => 자식: 반환된 WindowProxy 객체를 저장하여 해당 WindowProxy 객체에 postMessage를 쏴서 자식에게 컨텍스트 전달 가능.
- 자식 => 부모: 자식 shell의 window.opener가 부모 shell임. 자식 shell의 iframe이라면 window.parent.opener를 통해 컨텍스트 전달 가능.

#### 장점

1. 원하는 popup에 postMessage를 발송이 가능.

#### 단점

1. popup을 관리해줘야 함.

- 닫혔을 때를 대비해 open하기 전에 beforeUnload 이벤트를 달아둔 뒤에 open하여 popup 관리를 해도 될 듯

2. shell 혹은 core가 필연적으로 무거워질 수 밖에 없음. 팝업 관리를 하는 모듈을 따로 빼는 것도 좋지 않을까 생각.

---

### 2. BroadCast Channel

- 특징 : BroadcastChannel 클래스를 통해 공통된 postMessage를 받을 수 있음. postMessage를 쏜 곳에는 이벤트 발생하지 않음.
- 부모 => 자식 : 부모가 BroadCastChannel에 postMessage를 쏘면 됨.

#### 장점

1. 리소스 관리가 필요 없으며, 연결만 될 경우 손쉽게 브로드캐스트를 통한 양방향 통신이 가능.
2. 팝업이 하나이거나, 팝업 종류를 명확하게 정의하고 정리하여 사용 할 경우 사용하기 간단하고 강력할 것으로 보임.

#### 단점

1. 원하는 자식을 잡아서 통신하는 것이 불가능함. 채널 전체에 쏘는 것이기 때문에.
2. 보일러 플레이트가 아주 간단함.
3. 정책 상 동일 오리진만 BroadCastChannel을 통한 통신이 가능함.

---

### 3. Message Channel

- 특징 : MessageChannel 클래스를 통해 1대 1로만 브로드캐스트 채널을 여는 느낌.
- BroadcastChannel과 마찬가지로 쏘고 받으면 됨

---

# 정리 방법

1. 흐름은 why what how whatif로.
2. why : MFA가 늘어나면서 iframe의 사용이 늘어났고, 개인적으로는 popup의 사용이라던가 같은 사이트 다른 탭의 소통 면에서 처리해두면 좋을 내용이라 정리.
3. what : iframe 간의 통신, 혹은 탭 간의 통신을 위한 방법들을 정리할 것이다.
4. how

- 공통적으로는 `postMessage`를 사용함.
- 근데 그 `postMessage`의 사용 방식이 다름.
- 첫째로는 쌩으로 `window.postMessage`를 날리는 것 : 세부적인 조정에서 좋을 것으로 보임. 단, 부모쪽이나 자식쪽에서 message에 대해 어떻게 처리할 것인지를 명확하게 문서화해야 하며 보일러플레이트가 길어질 것으로 보임. 보안 면에서 와일드카드"\*"를 통해 사용이 가능한 만큼 로컬 환경에서 테스트하기 좋아보임. 오리진 제한도 가능할 것으로 보임.
- 둘째로는 `BroadcastChannel`을 통해 연결된 곳들에 전체로 날리는 것 : 부모자식의 통신이 1대1이라면 편하고 강력할 것으로 보임. 만일 여러개일 때 수행해야 할 작업에 있어서도 유리할 것으로 보임. 특히 `iframe`을 사용할 경우 `document`와 `iframe`이 함께 채널에 연결되어 2회 fetch가 되는 경우가 생길 것으로 보임. 보안면에서 같은 오리진이어야 하므로 유리한듯. 소수이거나, 아주 많거나 한 경우에 유리하다고 생각함.
- 셋째로는 서비스 워커를 통해 날리는 것 : 아직 잘 모르겠음.
- 포스트 메세지를 쓰지 않는 야매 방식은 `storage` 이벤트에서 로컬 스토리지를 변경하거나 하는 것 : 야매이지만 다크/라이트모드 같은 다른 창이어도 로컬연동이 좋은 것을 설정함에 있어서 정말 좋을 것으로 보임.
- 그리고 프론트 단이 아닌 서버단과 함께 `websocket`을 사용할 수 있음. 해당 부분은 리소스가 많이 필요하기 때문에 (웹 서버가 필요하며, client가 socket을 맺고 있어야 함) 언급만 이렇게 하고 넘어가겠음.
- 팝업 내 아이프레임이 opener에게 쏘는 방법 : `window.parent.opener.postMessage`가 가능함. 애초에 `window.parent`는 부모가 없으면(frame 기준) 자기 자신을 보기에 통일시켜도 됨.
- 부모가 팝업을 관리하는 방법 : `window.open()`을 실행하면 `WindowProxy` 객체가 반환됨. 해당 객체를 관리하고 해당 객체를 잡아서 postMessage를 쏴줄 수 있음. 이 부분은 `beforeunload` 이벤트에서 부모가 관리하는 popup 형태에서 자신을 빼는 함수를 실행시켜주면 좋을 것임.
- window가 popup을 열 때 함수를 message로 넘길 수 있는가? 는 좀 알아봐야 할 것 같으나, 넘기지는 못할 것으로 보임. cjs 파일을 안받아 올 수 있으므로.
- `window.open()`을 실행하여 얻은 `WindowProxy` 객체에서 `popup.document.querySelector` 등을 이용할 수 있다.

4. what if : iframe간의 통신이 원활해지고 전략을 짜는데 유용해짐. 특히 BroadcastChannel과 일반 postMessage를 사용하는 것이 좋다고 봄.

5. 좀 더 참고해서 봐야 할 블로그

- [인파데브 - window.open()에 대한 글](https://inpa.tistory.com/entry/JS-%F0%9F%93%9A-windowopen-%EC%A0%95%EB%A6%AC)
- [인파데브 - 부모 자식 프레임 간의 통신](https://inpa.tistory.com/entry/JS-%F0%9F%93%9A-%EB%B6%80%EB%AA%A8%EC%B0%BD-%E2%9E%9C-%EC%9E%90%EC%8B%9D%EC%B0%BD%EC%9D%98-%EA%B0%92-%EC%A0%84%EB%8B%AC)
- [토스트ui - 메세지 채널](https://ui.toast.com/posts/ko_20220831#messagechannel)
- [미디움블로그 - 브라우저 탭 간 소통 방법 4가지](https://blog.bitsrc.io/4-ways-to-communicate-across-browser-tabs-in-realtime-e4f5f6cbedca)
