'''
문제집

1번부터 N번까지 푼다.
1번이 젤 쉽고 N번이 젤 어려움.

먼저 풀면 좋은 문제가 있음.
1. N개의 문제 모두 풀어야 함.
2. 먼저 푸는 것이 좋은 문제가 있다면, 먼저 푸는것을 반드시 해야함.
3. 가능하면 쉬운 문제부터. (가능하면 오름차순으로.)

입력
1이상 32000이하 N, 1이상 10만이하 M 간선
A B A를 B보다 먼저 풀어야 함.
A B

출력
문제 번호를 애가 풀어야 하는 순서대로 적어라.
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 입력
g = [[] for _ in range(n+1)] # 그 노드 방문하면 풀리는 노드들 정보
reqq = [0] * (n+1) # 요구 간선
for _ in range(m): # m 반복
    a, b = map(int, input().split())
    reqq[b] += 1 # 요구 노드 갯수 추가
    g[a].append(b) # 출발노드에 도착노드 추가

q = [] # 보통 deque 쓰는데 정렬해야 하므로 list로 씀.
for i in range(1, n+1): # 요구 노드가 없다면 append
    if reqq[i] == 0:
        q.append(i)

while q:
    nq = q.pop(0) # popleft() 대신 pop(0)
    print(nq, end=' ')
    for i in g[nq]:
        reqq[i] -= 1
        if reqq[i] == 0:
            q.append(i)
            q.sort()
# 정렬해야되면 리스트로 덱을 쓰자.

'''
# 힙큐를 썻다.

import sys; input = sys.stdin.readline
import heapq
N, M = map(int, input().split())
ind = [0] * N
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1].append(B - 1)
    ind[B - 1] += 1
queue = []
for i in range(N):
    if not ind[i]:
        heapq.heappush(queue, i)
answer = [] # 정답 저장 할 리스트
while queue:
    i = heapq.heappop(queue)
    answer.append(i + 1)
    for j in graph[i]:
        ind[j] -= 1
        if not ind[j]:
            heapq.heappush(queue, j)
print(*answer)
'''


''' 리스트
q = []
for i in range(1, n+1):
    if reqq[i] == 0:
        q.append(i)

while q:
    nq = q.pop(0)
    print(nq, end=' ')
    for i in g[nq]:
        reqq[i] -= 1
        if reqq[i] == 0:
            q.append(i)
            q.sort()
'''
''' 덱
q = deque()
for i in range(1, n+1):
    if reqq[i] == 0:
        q.append(i)

while q:
    nq = q.popleft()
    print(nq, end=' ')
    for i in g[nq]:
        reqq[i] -= 1
        if reqq[i] == 0:
            if q and q[0] > i:
                q.appendleft(i)
            else:
                q.append(i)
                q = deque(sorted(q))
'''








