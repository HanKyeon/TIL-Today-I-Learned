'''
전기 버스.

충전지 교환하는 전기버스 예정.
정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행 할 수 있는 정류장 수가 정해져 있다.
방전되기 전에 교체운행해야 한다. 최소 교체 횟수.
정류장, 충전지 제시. 목적지에 도착하는데 필요한 최소한의 교환 횟수 출력. 출발지는 0

입력
테케T
정류장 수n, n-1개 정류장 별 배터리 용량 제시. 맨끝 제외.

출력
#테케T
'''
from collections import deque
from heapq import heappop, heappush

def 레쓰고(idx, fuel, cnt):
    q = deque()
    q.append((idx, fuel, cnt))
    while q:
        idx, fuel, cnt = q.popleft()
        for i in range(fuel, 0,-1):
            nidx = idx+i
            if nidx >= n-1:
                return cnt
            nfuel = nl[idx+i]
            if nfuel == 0:
                continue
            if not v[nidx]:
                v[nidx] = 1
                q.append((nidx, nfuel, cnt+1))

for tc in range(1, int(input())+1):
    nl = list(map(int, input().rstrip().split()))+[0]
    n = nl.pop(0)
    fuel = nl[0]
    ans = int(10e9)
    v = [0]*n
    v[0] = 1
    a = 레쓰고(0, fuel, 0)
    print(f"#{tc} {a}")












