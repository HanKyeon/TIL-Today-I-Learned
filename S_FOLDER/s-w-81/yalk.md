# Yalc

- yarn link / yarn pack보다 실용적이라고 생각되어서 작성.

-[참고](https://medium.com/zigbang/yalc-npm-%ED%8C%A8%ED%82%A4%EC%A7%80%EB%A5%BC-%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%95%98%EB%8A%94-%EB%8D%94-%EB%82%98%EC%9D%80-%EB%B0%A9%EB%B2%95-26eebae3f355)

## yarn link

- yarn link는 개발하는 동안 패키지 폴더에 심볼릭 링크를 생성한다.
- 즉, node_modules에 있는 패키지와 로컬 환경 패키지 간의 심볼릭 링크가 생긴다.
- 사용이 간단하다.

- 하지만, 패키지를 2개 링크하거나 했을 때, 상호 dependency가 얽혀서 이슈가 생길 수 있다. 이런 경우, 해당 라이브러리를 의존하는 모든 모듈이 강제로 하나의 경로를 바라보게 고정시킬 수 있다. (alias 설정을 잘 하면 됨.)

## yarn pack

- yarn pack은 설치 가능한 패키지 압축 파일을 생성하는 명령어이다.
- package.json에 해당 압축 파일을 사용한다고 명시하고 install하면 패키지를 사용하는 모든 파일에서 압축 파일의 내용을 바라보게 된다.
- 단점으로는 코드 수정사항으로 핫 리로드가 적용되지는 않는다. 매번 빌드, 인스톨하는 과정을 거쳐야 한다.

## yalc

- yalc는 더 나은 yan link를 목표로 하는 라이브러리이다. 직접 파일을 생성/복사 or 설치하는 대신 로컬 레포를 만들어서 패키지를 손쉽게 설치/업데이트 할 수 있게끔 도와준다. (yalc는 ~/.yalc 경로에 패키지를 저장함.)
- yalc는 yarn pack을 통해 패키징을 한 뒤, 해당 파일을 로컬 레포에 저장을 한다. yalc를 사용할 경우 node_modules까지 ㅅ미볼릭 링크를 생성하는 yarn link와 달리 패키징된 결과물만ㅁ 저장하므로, 서로 다른 경로에 존재하는 동일한 패키지 문제가 발생하지 않는다.

- yalc는 사용법이 직관적이다.
- npm에 배포하듯 패키지를 로컬 레포지토리에 배포하고 (yalc publish) 프로젝트에서 설치하고 (yalc add package) 수정사항이 생기면 패키지에서 다시 yalc publish를 하고 프로젝트에 yalc update package를 해야한다.
- yalc는 편의 기능 역시 제공중. yalc push 명령어를 통해 한번에 배포 및 수정이 진행 가능하다. 별도의 빌드가 필요한 ts pjt의 경우에는 tsc-watch --onSuccess \"yalc push\"" 이런 형태의 스크립트를 작성해서 해결할 수 있다.
- **yalc는 link 역시 지원한다. 대신 로컬 레포에 link를 생성하여 심볼릭 링크를 걸게 된다. yalc link를 사용하면 package.json을 수정하지 않고 테스트가 가능하다.**
