'''
N*N
2에서 3까지 몇 칸 가야 하는가

입력
테케T
N
미로

출력
#T 몇칸 가야하는지 못가면 0
'''
from collections import deque

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(input()) for _ in range(n)]
    v = [[0]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == '2':
                q.append((i, j, 0))
                v[i][j] = 1
    ans = 0
    while q:
        h, w, c = q.popleft()
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0 <= nh < n and 0 <= nw < n and v[nh][nw] == 0 and g[nh][nw] == '0':
                v[nh][nw] = 1
                q.append((nh, nw, c+1))
            if 0 <= nh < n and 0 <= nw < n and v[nh][nw] == 0 and g[nh][nw] == '3':
                v[nh][nw] = 1
                ans = c
                break
        if ans != 0:
            break
    print(f"#{testcase} {ans}")








