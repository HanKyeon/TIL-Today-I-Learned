'''
음료수 얼려먹기
'''
from collections import deque

n, m = map(int, input().split())

table = deque()

g = []
# 하 상 우 좌
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n) :
    g.append(list(map(int, input())))

def bfs(x, y) :
    if g[x][y] == 1 :
        return False
    g[x][y] = 1
    table.append((x, y))
    while table :
        nx, ny = table.popleft()
        for i, j in zip(dx, dy) :
            if 0 <= nx + i < n and 0 <= ny + j < m :
                if g[nx+i][ny+j] != 1 :
                    g[nx+i][ny+j] = 1
                    table.append((nx+i, ny+j))
    return True

c = 0
for a in range(n) :
    for b in range(m) :
        if bfs(a, b) :
            c += 1
print(c)





