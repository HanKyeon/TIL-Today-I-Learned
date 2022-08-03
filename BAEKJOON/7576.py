'''
도마도

bfs 문제길래 풀어보려 함.
bfs를 카운트 하면서 해나감. bfs 할 때 이전 값에 1 더한걸로 테이블을 고치는 형태로.
-1은 통과 불가. 음수 조건일 때 bfs 미실행을 주자.
1의 위치도 찾아야 한다. 1의 위치에서 함께 bfs를 실행한다.
1 더한걸 고치는 형태는 무슨 그냥 0이면 1로 지우면서 가자. 카운트 따로 넣어주고.

이후 테이블에 0이 있다면 -1 출력
아니라면 카운트 출력.

'''
from collections import deque
import sys

m, n = map(int, input().split())

g = []
for _ in range(n) :
    g.append(list(map(int, (sys.stdin.readline().rstrip()).split())))
re = 0

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

for i in range(n) :
    for j in range(m) :
        if g[i][j] == 1 :
            q.append([i, j])

while q :
    x, y = q.popleft()

    for s in range(4) :
        if 0 <= x + dx[s] < n and 0 <= y + dy[s] < m and g[x + dx[s]][y + dy[s]] == 0 :
            q.append(([x + dx[s], y + dy[s]]))
            g[x + dx[s]][y + dy[s]] = g[x][y] + 1
        else :
            continue
nc = 0
for tt in g :
    if tt.count(0) :
        nc = -1
    else :
        re = max(re, max(tt))
if nc == 0 : print(re-1)
elif nc == -1 : print(nc)



