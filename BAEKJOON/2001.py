'''
보석 줍기

n개의 섬이 m개 다리 연결. 서로 다른 두 섬은 최대 한 개의 다리로만 연결.
각 다리는 견딜 수 있는 무게가 다름.
섬들 중, K개의 서로 다른 섬에 보석이 존재. 1번 섬에서 빈 손으로 출발. 많이 주워서 1번으로 돌아옴. 다리 안무너지게. 다리 섬 여러번 ㅆㄱㄴ 섬 지날 때 보석 안주워도 됨.

입력
n, m, k 제시. 1~100, 1~1000, 1~14
k개 줄 보석 있는 섬 정보
m개 줄 다리 정보 a,b,c 제시. a, b 연결 최대 무게 c
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
parseIsl = {}
v = [[0 for _ in range(1<<k)] for _ in range(n+1)]
for i in range(k):
    parseIsl[int(input())] = i
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((c, b))
    g[b].append((c, a))

q = deque([(1, 0, 0)])
v[1][0] = 1
ans = 0
while q:
    nod, cnt, bm = q.popleft()
    if nod == 1 and cnt > ans:
        ans = cnt
    for mc, nnod in g[nod]:
        if mc < cnt or v[nnod][bm]:
            continue
        v[nnod][bm] = 1
        q.append((nnod, cnt, bm))
    fla = parseIsl.get(nod, -1)
    if fla < 0:
        continue
    if bm & (1<<fla):
        continue
    fla2 = bm | (1<< fla)
    q.append((nod, cnt+1, fla2))
    v[nod][fla2] = 1

print(ans)


'''
# 진짜 빠른 코드

"""Solution code for "BOJ 2001. 보석 줍기".

- Problem link: https://www.acmicpc.net/problem/2001
- Solution link: http://www.teferi.net/ps/problems/boj/2001

Tags: [DisjointSet]

(This code was generated by Import Inliner v0.4)
"""

import collections
import sys

START = 0
INF = float('inf')


# >>>[BEGIN] teflib.disjointset.DisjointSet [v2.2] (Copied from teflib/disjointset.py)<<<  yapf:disable
class DisjointSet:
    """Disjoint Set for integers with path compression and union-by-size."""

    def __init__(self, size: int):
        self._parent = [-1] * size

    def union(self, x: int, y: int, *, raise_if_same: bool = False) -> int:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            if raise_if_same:
                raise ValueError(f'{x} and {y} are already in the same set.')
            return root_x
        if self._parent[root_x] > self._parent[root_y]:
            root_x, root_y = root_y, root_x
        self._parent[root_x] += self._parent[root_y]
        self._parent[root_y] = root_x
        return root_x

    def find(self, x: int) -> int:
        cur = x
        while (par := self._parent[cur]) >= 0:
            cur = par
        root, cur = cur, x
        while cur != root:
            self._parent[cur], cur = root, self._parent[cur]
        return root

    def size(self, x: int) -> int:
        return -self._parent[self.find(x)]
# >>>[END] teflib.disjointset.DisjointSet [v2.2]<<<  yapf:enable


def main():
    n, m, K = [int(x) for x in sys.stdin.readline().split()]
    jewel_nodes = [int(sys.stdin.readline()) for _ in range(K)]
    edges_by_cap = collections.defaultdict(list)
    for _ in range(m):
        a, b, c = [int(x) for x in sys.stdin.readline().split()]
        edges_by_cap[c].append((a - 1, b - 1))

    collect_limit = INF
    jewels = {x - 1 for x in jewel_nodes}
    total_collected_count = 1 if START in jewels else 0
    jewels.discard(START)
    dsu = DisjointSet(n)
    for cap, edges in sorted(edges_by_cap.items(), reverse=True):
        for u, v in edges:
            dsu.union(u, v)
        start_group = dsu.find(START)
        newly_found_jewels = {x for x in jewels if dsu.find(x) == start_group}
        jewels -= newly_found_jewels
        collect_limit = min(collect_limit, cap)
        newly_collected_count = min(collect_limit, len(newly_found_jewels))
        total_collected_count += newly_collected_count
        collect_limit -= newly_collected_count

    print(total_collected_count)


if __name__ == '__main__':
    main()
'''
'''
# 빠른 코드 2
# https://www.acmicpc.net/problem/2001
# 1 <= N <= 100
# 1 <= M <= 1,000
# 1 <= K <= 14
import sys
from queue import PriorityQueue

I = sys.stdin.readline


def bfs():
    pq = PriorityQueue()
    pq.put((-15, 1))
    visit = [-2] * (N+1)
    while not pq.empty():
        v, now = pq.get()
        if visit[now] != -2:
            continue
        visit[now]= -v
        for n in range(1,N+1):
            if visit[n] != -2:
                continue
            if adj[now][n] == -1:
                continue
            pq.put((max(v, -adj[now][n]), n))

    pq = PriorityQueue()
    for j in jewelry:
        pq.put(visit[j])
    count = 0
    while not pq.empty():
        v = pq.get()
        if v == -2:
            continue
        count = min(count+1, v)
    return count

N, M, K = map(int, I().split())
jewelry = [int(I().strip()) for _ in range(K)]
bridges = [list(map(int, I().strip().split())) for _ in range(M)]
adj = [[-1] * (N+1) for _ in range(N+1)]
for a, b, c in bridges:
    adj[a][b] = c
    adj[b][a] = c
print(bfs())
'''
'''
# 빠른 코드 3
# https://www.acmicpc.net/problem/2001

import sys
from itertools import chain
from collections import deque

readline = lambda: sys.stdin.readline().rstrip()  # noqa

V, E, J = map(int, readline().split())
jpoints = [int(readline()) - 1 for _ in range(J)]

tols = [[0] * V for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, readline().split())
    u, v = u - 1, v - 1
    tols[u][v] = w
    tols[v][u] = w

for k in range(V):
    for u in range(V):
        for v in range(V):
            if tols[u][v] < min(tols[u][k], tols[k][v]):
                tols[u][v] = min(tols[u][k], tols[k][v])

max_jewels = 0
waypoints = deque([(0, 0, 0)])  # 현재 섬, 보석 개수, 보석 비트마스크
visited = [[False] * V for _ in range(2**J)]
while 0 < len(waypoints):
    u, j, jmask = waypoints.popleft()
    max_jewels = max(max_jewels, j) if u == 0 else max_jewels

    for jindex, v in enumerate(jpoints):
        if u == v:
            if (jmask & (1 << jindex)) == 0:
                visited[jmask | (1 << jindex)][v] = True
                waypoints.append((u, j + 1, jmask | (1 << jindex)))
            break

    for v in chain(jpoints, [0]):
        if j <= tols[u][v] and not visited[jmask][v]:
            visited[jmask][v] = True
            waypoints.append((v, j, jmask))

print(max_jewels)
'''




