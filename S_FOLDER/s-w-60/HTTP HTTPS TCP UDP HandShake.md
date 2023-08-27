### 참고

- https://doozi0316.tistory.com/entry/HTTPHTTPS%EB%9E%80-TCP-UDP-HandShake-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC
- https://seongonion.tistory.com/74
- https://jee-goo.tistory.com/entry/Web-HTTP%EB%9E%80
- https://pks2974.medium.com/website%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%B3%B4%EC%97%AC%EC%A7%80%EA%B2%8C%EB%90%98%EB%8A%94-%EA%B1%B8%EA%B9%8C-1-108009d4bdb
- https://developer.mozilla.org/ko/docs/Web/HTTP/Messages
- https://tech.ssut.me/https-is-faster-than-http/
- https://goodgid.github.io/Server-DNS/#dns-%EC%84%9C%EB%B2%84%EB%8A%94-2%EC%A2%85%EB%A5%98
- 위의 글을 읽고 정리하기로 맘을 먹었다.

### HTTP

- Hyper Text Transfer Protocol
- 클라이언트와 서버간 데이터를 주고 받기 위한 규약, protocol이다.
- 데이터는 텍스트, 이미지, 동영상 등 모든 종류이다.
- HTTP 종류에는 TCP, UDP 방식이 있으며, 80포트를 사용한다.

### TCP

- Transmission Control Protocol
- 서버와 클라이언트 1:1 연결을 지향하며 신뢰할 수 있는 통신을 제공한다.
- 양쪽에 연결을 수립한 뒤 데이터를 전송하고 연결을 종료한다.
- 일반적인 HTTP 통신은 TCP 방식을 따르고 있다.

### UDP

- User Datagram Protocol
- 1:1 혹은 1:N 비연결을 지향하며 신뢰할 수 없는 통신을 제공한다.
- 비연결 이라는 말은, 말 그대로 서버와 클라이언트가 연결되어 있지 않다는 뜻이다.
- TCP와 달리 연결 설정 과정이 필요 없고, 단지 소켓의 생성과 데이터 송수신 과정만 존재한다. TCP와 비교하면 신뢰할 수는 없지만 연결 수립에 필요한 부하가 없고 보다 빠르다.

### TCP와 UDP의 차이

|                        TCP                        |                                    UDP                                     |
| :-----------------------------------------------: | :------------------------------------------------------------------------: |
|               메시지 수신 확인 가능               |                           메시지 수신 확인 불가                            |
|    메시지가 보내진 순서를 보장하기 위해 재조립    |                     메시지 도착 순서를 예측할 수 없음.                     |
|       UDP에 비해 작업이 많아 속도가 느리다.       |                   TCP보다 속도가 빠르고 오버헤드가 적다.                   |
| 통신 안정성 및 순차적인 전달이 필요한 경우에 사용 | 오류의 검사 및 수정이 필요 없는 경우에 사용. ex) DNS, VOIP, 온라인 게임 등 |

- DNS란 Domain Name System의 약어로, IP 주소와 도메인 명을 교환하여 트리 구조로 되어있다.

### HTTP 메시지 구조

1. Request

- 통신 방법, host, os/browser 정보, 컨텐츠 타입, 클라 언어, 인코딩, 커넥션, 컨텐트 타입, 렝스 등을 가져야 한다.
- body의 경우, post put patch 등 서버에 데이터를 전송하는 경우에만 삽입된다.

2. Response

- protocol, status, 브라우저 정책(CORS관련 Access control allow origin), 커넥션, 컨텐트 인코딩, 시간, ETag, 요청 최대 갯수, 웹 시간 서버시간, 쿠키, 인코딩 변환, X-Frame-Options 등을 포함한다.
- Bodt의 경우 응답 마지막 부분에 들어가며, 특정 status code에 대해 없는 경우도 있다.

### TCP Handshake

- TCP 방식에는 연결 과정이 필요하다.
- 연결을 수립할 때는 3way-Handshake, 종료할 때는 4way-Handshake를 사용한다.
  ![tcpHandShake](./tcphandshake.png)

#### 3 way HandShake

