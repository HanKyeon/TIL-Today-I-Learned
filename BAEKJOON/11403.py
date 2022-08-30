'''
경로 찾기

가중치 없는 방향 그래프 G가 주어졌을 때 모든 정점 i,j에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 갯수 N 제시. 1이상 100이하.
그래프 인접행렬 제시. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 있다는 뜻, 0은 없다는 뜻.
i번째 줄의 i번째 숫자는 항상 0이다. (자기 자신은 0)

출력
총 N개에 걸쳐 문제의 정답을 인접행렬 형식으로 출력. 정점 i에서 j로 가는 경로가 있으면 i,j를 1로, 없으면 0으로.
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(idx): # BFS. v를 변형시키며 탐색하고 끝냄.
    global v
    q = deque()
    q.append(idx)
    while q:
        n = q.popleft()
        for i in gm[n]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)

n = int(input()) # 길이
g = [list(input().rstrip().split()) for _ in range(n)] # 그래프
gm = [[] for _ in range(n)] # 간선 그래프

for i in range(n): # 탐색하면서 1이면 간선 추가
    for j in range(n):
        if g[i][j] == '1':
            gm[i].append(j)
ng = [] # 새 그래프
for i in range(n): # 간선 시작점 확인하면서
    v = [0]*n # 방문처리 매번 새로 해서
    bfs(i) # bfs 실행
    ng.append(v) # 그 v 반환

for i in ng: # 출력
    print(*i)






















