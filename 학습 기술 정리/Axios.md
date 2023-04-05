# Axios 정리

학습 후기 : **개인적으로 가장 좋아하는 라이브러리이다. fetch API보다 간편한 여러가지 기능을 지원한다고 생각하며, AxiosRequestConfig의 형태가 직관적이고 읽기 쉽다고 생각한다.**

## WHY?

- 비동기 통신을 위한 라이브러리. 다양한 기능을 제공한다.
-
- AJAX, fetch API, Axios 3가지 라이브러리를 가장 많이 쓴다.
  - AJAX는 Jquery를 써야 호환성이 보장되고, Promise 기반이 아닌, callback 기반이다.
  - fetch API는 ES6 버전으로 업그레이드 되면서 들어온 라이브러리인데 지원하지 않는 브라우저가 존재하고, 네트워크 에러 발생 시 response timeout 기능이 없기에 따로 만들어주거나 기다려야 한다. 또한, json을 직렬화하는 과정이 필요하기에 불편한 점이 많다.
  - 그렇기에 일반적으로 Axios를 쓰며, 확장된 기능들 (proxy 객체 params객체 interceptor 등 여러가지 있는 것 같음.) 역시 지원하기에 이점이 크다.

## WHAT?

- 비동기 통신을 위한 라이브러리.
- Promise 객체를 반환하며, axios 객체 역시 만들어서 따로 설정한 axios 객체를 만들어서 별개로 사용이 가능하다.

## HOW?

- 이번에는 다른 것과 다르게 내가 써온 내용을 적겠음.
- 사용법 : `axios.get()` 이런 식으로 사용하는 방법이 있지만 나는 AxiosRequestConfig를 날리는 형태로 쓴다.

```js
import axios from "axios"

const myRequest = axios.create({ baseURL: ``, timeout: 3000 }) // 나만의 axios 객체 생성

myRequest({
  url: ``, // 보낼 url. baseURL + url 형태로 간다.
  baseURL: ``, // baseURL + url 형태로 보내준다.
  transformRequest: [
    function (data, headers) {
      // Do whatever you want to transform the data
      return data
    },
  ], // request 보내는 걸 낚아채서 배열에 있는 함수를 실행한 뒤 보내주는 함수. interceptor인데 put, post patch delete 요청만 낚아챈다.
  transformResponse: [
    function (data) {
      // Do whatever you want to transform the data
      return data
    },
  ], // then이나 catch로 잡히기 전의 response를
  headers: { "X-Requested-With": "XMLHttpRequest" }, // custom header를 설정 할 수는 없는 것 같다... common에서 무슨 세팅을 하면 될 것 같은데 잘 모르겠고, 그냥 고정된 헤더를 사용한다 나는...
  params: {}, // ?= 쿼리 파라미터로 가는 값
  paramsSerializer: function (params) {
    // 사실 이건 잘 모르겠음.
    return Qs.stringify(params, { arrayFormat: "brackets" })
  },
  data: {}, // 보내줄 데이터
  timeout: 1000, // 최대 응답 대기 시간. ms단위.
  withCredentials: false, // cross-site Access Control requset 관련 허용 / 비허용
  adapter: function (config) {
    // 테스트를 쉽게 해주는 커스텀 값이라고 하는데, Promise를 리턴해주고, Valid Response를 제공한다.
    /* ... */
  },
  auth: {
    // Authorization인가 대신 헤더로 들어간다. 오버라이트 된다.
    username: ``,
    password: ``,
  },
  responseType: "json", // 응답 받는 값. arraybuffer, document, text, stream 등 여러 설정 가능.
  responseEncoding: "utf8", // 아마 인코딩 형태일거고, 자세히는 잘 모르겠음. 건드리지 않아본 값.
  xsrfCookieName: "XSRF-TOKEN", // 건드리지 않아본 값.
  xsrfHeaderName: "X-XSRF-TOKEN", // 건드리지 않아본 값
  onUploadProgress: function (progressEvent) {
    // 뭔지 잘 모르겠어서 docs 내용 담았음.
    // Do whatever you want with the native progress event
  },
  onDownloadProgress: function (progressEvent) {
    // 마찬가지로 docs 내용.
    // Do whatever you want with the native progress event
  },
  maxContentLength: 2000, // Response의 최대 길이. in bytes allowed in nod
  maxBodyLength: 2000, //
  validateStatus: function (status) {
    return status >= 200 && status < 300 // default
  },
  maxRedirects: 5, // default
  socketPath: null,
  httpAgent: new http.Agent({ keepAlive: true }),
  httpsAgent: new https.Agent({ keepAlive: true }),
  proxy: {
    // 프록시로, url을 스틸해서 세팅해준다 보면 됨. 프로토콜 방식과 호스트, 포트를 설정해서 url을 꽂아준다. baseURL 말고 프록시 방식으로 지정해도 좋을 듯.
    // 보통 호스트 네임을 window에서 콜 할 수 있으므로, 여기서 hostname을 사용해주면 좋을 것 같다.
    protocol: "https",
    host: "127.0.0.1",
    port: 9000,
    auth: {
      username: "mikeymike",
      password: "rapunz3l",
    },
  },
  cancelToken: new CancelToken(function (cancel) {}), // axios 요청을 cleanup 할 때 쓰이는 cancelToken
  decompress: true,
})
```

