'''
두 로봇

두 로봇은 임의의 지점에 있다. 한 통로 위에 있으면 통신 가능.
현 위치 제시. 통신하기 위해 이동해야 하는 거리의 합 최솟값.

입력
n, s, e 제시.
a, b, c를 n-1개 제시.

출력
서로 통신하기 위해 현재 위치에서 이동해야 하는 거리의 합 최솟값 정수로 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global n, s, e
    if s==e:
        return 0
    v = [-1]*(n+1)
    v[s] = 0
    q = deque([(s, 0)])
    while q:
        idx, maxi = q.popleft()
        for cost, i in g[idx]:
            if v[i] >= 0:
                continue
            v[i] = v[idx] + cost
            if cost > maxi:
                if i == e:
                    return v[idx]
                q.append((i, cost))
            else:
                if i == e:
                    return v[i] - maxi
                q.append((i, maxi))

n, s, e = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))
print(bfs())






