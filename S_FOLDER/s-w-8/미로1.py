'''
미로

1,1에서 출발해서 목적지 도착 가능?
'''

from collections import deque

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

for testcase in range(1, 11):
    _ = input()
    g = [list(input()) for _ in range(16)]
    q = deque()
    for i in range(16):
        for j in range(16):
            if g[i][j] == '2':
                q.append((i, j))
    ans = 0
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<16 and 0<=nw<16 and g[nh][nw] == '0':
                g[nh][nw] = '5'
                q.append((nh, nw))
            elif 0<=nh<16 and 0<=nw<16 and g[nh][nw] == '3':
                ans = 1
                break
        if ans:
            break
    print(f"#{testcase} {ans}")