- 간단히 말해서 A=>B=>A=>B 순으로 수신 여부를 확인하는 것으로 보인다.
- 클라이언트는 접속을 요청하는 SYN 패킷을 보낸다. SYN을 패킷을 보냄과 동시에 SYN/ACK 응답을 기다리기 위해 SYN_SENT 상태로 변하게 된다.
- 서버는 SYN 요청을 받고, 클라이언트에게 요청을 수락하는 ACK 패킷과 SYN 패킷을 보내고, SYN_RCVD 상태로 변하여 클라이언트가 ACK 패킷을 보낼 때까지 기다리게 된다.
- 클라이언트는 서버에 ACK 패킷을 보내고, 이후 ESTABLISHED 상태가 되어 데이터 통신이 가능하게 된다.

- SYN : synchronize sequene numbers의 약어로, 연결 확인을 위해 보내는 무작위 숫자값이다.
- ACK : acknowledgements의 약어로, 클라 혹은 서버로부터 받은 SYN에 1d를 더해 SYN을 잘 받았다는 ACK이다.
- ISN : initial sequence numbers의 약어로, 클라와 서버가 각각 처음으로 생성한 SYN을 뜻한다.
- CLOSED : 연결을 수립하기 전 기본 상태이다.
- LISTEN : 포트가 열린 상태로 연결 요청을 대기하는 상태이다.
- SYN_SENT : SYN을 요청한 상태이다.
- SYN_RECEIVED : SYN 요청을 받고, 상태의 응답을 기다리는 상태이다.
- ESTABLISHED : 연결 수립이 완료되어 서로 데이터를 교환할 수 있는 상태이다.

#### 4 way HandShake

- 간단히 말해서 A=>B=>B=>A=>B 순서이다.
- 서버와 클라이언트가 TCP 연결이 되어있는 상태에서 클라이언트가 접속을 끊기 위해 CLOSE() 함수를 호출하게 된다. 이후 CLOSE() 함수를 호출하며 FIN segment를 보내게 되고, 클라이언트는 FIN_WAIT1 상태로 변하게 된다.
- 서버는 클라이언트가 CLOSE() 한다는 것을 알게 되고, CLOSE_WAIT 상태로 바꾼 후, ACK segment를 전송한다. 즉, 클라이언트가 끊을 것이라는 신호를 받았다는 의미이고, CLOSE_WAIR를 통해 자신의 통신이 끝날 때까지 기다리는 상태가 된다.
- ACK segment를 받은 클라이언트는 FIN_WAIT2로 변환되고, 이 때 서버는 CLOSE() 함수를 호출하고 FIN segment를 클라이언트에 보낸다.
- 서버도 연결을 닫았다는 신호를 클라이언트가 수신하면 ACK segment를 보낸 후, TIME_WAIT 상태로 전환된다. 이후 모든 과정이 끝나면 CLOSED 상태로 변환된다.

- CLOSE : 연결을 수립하기 전의 시본 상태
- ESTABLISHED : 연결 수립이 완료되어 서로 데이터를 교환할 수 있는 상태이다.
- CLOSE-WAIT : 상대방의 FIN, 종료 요청을 받은 상태이다. 상대방 FIN에 대한 ACK를 보내고, 애플리케이션 종료를 알린다.
- LAST_ACK : CLOSE-WAIT 상태를 처리 후 자신의 FIN 요청을 보낸 후, FIN에 대한 ACK를 기다리는 상태.
- FIN-WAIT-1 : 자신이 보낸 FIN에 대한 ACK를 기다리거나 상대방의 FIN을 기다리는 상태
- FIN-WAIT-2 : 자신이 보낸 FIN에 대한 ACK를 받았고, 상대방의 FIN을 기다린다.
- CLOSING : 상대방의 FIN에 ACK를 보냈지만 자신의 FIN에 대한 ACK를 못받은 상태
- TIME-WAIT : 모든 FIN에 대한 ACK를 받고 연결 종료가 완료된 상태. 새 연결과 겹치지 않도록 일정 시간 동안 기다린 후, CLOSED로 전이한다.

### HTTP 통신 과정