## WHAT IF?

- 간단히, 데이터를 직렬화하고 데이터를 풀어 헤치는 과정이 빠지는 것만 해도 좋다고 생각한다.
- 하지만 인터셉터 기능, 간편한 timeout 세팅, 디버깅, cancel token을 통한 캔슬링 등 굉장히 강력한 이점이 크다고 생각했다.
- 사실 통신에 관한 모든 로직을 axios로 관리하면 되서 편하다.

## interceptor 기능

- 사용법만 적도록 하겠음.
- 인터셉터란, 응답을 요청하기 전, 응답을 받기 전 두가지의 경우에 요청과 응답을 채서 원하는 함수를 실행한 뒤 다시 트라이 할 수 있는 기능이다.
- 주로 JWT의 관리 부분에서 사용된다.
- React Query와의 연계를 해야 할 경우, transformResponse로도 가능할 듯 하다. defaults 값을 설정해서!
- 주로 axios 인스턴스를 생성해서 인터셉터 기능을 수행한다.
- 아마도 로그인의 경우, 틀릴 경우 401 에러를 응답하게 되는데 해당 부분을 분리하기 위해서라고 추측.

```js
import axios, { AxiosRequestConfig, AxiosResponse } from "axios"
import store, { DispatchToast } from "store/index"
import { tokenActions } from "store/tokenSlice"

// 해당 인터셉터 인스턴스는 header에 원하는 변수로 설정하는 방법을 defaults로 넣는 방법밖에 몰라서 사용했음.
// Authorization 이외의 값을 넣고 싶었기에 사용하는 인스턴스.
const interceptorRequest = axios.create({
  baseURL: "https://", // base 서버 주소
  withCredentials: true, // 쿠키 사용을 위해 설정
  timeout: 10000, // 10초까지만 대기
})

/*
  서버에 요청을 날리는 axios instance
  https://yamoo9.github.io/axios/guide/api.html#%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4-%EC%83%9D%EC%84%B1
  */
const apiRequest = axios.create({
  baseURL: "https://j8a601.p.ssafy.io", // 서버 주소
  // baseURL: "http://70.12.246.176:8200", // 서버 주소
  withCredentials: true, // 쿠키 사용을 위해 설정
  timeout: 10000, // 10초까지만 대기
})

// request 인터셉터
apiRequest.interceptors.request.use(
  (config) => {
    const state = store.getState() // 리덕스 상태 가져오기
    const accessToken = state.token.accessToken // 리덕스 accessToken 읽기
    // const refreshToken = state.token.refreshToken
    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}` // 리덕스에 accessToken이 있을 경우 Authorization 헤더 추가
    }
    // if (refreshToken) {
    //   config.headers.common[`refreshtoken`] = `Bearer ${refreshToken}`
    // }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// response 인터셉터
