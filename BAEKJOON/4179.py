'''
불!

지훈이는 미로에서 일을 한다. 미로 탈출 시키자.
탈출 여부, 얼마나 빨리 탈출 할 수 있는지. 사방이동, 사방확산. 가장자리 도착 시 탈출. 벽 못뚫음

입력
n,m 제시.
그래프 제시. # 벽 .공간 J지훈 F불

출력
미로 탈출 못하면 IMPOSSIBLE 출력
미로 탈출 가능한 경우, 가장 빠른 탈출 시간 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
q = deque()
ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 'F':
            q.appendleft((i, j, 'F'))
        elif g[i][j] == 'J':
            q.append((i, j, 'J', 0))
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                ans = 1
while q:
    if ans:
        break
    info = q.popleft()
    if len(info) == 3:
        h, w, val = info
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and (g[nh][nw] == '.' or g[nh][nw] == 'J'):
                g[nh][nw] = val
                q.append((nh, nw, val))
    else:
        h, w, val, cnt = info
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<m and g[nh][nw] == '.':
                if nh == 0 or nh == n-1 or nw == 0 or nw == m-1:
                    ans = cnt+2
                    break
                g[nh][nw] = val
                q.append((nh, nw, val, cnt+1))
if not ans:
    ans = 'IMPOSSIBLE'
print(ans)











