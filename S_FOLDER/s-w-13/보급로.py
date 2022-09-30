'''
보급로

시작지에서 도착지까지 도로 복구를 빠른 시간내로 수행하려 한다.
도로가 파인 깊이에 비례해 복구 시간 증가.
복구 시간이 가장 짧은 경로에 대해 총 복구 시간.
깊이 1은 복구 1
시작은 0,0 도착은 n-1, n-1

입력
테케 수
n
지도 제시

출력
#테케 답
'''
from heapq import heappop, heappush

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

def 레쓰고(tc):
    n = int(input())
    g = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    v = [[int(10e9)]*n for _ in range(n)]
    heap = [(0, 0, 0)]
    v[0][0] = 0
    while heap:
        cost, h, w = heappop(heap)
        if v[h][w] < cost:
            continue
        if h==n-1 and w==n-1:
            print(f"#{tc} {cost}")
            return
        for i in range(4):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<n and 0<=nw<n and v[nh][nw] > cost+g[nh][nw]:
                v[nh][nw] = cost+g[nh][nw]
                heappush(heap, (v[nh][nw], nh, nw))

for tc in range(1, int(input())+1):
    레쓰고(tc)











