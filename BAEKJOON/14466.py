'''
소가 길을 건너간 이유 6

n*n 목초지. 격자.
k마리 소, 각 소는 서로 다른 목초지. 길을 건너지 않으면 만나지 못하는 소의 쌍 수.

입력
n, k, r 제시.
r개 줄 길 제시. 상하좌우 행열행열 제시. 1이상 n이하. k줄 소 위치 행렬 제시.

출력
못건너면 못만나는 소가 몇 쌍인지 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(h, w):
    global nn
    q = deque([(h, w)])
    v[h][w] = 1
    ret = 1 if g[h][w] else 0
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<nn and 0<=nw<nn and not v[nh][nw]:
                if g[nh][nw] == 1:
                    ret += 1
                v[nh][nw] = 1
                q.append((nh, nw))
    return ret

mov = [(-1,0),(0,1),(1,0),(0,-1)]
n, k, r = map(int, input().rstrip().split())
nn = n*2-1
g = [[0]*(nn) for _ in range(nn)]
v = [[0]*(nn) for _ in range(nn)]
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().rstrip().split())
    r1, c1, r2, c2 = (r1-1)*2, (c1-1)*2, (r2-1)*2, (c2-1)*2
    v[(r1+r2)//2][(c1+c2)//2] = 1
for i in range(1, nn, 2):
    for j in range(1, nn, 2):
        v[i][j] = 1
for _ in range(k):
    h, w = map(int, input().rstrip().split())
    g[(h-1)*2][(w-1)*2] = 1
cowz = []
for i in range(nn):
    for j in range(nn):
        if v[i][j]:
            continue
        a = bfs(i, j)
        if a:
            cowz.append(a)
ans = 0
for i in range(len(cowz)-1):
    fst = cowz[i]
    for j in range(i+1, len(cowz)):
        ans += fst * cowz[j]
print(ans)

'''
5 5
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
5 4 4
2 2 1 2
2 2 2 1
2 2 3 2
2 2 2 3
2 2
3 3
4 4
3 4
'''
