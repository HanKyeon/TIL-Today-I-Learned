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
# 입력
m, n = map(int, input().split())
g = []
for _ in range(n) :
    g.append(list(map(int, (sys.stdin.readline().rstrip()).split())))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# q에 시작점들 담아주기
q = deque()
# 도마도가 있는 1의 위치 담기
for i in range(n) :
    for j in range(m) :
        if g[i][j] == 1 :
            q.append([i, j])
# bfs
while q :
    x, y = q.popleft()
    # 범위 안에 있고, 거기에 도마도가 있으면 pop한 값에서 1을 더해서 몇일차에 익는지 기록
    for s in range(4) :
        if 0 <= x + dx[s] < n and 0 <= y + dy[s] < m and g[x + dx[s]][y + dy[s]] == 0 :
            q.append(([x + dx[s], y + dy[s]]))
            g[x + dx[s]][y + dy[s]] = g[x][y] + 1
        else :
            continue
nc = 0
re = 0
# 도마도 밭을 행으로 0의 유무 확인, 있으면 -1 뱉고 탈출, 아니면 re에 최대일수 갱신
for tt in g :
    if tt.count(0) :
        nc = -1
        break
    else :
        re = max(re, max(tt))
# 출력. 안익는게 있으면면 -1, 익는데 걸린 날짜 -1 (도마도가 1로 시작했으므로.)
if nc == 0 : print(re-1)
elif nc == -1 : print(nc)



