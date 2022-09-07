'''
음악 프로그램

순서를 정하기 위해 조건 따져야함.
담당 가수 출연 순서 pd들이 정해서 옴.
1 4 3
6 2 5 4
2 3

경우에 따라서 남일이가 모두를 만족하는 순서를 정하는 것이 불가능할 수도 있다. 예를 들어, 세 번째 보조 PD가 순서를 2 3 대신에 3 2로 정해오면 남일이가 전체 순서를 정하는 것이 불가능하다.

입력
가수N pd수M. 1.2..N 1이상 1000이하 정수 M은 1이상 100이하 정수
피디ㄱ ㅏ정한 순서.

출력
N개 줄. 한 줄에 번호 하나씩.
순서를 정하는 것이 불가능 할 경우 첫째줄에 0 출력.
'''
from heapq import heappop, heappush
import sys
input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
reqn = [0] * (n+1) # 요구 노드
g = [[] for _ in range(n+1)] # 채우면 어느 곳을 만족시켜 주는가. 어느 곳의 reqn을 깎아줄 것인가.
for _ in range(m):
    s = list(map(int, input().rstrip().split())) # 입력
    sl = s.pop(0) # 반복 숫자
    for i in range(1, sl): # i-1과 비교해야 하므로 1부터 순회
        g[s[i-1]].append(s[i]) # 첫번째가 선행되면 두번째로 갈 수 있다.
        reqn[s[i]] += 1 # 두번째의 요구 노드가 증가한다.

heap = [] # 힙으로 풀것임.
for i in range(1, n+1): # 1부터 돌면서 0이면 힙에 넣어준다.
    if reqn[i] == 0:
        heappush(heap, i)
ans = [] # 정답 담을 것.
while heap: # 위상정렬 끝날 때까지
    idx = heappop(heap) # pop
    ans.append(idx) # 정답에 idx 추가.
    for i in g[idx]: # 가는 노드 확인
        reqn[i] -= 1 # 요구 노드 제외
        if reqn[i] == 0: # 요구 노드가 0이 되면
            heappush(heap, i) # 힙에 넣어줘라
if reqn.count(0) == n+1: # 전부 방문 했으면 정상 출력
    for i in ans:
        print(i)
else: # 다 끝났는데도 요구 노드가 남은 노드가 있다면 서로 요구노드인 괴리한 상태. 서순상태.
    print(0)




