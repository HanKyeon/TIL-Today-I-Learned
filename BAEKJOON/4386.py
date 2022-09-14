'''
별자리 만들기

도현이는 우주의 신이다. 별자리를 만들 것.
1. 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
2. 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져야 한다.
별들이 2차원 평면 위에 놓여있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리 만드는 최소 비용.

입력
별의 갯수n
x, y 좌표 제시. 최대 소수점 둘째자리. 좌표는 1000이하 양의 실수. (*100 할거니 10만과 같은듯)

출력
정답 출력. 절대/상대 오차는 0.01까지 허용.
'''
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
stl = []
for i in range(n):
    a, b = map(float, input().rstrip().split())
    a *= 100
    b *= 100
    stl.append((a, b))
g = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        ih, iw = stl[i]
        jh, jw = stl[j]
        itoj = ((((ih-jh)**2) + ((jw-iw)**2)) ** (0.5))
        g[i].append((itoj, j))
        g[j].append((itoj, i))

ans = int(10e9)
for i in range(n): # 모든 노드를 시작점으로 하는 최소 거리를 찾아봄. 근데 이게 맞는 방법은 아닌듯?
    heap = [(0, i)]
    dp = [0] * n
    vst = [0] * n
    cnt = 0
    while heap:
        if cnt == n:
            break
        c, idx = heappop(heap)
        if not vst[idx]:
            vst[idx] = 1
            dp[idx] = c
            cnt +=1
            for i in g[idx]:
                heappush(heap, i)
    ans = min(sum(dp), ans)

print(ans*0.01)


'''
# 프림 알고리즘인가 뭔가 그거 같음.
def prim(s, n, distance):
    visited = [0 for _ in range(n)]
    cost = [float('inf') for _ in range(n)]
    cost[s] = 0

    for _ in range(n):
        minidx, minval = 0, float('inf')
        for j in range(n):
            if not visited[j] and cost[j] < minval:
                minidx = j
                minval = cost[j]
        visited[minidx] = 1

        for j in range(n):
            if visited[j] or j == minidx:
                continue
            cost[j] = min(cost[j], distance[minidx][j])

    return sum(cost)

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
distance = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        d = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** (1/2)
        distance[i][j] = d
        distance[j][i] = d

print(prim(0, n, distance))
'''













