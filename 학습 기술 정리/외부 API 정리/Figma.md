# 개요

- SSAFY 자율 프로젝트를 진행하며 Figma API를 사용하기로 함.
- 해당 부분에 대한 원활한 소통을 위해 필요한 API에 대해 정리.
- 필요한 내용에 대해서만 정리하기에 추가 내용은 docs 참고 바람
- Docs Link : https://www.figma.com/developers/api

## Authentication

- Authentication을 진행하는 방법은 두가지가 있음.
  1. Personal Authentication
  2. OAuth2 Authentication

1. Personal Authentication

- 말 그대로 Figma Setting에서 personal AccessToken을 generate한 뒤, 해당 token을 통해 figma API를 이용하는 것.
- Figma token을 입력 받기에 가장 명확하고 빠르게 사용이 가능.
- 하지만 사용자 입장에서 개인의 token을 입력해야하기에, 프로젝트의 보안과 신뢰성이 중요함.
- 사용법은 어렵지 않음.
- headers에 "X-Figma-Token" 속성을 선언하고, 해당 부분에 할당해주면 사용 가능.
- baseURL은 `https://api.figma.com`

2. OAuth2 Authentication

- Figma Developer로 App을 등록하면 기존 Figma 사용자 계정과 앱 간에 링크가 설정되어 사용자 대신 Figma API를 통해 데이터에 액세스 할 수 있다.
- My Apps에서 앱을 만들고 Client ID와 Client Secret 등을 가지고 사용한다.
- 앱 링크와 EndPoint를 지정해주면 accessToken이 있는 것을 EndPoint로 연결시켜준다.
- 이 때 사용되는 요청 객체는 아래와 같음.

```js
// 이건 window.location.href로 보내줘도 좋다.
{
  baseURL: `https://www.figma.com`,
  url: `/oauth`
  params: {
    "client_id" : "MyApp ClientID", // MyApps에 있는 App의 Client ID
    "redirect_uri" : "MyApp callback", // MyApps에 있는 해당 App의 Callbacks
    "scope" : "file_read", // only `file_read`
    "state" : "some random state for checking", // 해당 부분은 랜덤 값으로, 이후 받았을 때 다시 왔을 때 같은 값인지 체크하는 것
    "response_type" : "code" // only `code`
  }
}
```

- 아래 url로 이동하고 인증하면 params로 code와 state가 들어온다. `callbackLink?code=코드값&state=상태값`
- 이후 code를 통해 OAuthAPI로 accessToken을 받아올 수 있다.
- **중요 : code를 db에 저장해야 할 듯 하다. 해당 코드로 다시 받아오면 되서.**

```js
// 요청 객체
{
  method: `post`,
  baseURL: `https://www.figma.com`,
  url: `/api/oauth/token`,
  params: {
    client_id: `myApps 클라 아이디`,
    client_secret: `myApps 생성 시 받는 secret`,
    redirect_uri: `myApps의 callback에 있는 uri`,
    code: `db에 저장된, 권한 허가 할 때 쓰인 코드.`,
    grant_type: `authorization_code` // 고정
  }
}

// 응답

{
  "user_id": `OAuth2 userId`,
  "access_token" : `토큰`,
  "expires_in" : `만료 시간`,
  "refresh_token": `리프레시 토큰`
}
```

- **중요 : access_token과 refresh_token을 DB에 저장해야 refetch 해올 수 있음!**
- 근데 애초에 access_token 이 좀 오래 가는거 같던뎅... 90일인가
- expire 되었을 때, access token 재발급은 아래로 보내서 재발급 받는다.

```js
// 요청 객체
{
  method: `post`,
  baseURL: `https://www.figma.com`,
  url: `/api/oauth/refresh`,
  params: {
    client_id: `myApps 클라 아이디`,
    client_secret: `myApps 생성 시 받는 secret`,
    refresh_token: `리프레시 토큰`
  }
}

// 응답 객체
{
  "user_id": `OAuth2 userId`, // 확인 안해봤으나 있을듯.
  "access_token" : `토큰`,
  "expires_in" : `만료 시간`,
}
```

- **이하 모든 요청에 토큰 들어감@@@@@@@@**

## Figma Files

1. 공통적으로 가지는 값들

```js
{
  id : string
  name: string
  visible: boolean // default: true
  type: string
  rotation : number // rotation 돌리기 관련
  pluginData : Any // 플러그인 쓰지마!!!!
  sharedPluginData : Any // 쓰지말라고!
  componentPropertyReferences : Map<String, String>
}
```

2. Node type에 따른 속성 값들

- 객체 형태로 작성하겠음.

```js
{
  DOCUMENT: {
    children: Node[]
  }
  CANVAS: {
    children : Node[]
    backgroundColor : Color
    prototypeStartNodeID : String
    flowStartingPoints : FlowStartingPoint[]
    prototypeDevice : PrototypeDevice
    exportSettings : ExportSetting[]
  }
  FRAME: {
    children : Node[]
    locked: boolean
    background : Paint[]
    backgroundColor : Color
    fills : Paint[]
    stroke : Paint[]
    strokeWeight : Number
    strokeAlign : String
    cornerRadius : Number
    rectangleCornerRadii : Number[]
    exportSettings : ExportSetting[]
    blendMode : BlendMode
    preserveRatio : Boolean
    constraints : LayoutConstraint
    layoutAlign : String // INHERIT, STRETCH 등의 데이터와 IN CENTER MAX STRETCH 등 데이터인듯
    transitionNodeID : 적다 말았으니 이따 여기서부터 재작성하자... 양이 넘 많으니 공통점 좀 추려서 진행하자
  }
  GROUP : FRAME과 동일
  VECTOR: {}
  BOOLEAN_OPERATION: {}
  STAR: {}
  LINE: {}
  ELLIPSE: {}
  REGULAR_POLYGON: {}
  RECTANGLE: {}
  TABLE: {}
  TABLE_CELL: {}
  TEXT: {}
  SLICE: {}
  COMPONENT: {}
  COMPONENT_SET: {}
  INSTANCE: {}
  STICKY: {}
  SHAPE_WITH_TEXT: {}
  CONNECTOR: {}
  WASHI_TAPE: {}
}
```

3. 각 속성들의 타입들 관련 내용

- 먼 미래에 작성 예정

## GET file

1. 전체 파일 data fetch 하기 => depth를 2로 하면 document (0) => section (1) => frame (2)

```js
// AxiosRequestConfig
{
  method: `get`,
  baseURL: `https://api.figma.com`,
  url: `/v1/files/파일키` //
  headers: {
    Authorization: `Bearer 피그마 access 토큰`
  },
  params: {
    version: 옵셔널값,
    ids: 옵셔널 배열타입 특정 노드들 배열로 가져오는듯,
    depth: 옵셔널number타입 값 깊이 지정, // 이 값을 통해 적절히 받아오면 될 듯 하다!
    plugin_data: 옵셔널 string
    branch_data: 옵셔널 불리언값
  }
}