apiRequest.interceptors.response.use(
  (res: AxiosResponse) => {
    const newAccessToken = res.headers["accesstoken"] || res.data?.accesstoken
    const newRefreshToken =
      res.headers["refreshtoken"] || res.data?.refreshtoken
    if (newAccessToken) {
      store.dispatch(
        tokenActions.setAccessToken({ accessToken: newAccessToken })
      ) // 리덕스 accessToken 갱신
    }
    if (newRefreshToken) {
      store.dispatch(
        tokenActions.setRefreshToken({ refreshToken: newRefreshToken })
      )
    }
    // console.log("response", res)
    return res
  },
  async (error) => {
    console.log("error", error)
    console.log(`errorStatusCode: ${error.response.status}`)

    const state = store.getState() // 리덕스 상태 가져오기
    const accessToken = state.token.accessToken // 리덕스 accessToken 읽기
    const refreshToken = state.token.refreshToken

    const originalConfig = error.config // 기존 요청 정보 저장 (accessToken 요청 후 재발급을 위해)
    const response = error.response // 에러 정보

    if (response.status === 401) {
      // access Token 재발급
      const config: AxiosRequestConfig = {
        method: `post`,
        baseURL: "https://j8a601.p.ssafy.io", // 서버 주소
        // baseURL: "http://70.12.246.176:8200", // 서버 주소
        url: `/api/auth/reissue`,
      } // accessToken 재발급 관련 설정
      if (accessToken) {
        interceptorRequest.defaults.headers.common[`accesstoken`] = accessToken
      }
      if (refreshToken) {
        interceptorRequest.defaults.headers.common[`refreshtoken`] =
          refreshToken
      }
      await interceptorRequest(config)
        .then((res) => {
          console.log("토큰 재발급 응답:")
          console.log(res)
          const newAccessToken =
            res.headers["accesstoken"] || res.data?.accesstoken
          // const newRefreshToken =
          //   res.headers["refreshtoken"] || res.data?.refreshtoken
          if (newAccessToken) {
            store.dispatch(
              tokenActions.setAccessToken({ accessToken: newAccessToken })
            ) // 리덕스 accessToken 갱신
            // originalConfig.headers.common["accesstoken"] = `${newAccessToken}`
            originalConfig.headers.Authorization = `Bearer ${newAccessToken}`
          }
          // if (newRefreshToken) {
          //   store.dispatch(
          //     tokenActions.setRefreshToken({ refreshToken: newRefreshToken }),
          //   )
          //   originalConfig.headers.common["refreshtoken"] = `${newRefreshToken}`
          // }
          return apiRequest(originalConfig) // 기존 요청 새로운 token으로 재시도
        })
        .catch((err) => {
          console.log("토큰 재발급 에러 : ", err)
          // store.dispatch(DispatchToast("다시 로그인 해주세요.", false))
          return Promise.reject(err)
        })
    } else if (response.status === 403) {
      store.dispatch(
        DispatchToast("토큰이 만료되었습니다. 다시 로그인 해주세요.", false)
      )
      store.dispatch(tokenActions.deleteTokens({}))
    } else if (response.status >= 500) {
      store.dispatch(
        DispatchToast("서버와의 통신에 문제가 발생하였습니다.", false)
      )
    }
    return Promise.reject(error)
  }
)

export default apiRequest
```

## 참고

https://axios-http.com/docs/intro
https://yamoo9.github.io/axios/guide/
https://velog.io/@artlogy/Axios-Front%EC%9A%A9-%ED%95%9C%EB%B0%A9-%EC%A0%95%EB%A6%AC
