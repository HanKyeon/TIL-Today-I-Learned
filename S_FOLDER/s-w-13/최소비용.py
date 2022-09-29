'''
다익스트라 미궁 이동
'''
from heapq import heappop, heappush

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    heap = [(0, 0, 0)]
    dst = [[int(10e9)]*n for _ in range(n)]
    dst[0][0] = 0
    while heap:
        cost, h, w = heappop(heap)
        if h == n-1 and w == n-1:
            break
        if dst[h][w] < cost:
            continue
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n:
                cha = g[nh][nw] - g[h][w]
                if cha > 0:
                    if dst[nh][nw] > cost+1+cha:
                        dst[nh][nw] = cost+1+cha
                        heappush(heap, (cost+1+cha, nh, nw))
                else:
                    if dst[nh][nw] > cost+1:
                        dst[nh][nw] = cost+1
                        heappush(heap, (cost+1, nh, nw))
    print(f"#{tc} {cost}")