1. 브라우저에서 URL을 분석하여 HTTP Request 메시지를 만들고 웹 서버로 전송한다. 이 때, 브라우저는 OS를 통해 메시지를 전달하는데, 어디로 보낼 지는 IP 주소로 지정해야 한다. 이 과정에서 웹 서버의 도메인 명을 DNS 서버에 조회하여 IP 주소를 얻는다.

2. protocol stack (운영체제에 내장된 네트워크 제어용 소프트웨어)은 브라우저로부터 받은 메시지를 패킷 속에 저장한 뒤, LAN 어댑터를 통해 패킷을 LAN 케이블로 송출한다.

3. LAN 어댑터가 송신한 패킷은 스위칭 허브를 경유하여 인터넷 접속용 라우터에 도착하고 인터넷으로 들어간다.

4. 패킷은 인터넷의 입구에 있는 액세스 회선에 의해 POP(Point Of Presence, 통신 사용 라우터)까지 운반된다. 이후 POP를 거쳐 인터넷의 핵심부로 들어가게 된다. 그리고 수많은 고속 라우터들 사이로 패킷이 목적지를 향해 흘러가게 된다.

5. 패킷은 인터넷 핵심부를 통과하여 웹 서버 측의 LAN에 도착한다. 웹 서버의 방화벽이 도착한 패킷을 검사하고 패킷이 웹 서버까지 가야하는지 가지 않아도 되는지 캐시 서버가 판단하여 굳이 서버까지 가지 않아도 되는 경우를 골라낸다. 페이지의 데이터 중에 다시 이용할 수 있는 것이 있으면 캐시 서버에 저장된다.

6. 패킷이 물리적인 웹 서버에 도착하면 웹 서버의 프로토콜 스택은 패킷을 추출하여 메시지를 복원하고 웹 서버 애플리케이션에 넘긴다. 메시지를 받은 웹 서버 애플리케이션은 요청 메시지에 따른 데이터를 응답 메시지에 넣어 클라이언트로 회신한다.

7. 왔던 방식대로 응답 메시지가 클라이언트에게 전달된다.

### HTTPS

- Hyper Text Transfer Protocol over Secure socket layer의 약자.
- HTTP는 암호화되지 않은 정보, 즉 평문으로 통신하기 때문에 보안이 취약한 프로토콜이다. 그렇기에 등장한 것이 HTTPS이다.
- 기본 포트는 443이다. 원래 HTTP는 TCP와 직접 통신했지만, HTTPS에서 HTTP는 SSL과 통신하고 SSL이 TCP와 통신한다. SSL을 사용한 HTTPS는 암호화와 증명서, 안전성 보호를 이용할 수 있게 된다.
- 대칭 키와 공개키 암호화 방식을 혼합하여 보안 통신을 구현한다. 대칭키를 공개키 암호화 방식으로 교환한 다음에 그 후 통신은 대칭키를 사용하는 방식이다. 공개키 암호에서는 서로 다른 두개의 키 페어(비밀 키, 공개 키)를 사용한다. 비밀 키는 알려지면 안되는 키이며 공개키는 누구에게나 알려져도 괜찮은 키이다.

#### HTTPS 통신 과정

- 클라이언트가 상대의 공개키를 사용해 함호화를 한다.
- 서버는 자신읜 비밀키를 사용해 복호화를 시도한다. 이 방식은 암호를 푸는 비밀키를 통신으로 보낼 필요가 없으며 도청에 의해서 키를 빼앗길 걱정이 없다.

- 공개 키가 진짜인지 아닌지를 서버에서 증명하기 위해 인증기관Certificate Authority과 그 기관이 발행하는 공개키 증명서가 이용되고 있다. 인증 기관은 클라이언트와 서버 모두 신뢰하는 제 3자 기관이다.
- 공개키를 인증 기관에 제출하면 인증 기관은 제출된 공개키에 디지털 서명을 하고, 서명이 끝난 공개키를 만든다. 그 후 공개키 인증서에 서명이 끝난 공개키를 담는다.

- 과거에는 HTTPS 인증서에 대한 비용이 발생했으나, 구글 모질라 등에서 Let's Encrypt라는 이름의 무료 HTTPS 인증서를 보급해주는 기관을 만들었으니 그것으로 HTTPS 인증서를 무료로 사용이 가능하다.
