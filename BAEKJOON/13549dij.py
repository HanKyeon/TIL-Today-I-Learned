'''
숨바꼭질3

현재 위치 0이상 10만이하 n, 동생은 0이상 10만이하 k
걷거나 순간이동.
걷기는 1초 후 -1 혹은 +1로 이동. 순간이동은 0초 후 바로 2*x로 이동.
동생 가장 빨리 몇 초내로 찾음?

입력
N, K 제시

출력
동생 찾는 가장 빠른 시간.
'''
from heapq import heappop, heappush

def dij(sta, end):
    dst = [int(10e9)] * (end*2+1)
    dst[sta] = 0
    heap = []
    heappush(heap, (0, sta))
    while heap:
        sumc, now = heappop(heap)
        if dst[now] < sumc:
            continue
        a = now*2
        while a != 0 and a <= end*2:
            if dst[a] > sumc:
                dst[a] = sumc
                heappush(heap, (sumc, a))
            a *= 2
        if 0<=now+1<=end*2 and dst[now+1] > sumc + 1:
            dst[now+1] = sumc + 1
            heappush(heap, (sumc+1, now+1))
        if 0<=now-1<=end*2 and dst[now-1] > sumc + 1:
            dst[now-1] = sumc + 1
            heappush(heap, (sumc+1, now-1))
    return dst[end]

n, k = map(int, input().split())
if k <= n:
    print(n-k)
else:
    print(dij(n, k))

'''
from collections import deque

def bfs(sta, end):
    dst = [int(10e9)] * (end*2+1)
    q = deque()
    q.append((0, sta))
    dst[sta] = 0
    while q:
        sumc, now = q.popleft()
        if now == 0:
            if dst[now+1] > sumc+1:
                dst[now+1] = sumc+1
                q.append((sumc+1, now+1))
        elif now<end*2:
            if dst[now-1] > sumc+1:
                dst[now-1] = sumc+1
                q.append((sumc+1, now-1))
            if dst[now+1] > sumc+1:
                dst[now+1] = sumc+1
                q.append((sumc+1, now+1))
            a = now*2
            while a <= end*2:
                if dst[a] > sumc:
                    dst[a] = sumc
                    q.insert(0, (sumc, a))
                a *= 2

    return dst[end]

n, k = map(int, input().split())
if k <= n:
    print(n-k)
else:
    print(bfs(n, k))
'''





