'''
벽 k번 부수고 이동하기.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, m, k = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
v = [[k+1]*m for _ in range(n)]
heap = [(1, 0, 0, 0)]
fla = False
while heap:
    dep, cnt, h, w = heappop(heap)
    if h==n-1 and w==m-1:
        fla = True
        break
    if v[h][w] < cnt:
        continue
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '0':
            if v[nh][nw] > cnt:
                v[nh][nw] = cnt
                heappush(heap, (dep+1, cnt, nh, nw))
        if 0<=nh<n and 0<=nw<m and g[nh][nw] == '1':
            if v[nh][nw] > cnt+1:
                v[nh][nw] = cnt+1
                heappush(heap, (dep+1, cnt+1, nh, nw))
if fla:
    print(dep)
else:
    print(-1)














