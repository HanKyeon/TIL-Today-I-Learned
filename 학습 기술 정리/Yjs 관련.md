# Yjs + y-webrtc + presence + syncedStore 정리

학습 후기 : **공동작업 툴 유용하다.**

흐름 자체는 아래와 같음.

```
npm install yjs // Yjs 설치 명령어
npm install y-webrtc // Yjs의 시그널링 서버를 사용하기 쉽게 만든 라이브러리 설치
npm install y-websocket // Yjs의 웹소켓 서버를 쉽게 사용하기 위한 라이브러리. webrtc와 선택.
npm install @y-presence/client // 시그널링 서버에 있는 다른 conn들의 정보를 다루는데 특화된 라이브러리.
npm install @y-presence/react // 그 중에 리액트에 특화
npm install @syncedstore/core // 연결된 공통 store를 사용하기 위한 라이브러리
npm install @syncedstore/react // 그 중에서 react에 특화된.
```

1. 설치
2. room provider로 어디서 yjs를 사용할지 명시
3. presence 등 추가 세팅이 필요할 경우 세팅
4. y-webrtc || y-websocket을 이용하여 signaling server connect
5. webrtc에서 사용할 store를 context api로 지정
6. context provider를 만들어서 roomprovider 내부에서 제공.
7. 이후 syncedStore 라이브러리를 통해 yjs Doc을 가져옴.
8. useSyncedStore를 통해 선언된 컨텍스트 API의 state를 가져오면 해결.
9. 만약 다른 사용자를 가져오고 싶다면 presence 라이브러리를 통해 다른 user 정보를 받아올 수 있음.

## WHY?

- 공동작업 처리 하려고.

## WHAT?

1. Yjs

- 가장 큰 개념의 라이브러리.

2. y-webrtc

- yjs를 위한 wss 기본 서버 제공 및 시그널링 서버 js 코드 제공

3. presence

- 공동 작업 시 다른 conn의 정보를 알 수 있는 것에 도움을 주는 라이브러리. useOthers 등 제공.

4. syncedStore

- 공동 작업 시 함께 사용 할 저장소.
- 기본적으로 서버가 열려 있다면 그 state를 연동하지만 없다면 빈 값으로 초기화해준다.

## HOW?

1. Yjs를 사용한다는 명시를 해줘야 함.

```js
  let { state, doc, figmaY } = useYjsState(); // Yjs store의 경우 context api를 사용하였기에 이런 형태로 호출.
  const store = useSyncedStore(state); // synced된 store를 사용하기 위해 store를 사용.
  const [awareness, setAwareness] = useState<Awareness>(); // awareness는 사용자와 연결을 위함.
  useEffect(
    function () {
      let provider: WebrtcProvider; // y-webrtc 사용하기 위함.
      if (state && spaceId?.length) {
        provider = new WebrtcProvider( // 새 객체
          `ssafast${spaceId}`, // 방 이름
          getYjsDoc(state) as any,
          {
            signaling: [ // 시그널링서버 세팅. 없다면 기본적으로 제공하는 서버로 이용됨.
              // `ws://localhost:4444`, // 데브 쓸 때 띄우는 용도
              `wss://www.ssafast.com/ws`,
            ],
          }
        );
        provider.connect();
        const { awareness: innerAwareness } = provider;
        setAwareness(innerAwareness);
      }
      return function () {
        console.log('디스커넥트');
        provider.disconnect();
      };
    },
    [state, spaceId]
  );
  // 이 아래는 정보가 처음에 없을 때 넣어준다! 라는 개념으로 넣었음.
  useEffect(
    function () {
      if (!awareness && spaceFrameDataLoading) {
        return;
      }
      if (!figmaY.length && spaceFrameData) {
        figmaY.push([...spaceFrameData.figmaSections]);
      }
    },
    [awareness, spaceFrameData, baseUrls]
  );

<YjsProvider>
  {awareness && userData && (
    <RoomProvider<PresenceUserData> // 룸 프로바이더에서 프리센스로 유저 데이터 이렇게 다룰거다 명시하고, 자기 자신 값은 이렇다고 명시.
      key={`RoomProvider`}
      awareness={awareness}
      initialPresence={{
        name: `${userData?.name}`,
        color: `#${Math.round(Math.random() * 0xffffff).toString(16)}`,
        step: 1,
        img: userData?.profileImg,
      }}
    >
      <WorkContainer store={state} />
    </RoomProvider>
  )}
</YjsProvider>
```

1. 우선 나는 Yjs Provider를 만들었음.

```js
import { SpaceFigma } from '@/hooks/queries/queries';
import { SpaceParams } from '@/pages/space';
import syncedStore, { getYjsDoc, getYjsValue } from '@syncedstore/core';
import { useRouter } from 'next/router';
import {
  PropsWithChildren,
  useContext,
  createContext,
  useEffect,
  useState,
} from 'react';
import { WebrtcProvider } from 'y-webrtc';
import {
  DocTypeDescription,
  MappedTypeDescription,
} from '@syncedstore/core/types/doc';
import { Awareness } from '@y-presence/client';
import { SpinnerDots } from '../common/Spinner';
import Modal from '../common/Modal';
import { PresenceUserData } from './presence-type';
import * as Y from 'yjs';
import { YArray } from 'yjs/dist/src/internals';

interface YjsInterface {
  state: MappedTypeDescription<{
    figmaList: SpaceFigma[];
    apiConnectList: any[];
    apiList: any[];
    useCaseList: any[];
    overloadList: any[];
    baseUrlList: string[];
    editors: PresenceUserData[];
    fragment: 'xml';
  }>;
}

const YjsContext = createContext<YjsInterface>({
  state: syncedStore({
    figmaList: [] as SpaceFigma[],
    apiConnectList: [] as any[],
    apiList: [] as any[],
    useCaseList: [] as any[],
    overloadList: [] as any[],
    baseUrlList: [] as string[],
    editors: [] as PresenceUserData[],
    fragment: 'xml',
  }),
});

const YjsProvider = function ({ children }: PropsWithChildren) {
  const { Provider } = YjsContext;
  const { state } = useContext(YjsContext);
  return <Provider value={{ state }}>{children}</Provider>;
};

export const useYjsState = function () {
  const value = useContext(YjsContext) as YjsInterface;
  const { state } = value;
  let doc = getYjsDoc(state);
  let figmaY: YArray<SpaceFigma> = doc.getArray('figmaList');
  return { state, doc, figmaY };
};

export default YjsProvider;

```

## WHAT IF?

## 참고

https://lucky516.tistory.com/217

- loader 개념 : 페이지가 렌더링 될 때 사용 할 데이터를 불러오는 함수?이다.
- Hook을 이용해 해당 라우터 내라면 어디서든 사용이 가능하다.
