
#비트연산은 활용과 확장이 힘들다!

백트래킹 이따 가볍게 맛보기 할 것이다.

백트래킹은 상태 트리를 만들어서 한다. 연습을 해서 표현하고 구현하는게 중요하다.

트리는 이진트리, 멀티트리가 있다. YES NO는 다 이진트리. 웬만해선 이진트리로 해라.

비트연산처럼 쓸거냐 안쓸거냐

문교수님 스타일:

종료 조건에 들어갈 변수를 제일 먼저 둔다.

아래 형태로 만든다 재귀를.

함수(종료조건, 파라미터..):
  종료조건
   return

  함수(종료조건+1, 파라미터..)
  함수(종료조건+1, 파라미터..)

질문1. 백트래킹? dfs?
 섞어쓰기도 하고 구분하기도 함. 연습하면서 익숙해지는거다.
 브루트 포스인데, 브루트 포스 중 안해도 되는 것들을 제거하며 진행하는 것이다.























