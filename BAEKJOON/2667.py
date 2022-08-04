'''
단지 번호 붙이기

머리를 썼으면 좀 쉬고 나서 하자
'''
from collections import deque
import sys
# 입력
n = int(input())
g = [[] for _ in range(n)]
for i in range(n) :
    g[i] = list(map(int, list((sys.stdin.readline().rstrip()))))
# x, y 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 담을 변수
apt = []
# bfs
def bfs(g, a, b) :
    # 첫 방문지 방문 기록 및 덱 추가 카운트 추가
    q = deque()
    q.append((a, b))
    g[a][b] = 0
    c = 1
    # bfs 실행
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 1:
                g[nx][ny] = 0
                q.append((nx, ny))
                c += 1
            else : 
                continue
    return c

for i in range(n) :
    for j in range(n) :
        if g[i][j] == 1 :
            apt.append(bfs(g, i, j))


print(len(apt))
apt.sort()
for i in range(len(apt)) :
    print(apt[i])

c=0

def dfs(a, b) :
    global c
    if 0 <= a < n and 0 <= b < n and g[a][b] == 1 :
        g[a][b] = 0
        c += 1
        for i in range(4) :
            nx, ny = a + dx[i], b + dy[i]
            dfs(nx, ny)
        return True
    else :
        return False

for i in range(n) :
    for j in range(n) :
        if g[i][j] == 1 :
            dfs(i, j)
            apt.append(c)
            c = 0

print(len(apt))
apt.sort()
for i in range(len(apt)) :
    print(apt[i])

























'''
q = deque()
apt = [0]
c = 1

for a in range(n) :
    for b in range(n) :
        if g[a][b] == 1:
            q.append([a, b, c])
            while q:
                nx, ny, u = q.popleft()
                g[nx][ny] = u
                if g[nx][ny] != 1 :
                    continue
                for i in range(4) :
                    if 0 <= nx+dx[i] < n and 0 <= ny+dy[i] < n and g[nx+dx[i]][ny+dy[i]] == 1 :
                        q.append([nx+dx[i], ny+dy[i], u])
                        g[nx+dx[i]][ny+dy[i]]
            c += 1

print(g)

'''




'''
def dfs(x, y) :
    global cc
    if 0 <= x < n and 0 <= y < n and g[x][y] == cc :
        g[x][y] = cc
        cc += 1
    else :
        return

    for i in range(4) :
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n :
            dfs(x+dx[i], y+dy[i])
    apt.append(cc)
    return
    '''

'''
    if 0 <= x < n and 0 <= y < n and g[x][y] != 0 :
        dep += 1
        g[x][y] = dep
        for i in range(4):
            dfs(x+dx[i], y+dy[i])

for f in range(n) :
    for j in range(n) :
        if g[f][j] == 1 :
            apt.append(dfs(f, j))

print(g)
'''