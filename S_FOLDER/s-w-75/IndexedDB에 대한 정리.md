# IndexedDB

- [참고 - mdn 설명이 충분히 잘 되어있음](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Terminology)
- [참고 - 문서](https://velog.io/@longroadhome/%EB%AA%A8%EB%8D%98JS-%EC%8B%AC%ED%99%94-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%97%90-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0-2)
- [참고 - dexie-encrypted](https://github.com/mark43/dexie-encrypted)

- [사용기 - 드림어스 컴퍼니](https://www.blog-dreamus.com/post/indexed-db-%EC%A0%81%EC%9A%A9%EA%B8%B0)

## 정의

- indexedDB란 File, Blob 등 많은 양의 구조화된 데이터를 글라이언트에 저장하기 위한 api이다.

### 장점

- 많은 양의 구조화된 데이터를 클라이언트에 저장할 수 있다.
- Javascript 기반의 객체지향 데이터베이스이다. 즉, Javascript가 인식할 수 있는 자료형과 객체를 저장할 수 있다.
- 트랜잭션을 사용하며 Key-Value 데이터베이스이다.
- IndexedDB는 비동기 API이다.

### 특징

- 관계형 데이터베이스와 같이 트랜잭션을 사용하는 DB 시스템이다. 트랜잭션은 비동기 형식으로 실행된다.
- RDBMS의 고정 컬럼 테이블 대신 JS 기반의 객체지향 DB이다. 인덱스 키를 사용해 저장하고 검색이 가능하며, Error와 Function, DOM Node 등 일부의 JS를 제외하고는 모두 저장이 가능하다.
- 스키마 지정, DB 통신 후 트랜잭션을 통해 데이터를 가져오거나 업데이트한다. CORS를 따른다.

- iframe 같은 서드파티 윈도우 컨텐츠는 브라우저가 삽입된 iframe의 origin에 대해 never acept third party cookies를 설정하지 않았다면 접근이 가능하다.

# WebCrypto API

### 특징

- 웹 브라우저의 Web Crypro API는 외부 JS 종속성 없이 브라우저에 내장된 공통 암호화 기능을 제공한다.
- Web Crypto API에 의해 생성된 키의 메타 데이터 정보는 JS 환경에 노출되지만 키의 내용은 노출되지 않는 등 몇가지 보안상의 이점을 제공한다.
- Web Crypto API에서 키를 생성할 때 추출 가능한 속성을 false로 하여 key를 JS 밖으로 내보낼 수 없도록, 용도를 지정할 수 있도록 할 수 있다.
- CryptoKey는 객체는 IndexedDB 스토리지에 직접 저장이 가능.

- Web Crypto API의 표준 사양은 브라우저 저장소에 암호화된 암호화 키를 저장하는 메커니즘을 명시적으로 제공하지 않음.
- 서버에서 키를 프로비저닝 하려면 클라이언트 수준에서 별도의 언래필 키가 필요한데 이 키는 사용자의 입력이나 비ㅣㅁㄹ번호에서 pbkdf와 같은 키 파생 함수를 이용하여 파생할 수 있지만, UX를 저하시킬 수 있다.

## 현상황

1. 암호화 없이 저장할 경우 개발자 도구를 통해 모든 값을 확인할 수 있음.
2. 암호화를 할 경우 암호화 키가 필요. 암호화 키는 web crypto api를 사용하기에 uint8array가 필요함.
3. 암호화된 자료는 index로 쓰이는 key 값들을 제외하고는 암호화됨.
4. crypto key에 쓰이는 uint8array를 일반적으로 password를 JS API를 통해 arraybuffer로 변경한 뒤 uint8array로 전환하여 사용
5. 해당 uint8array를 key를 저장한 idb에서 꺼내서 사용

### 문제점

0. 동작 관련

- indexedDB는 트랜잭션 데이터베이스 모델을 기반으로 한 RDBMS임. 그리고 NoSQL임.
- key로 등록한 index들로 접근이 가능하며 개발자 도구를 열면 모두 확인이 가능하다.
- 동일 출처 오리진 정책 따른다.
- iframe 같은 서드파티 윈도우 컨텐츠는 브라우저가 삽입된 iframe의 origin에 대해 never acept third party cookies를 설정하지 않았다면 접근이 가능하다.
- 서비스워커에서 사용 가능한 API

- Web Crypto API는 크립토 객체를 뱉어냄.
- 크립토 객체는 "키를 추출할 수 없는 키 객체"를 만들 수 있음. 파싱을 위한 32길이의 Uint8Array가 필요함.

1. 서버 데이터 베이스와 동기화
   => indexedDB 자체가 서버 DB와 동기화 처리하도록 설계되지 않았음.
   => 직접 동기화 해줘야 함.
   => 해당 부분은 프로젝트 진행하면서 고민해야 할 문제 같음. 동기화 시점 등에 대해. (unload 이벤트에서 트랜잭션을 하지 말라고 함)

2. 보안 관련 문제
   => 브라우저에서 암호키와 같은 민감한 데이터를 안전하게 저장할 수 있는 옵션이 거의 없음
   => web crypto API를 통해 읽기만 가능하게 하여 key를 사용이 가능함.
   => webcrypto API를 통해 "키를 추출할 수 없는 키 객체"를 만들고 IndexedDB에 해당 키 객체를 저장해서 사용

3. 다른 탭에서의 업데이트 문제
   => 일반적으로 version을 바꿔서 해결함.
   => versionchange 이벤트는 구식의 IndexedDB 객체가 감지되었을 때 발생
   => 해당 이벤트에 콜백을 달아두면 업데이트 로직 실행 가능.

## 기업 기술 블로그 / docs 위주 확인 결과

1. 실제 db 처럼 사용하는 경우에는 각 보안 라이브러리를 만들어서 사용. 라인에서는 화이트박스 암호와 웹 어셈블리를 사용.
2. 일반적으로는 해당 user에 대해 노출이 되어도 되거나 변경 사항이 적은 file, blob 등을 저장하는 것에 사용중.
3. docs 및 암호화 라이브러리에서는 crypto key를 위한 string | uint8array는 BE에 저장하는 것을 권장. local 저장 비권장.
4. 실제로 크기가 큰 도서 카탈로그, 음악 파일, 영상 파일 등을 저장하는 경우가 대다수이며, mdn에서 역시 이러한 경우를 추천하고 있음.
5. (참고) 메신저에 사용하는 라인의 경우는 화이트박스 암호와 웹 어셈블리를 사용하여 극복한듯함.

## indexedDB 동작

1. 트랜잭션 데이터베이스 모델을 기반으로 구축됨. 관계형 데이터베이스임. RDBMS.
2. 서버 데이터 베이스와 동기화 처리하도록 설계되지 않았음.
3. key value storage로, Error와 Function, DOM Node 등 일부를 제외하고는 모두 저장이 가능하다.