// AxiosResponse
{
  document: {
    id, name, type, scrollBehavior, children
  },
  components: {
    컴포넌트ID: {key, name, description, remote, documentationLinks}
  },
  componentSets: {없어서 몰루},
  schemaVersion: 0,
  styles: {
    컴포넌트ID: {key, name, styleType, remote, description}
  }
  name: 플젝 이름,
  lastModified: 최근 수정,
  thumbnailUrl: 썸네일url 바로 나오는듯,
  version: 숫자,
  role: 역할,
  editorType: figma 고정인듯,
  linkAccess: 정해진 특정 몇 string인듯
}
```

2. 특정 노드 data fetch하기

- https://www.figma.com/file/:key/:title?node-id=:id
- 해당 요청은 프레임이든 뭐든 우클릭해서 copy/paste as에서 copy link로 복사해오면 된다.
- api.figma.com 관련해서 요청을 보내면 nodes를 각각의 document로 가지게 만들어서 뱉는다.

```js
// 요청 객체
{
  baseURL: `https://api.figma.com`,
  url: `/v1/files/파일키/nodes`,
  headers: {
    Authorization: `Bearer 피그마 access 토큰`
  },
  params: {
    ids: 노드ID 필수 값 5:2,4:2 이런식으로 comma로 연결시킨 id들을 string으로 주면 다 가져옴.,
    version: 옵셔널값,
    depth: 옵셔널number타입 값 깊이 지정, // 이 값을 통해 적절히 받아오면 될 듯 하다!
    geometry: 옵셔널string,
    plugin_data: 옵셔널 string
  },

}

// 응답 객체

{
  전체 파일 요청과 동일한데,
  nodes: {
    ids에 있는 노드 정보가 각각이 document를 가지고, depth만큼 들어옴.
  }
}

```

3. image fetch 하기.

```js
// 요청 객체
{
  method: `get`,
  baseURL: `https://api.figma.com`,
  url: `/v1/images/:피그마 프로젝트 파일 키`,
  headers: {
    Authorization: `Bearer 피그마 access 토큰`
  },
  params: {
    ids: 작성법 똑같음 아이디,아이디,아이디를 스트링으로 담아 보내면 됨,
    scale: 옵셔널 배율 0.01에서 4 사이값,
    format: 옵셔널 string값 jpg png svg pdf 중 하나,
    svg_include_id: 옵셔널 boolean값이고 기본값 false,
    svg_simplify_stroke: 옵셔널 설명 보는데 뭔 소린지 모르겠음,
    use_absolute_bounds: 옵셔널 설명 보는데 뭔 소린지 모르겠음,
    version: 버전 옵셔널
  }
}
// 응답 객체
{
  err: null,
  images : {
    아이디: 링크,
    아이디: 링크
  }
}
```

4. image fills fetch

- 프로젝트에 사용된 모든 이미지들 link를 fetch 해오는듯!
- 따라서, 우리에겐 필요 없음.

## Comment 관련 API, user, version history, 컴포넌트 & styles, 웹훅, 액티비티로그 등

- 추후 작성 예정

---

# Figma API + React Query 고민

![Figma API 관련 이해](../assets/pjt/FigmaAPI.png)

- url을 보내고, redirectURL에서 code를 받아서 던져줘야 함.
- 이 부분을 팀장의 코드로만 가능하게? 팀장 권한만 가지고 여러번 받아도 되나?

- 필요한 api

  1. code 저장 페이지
     - code 저장에 space ID
     - code 저장 post API
     - code 저장 완료 시
  2. BE측이 code를 통해

- 현재 고민되는 점

  1. get images가 오래 걸리기에 fetch 시작이 최대한 빨라야 함.
  2. 팀 생성 과정에서 figma access / figma refresh를 받는 경우
     - code, figma access, figma refresh를 FE측이 들고 있어야 함.
  3. 팀 생성을 최종 버튼을 눌렀을 때 하는 경우
     - code를 보내고 BE측이 figma access, figma refresh를 받아서 저장, 이후 token을 받아오는 요청이 있어야 함.

  - **즉, 팀 생성의 기준이 명확해야 할 것 같음.**

  => 해결법

  1. Figma Token Table을 하나 생성, 유저에게 귀속.
  2. space의 팀장의 figma token을 가져와서 return 해주는 등 하면 될 듯.
