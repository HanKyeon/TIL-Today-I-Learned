# WebSocket

- 웹소켓은 클라이언트와 서버를 연결하고 실시간으로 통신이 가능하도록 하는 통신 프로토콜이다.
- 하나의 TCP 접속에 전이중(duplex) 통신 채널을 제공한다.
- 즉, 웹소켓은 Socket Connection을 유지한 채로 실시간으로 양방향 통신 혹은 데이터 전송이 가능한 프로토콜이다.
- 주로 채팅 애플리케이션, 멀티 플레이, 웍스, 화상회의 등의 분야에서 활용.

- 이전에는 Polling이라 부르는 일정 주기로 서버에 요청하는 방식을 사용하여 유사 웹소켓을 구현했었다.

### WebSocket과 HTTP의 차이

- HTTP는 단방향 통신이다. Stateless를 지향한다. 그렇기에 요청에 대해서만 Response를 제공한다.
- WebSocket은 양방향 통신이다. 즉 Request가 없더라도 Server에서 데이터를 받을 수 있다.

### WebSocket의 동작

- 웹소켓은 HTTP 80포트, HTTPS 442 포트에서 작동한다.
- 웹소켓은 TCP 연결처럼 HandShake를 통해 연결을 맺는다.
- 최초 접속 시 핸드셰이킹을 진행하며, HTTP 업그레이드 헤더를 사용하여 HTTP 프로토콜에서 웹소켓 프로토콜로 변경한다.
- 이후 연결이 맺어지면 어느 한 쪽이 연결을 끊지 않는 이상 영구적인 동일한 채널이 맺어지고, HTTP 프로토콜이 웹소켓 프로토콜로 변경된다. 이 때 데이터 암호화를 위해 WSS 프로토콜 등을 이용 할 수 있다.

### 참고

- https://doozi0316.tistory.com/entry/WebSocket%EC%9D%B4%EB%9E%80-%EA%B0%9C%EB%85%90%EA%B3%BC-%EB%8F%99%EC%9E%91-%EA%B3%BC%EC%A0%95-socketio-Polling-Streaming
