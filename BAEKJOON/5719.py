'''
거의 최단 경로

최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은 것의 길이 출력
0부터 n-1까지 번호, 노드에서 노드로 가는 도로는 최대 1개이다.

입력
노드n 도로m
시작노드s, 도착노드e 제시
m개 줄 a, b, c 제시
입력의 마지막에는 0 0 제시

출력
거의 최단 경로 길이 출력. 없다면 -1 출력
'''
import sys
from heapq import heappush, heappop
from collections import deque
inf = sys.maxsize

def dij(s, e):
    global n
    dst[s] = 0
    heap = [(0, s)]
    while heap:
        cost, nod = heappop(heap)
        if dst[nod] < cost: continue
        if nod == e: return dst[e]
        for co, nnod in g1[nod]:
            if g3[nod][nnod] and cost+co < dst[nnod]:
                dst[nnod] = cost+co
                heappush(heap, (cost+co, nnod))
    return dst[e]

def bfs(s, e):
    global n
    q = deque([e])
    while q:
        nod = q.popleft()
        if nod == s: continue
        for co, nnod in g2[nod]:
            if dst[nnod]+co == dst[nod] and g3[nnod][nod]:
                g3[nnod][nod] = 0
                q.append(nnod)

while True:
    n, m = map(int, input().rstrip().split())
    if not n and not m: break
    s, e = map(int, input().rstrip().split())
    g1, g2, g3 = [[] for _ in range(n)], [[] for _ in range(n)], [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        g1[a].append((c, b))
        g2[b].append((c, a))
        g3[a][b] = 1
    dst = [inf]*n
    if dij(s, e) == inf: print(-1); continue
    bfs(s, e)
    dst = [inf]*n
    print(-1 if dij(s, e) == inf else dst[e])

'''
import sys, io, os, collections
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from heapq import heappop, heappush
INF = 1234567891

def dij(G, s):
  n = len(G)
  D, P = [INF] * n, [set() for _ in range(n)]
  D[s] = 0

  Q = [(0, s)]
  while Q:
    pl, v = heappop(Q)
    if pl != D[v]: continue
    for w, el in G[v]:
      if el + pl < D[w]:
        D[w] = el + pl
        P[w] = set([v]) #최단거리가 갱신될때마다 부모 노드 번호도 갱신한다. 
        heappush(Q, (el + pl, w))
      elif el + pl == D[w] :
        P[w].add(v)

  return D, P

def sol() :
  N, M = map(int, input().split())
  if N == M == 0 : raise StopIteration
  S, D = map(int, input().split())
  G = [[] for _ in range(N)]
  for _ in range(M) :
    u, v, w = map(int, input().split())
    G[u].append((v, w))
  dist, P = dij(G, S)
  first = dist[D]
  if first == INF : #해당 경로로 가는 경로가 없으면 불가능
    sys.stdout.write('-1\n')
    return
  
  while True :
    vis = [False] * N
    vis[D] = True
    Q = collections.deque([D])
    while Q :
      v = Q.popleft()
      for u in P[v] : #u에서 도착점이 D인 것을 전부 지운다
        for i, (p, _) in enumerate(G[u]) :
          if p != v : continue
          if not vis[u] : 
            Q.append(u)
            vis[u] = True
          del G[u][i]
          break
  
    dist, P = dij(G, S)
    if dist[D] != first: break
  sys.stdout.write(str(-1 if dist[D] == INF else dist[D]) + '\n')
  
while True :
  try :
    sol()
  except StopIteration :
    break
  except :
    raise
'''
'''
import sys; input = sys.stdin.readline
from math import inf
from heapq import heappop, heappush

def solve(N, M):
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    reverse_graph = [[] for _ in range(N)]
    for i in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((V, P, i))
        reverse_graph[V].append((U, P, i))

    queue = [[0, S]]
    distance = [inf] * N
    distance[S] = 0
    while queue:
        d, u = heappop(queue)
        if distance[u] < d:
            continue
        for v, p, i in graph[u]:
            if distance[v] > d + p:
                distance[v] = d + p
                heappush(queue, [distance[v], v])

    use = [False] * M
    queue = [D]
    while queue:
        v = queue.pop()
        for u, p, i in reverse_graph[v]:
            if not use[i] and distance[v] == distance[u] + p:
                use[i] = True
                queue.append(u)

    queue = [[0, S]]
    distance = [inf] * N
    distance[S] = 0
    while queue:
        d, u = heappop(queue)
        if distance[u] < d:
            continue
        for v, p, i in graph[u]:
            if not use[i] and distance[v] > d + p:
                distance[v] = d + p
                heappush(queue, [distance[v], v])

    print(distance[D]) if distance[D] < inf else print(-1)

while True:
    N, M = map(int, input().split())
    if not N:
        break
    solve(N, M)
'''
'''
import sys
from collections import deque

def dijkstra():
    q = deque()
    q.append([s, 0])
    while q:
        cur_node, cur_cost = q.popleft()
        if cur_node == d: continue
        for each in adj[cur_node]:
            next_node, next_cost = each, adj[cur_node][each]
            new_cost = cur_cost + next_cost
            if new_cost > distance[next_node]: continue
            if new_cost == distance[next_node]:
                edge[next_node].append(cur_node)
            else:
                edge[next_node] = [cur_node]
                distance[next_node] = new_cost
                q.append([next_node, new_cost])

def delete():
    q = deque()
    for each in edge[d]:
        q.append([d, each])
    while q:
        cur_node, ex_node = q.popleft()
        if cur_node == s: break
        adj[ex_node][cur_node] = sys.maxsize
        while edge[ex_node]:
            q.append([ex_node, edge[ex_node].pop()])

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0: break
    s, d = map(int, sys.stdin.readline().split())
    adj = [dict() for _ in range(n)]
    distance = [sys.maxsize for i in range(n)]; distance[s] = 0
    edge = [[] for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        adj[u][v] = p
    dijkstra()
    delete()
    distance = [sys.maxsize for i in range(n)]
    dijkstra()
    print(distance[d] if distance[d] != sys.maxsize else -1)
'''
'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class SecondBest():
    def __init__(self, N, M):
        S, D = map(int, input().split())
        graph = [[] for _ in range(N)]
        for _ in range(M):
            U, V, P = map(int, input().split())
            graph[U].append((P, V))
        memo = [[] for _ in range(N)]

        dist = [sys.maxsize] * N
        dist[S] = 0
        pq = [(0, S)]
        while pq:
            pd, pn = heappop(pq)
            if dist[pn] < pd:
                continue
            for cd, cn in graph[pn]:
                if pd+cd < dist[cn]:
                    dist[cn] = pd+cd
                    heappush(pq, (pd+cd, cn))
                    memo[cn] = [pn]
                elif pd+cd == dist[cn]:
                    memo[cn].append(pn)

        exclude = [set() for _ in range(N)]
        stack = [(D, memo[D])]
        while stack:
            cn, pns = stack.pop()
            for pn in pns:
                if cn in exclude[pn]:
                    continue
                exclude[pn].add(cn)
                stack.append((pn, memo[pn]))

        dist = [sys.maxsize] * N
        dist[S] = 0
        pq = [(0, S)]
        while pq:
            pd, pn = heappop(pq)
            if dist[pn] < pd:
                continue
            for cd, cn in graph[pn]:
                if cn in exclude[pn]:
                    continue
                if pd+cd < dist[cn]:
                    dist[cn] = pd+cd
                    heappush(pq, (pd+cd, cn))

        self.answer = -1 if dist[D] == sys.maxsize else dist[D]
        

if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        tc = SecondBest(N, M)
        print(tc.answer)

'''




