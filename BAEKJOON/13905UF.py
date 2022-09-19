'''
세부

집과 집을 연결하는 오크나무다리.
최대한의 금 빼빼로를 들고 가려고 한다. 무게 제한이 가장 작은 다리 중 가장 큰 거

입력
집의 수 n 2이상 10만이하, 다리 수 m 1이상 30만이하.
출발위치 s 도착위치 e 제시.
다리 정보.
집번호h1 집번호h2 무게제한k

출력
시작 위치에서 도착 위치까지 들고 갈 수 있는 최대 갯수.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기.
    if x < y:
        parent[y] = x
        count[x] = max(count[x], count[y])
    else:
        parent[x] = y
        count[y] = max(count[x], count[y])

n, m = map(int, input().rstrip().split())
s, e = map(int, input().rstrip().split())
s, e = min(s, e), max(s, e) # 도착지가 더 크게.
parent = list(range(n+1))
count = [int(-10e9)]*(n+1)
g = []
for _ in range(m):
    h1, h2, k = map(int, input().rstrip().split())
    g.append((-k, h1, h2))
g.sort()
for i in g:
    if find(s) == find(e):
        break
    k, h1, h2 = i
    a, b = find(h1), find(h2)
    if a == b:
        continue
    count[a], count[b] = max(count[a], k), max(count[b], k)
    union(a, b)

ans = -count[find(s)]
if find(s) != find(e):
    ans = 0

print(ans)




'''
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
start, end = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, weight = map(int, input().split())
    arr[a].append((weight, b))
    arr[b].append((weight, a))
visited = [0] * (N+1)


def dijkstra():
    q = []
    heapq.heappush(q, (-sys.maxsize, start))
    visited[start] = sys.maxsize
    while q:
        cost, node = heapq.heappop(q)
        cost = -cost
        if visited[node] > cost:
            continue
        for ncost, nnode in arr[node]:
            temp = min(cost, ncost)
            if visited[nnode] < temp:
                visited[nnode] = temp
                heapq.heappush(q, (-temp, nnode))


dijkstra()
print(visited[end])
'''















