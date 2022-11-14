'''
환승

아주 먼 미래에 사람들이 많이 쓰는 대중교통 하이퍼 튜브. 하나는 역 k개를 서로 연결.
1번에서 n번으로 가는데 방문하는 최소 역의 갯수는?

입력
역의 수 n, 연결 역 갯수 k, 튜브 갯수 m 제시. n은 1이상10만이하 k,m은 1이상 1000이하.
다음 m개 줄 하이퍼 튜브 정보 제시. k개의 숫자, 그 하이퍼 튜브가 서로 연결하는 역의 갯수.

출력
1번역에서 n번 역으로 가는데 방문하는 역의 갯수 최솟값. 갈 수 없다면 -1 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global n
    if n==1:
        return 1
    q = deque()
    v = [0]*(n+1)
    v[1] = 1
    q.append(1)
    while q:
        idx = q.popleft()
        for i in g[idx]:
            for j in ht[i]:
                if v[j]:
                    continue
                if j == n:
                    return v[idx]+1
                v[j] = v[idx]+1
                q.append(j)
    return -1

n, k, m = map(int, input().rstrip().split())
ht = []
g = [[] for _ in range(n+1)]
for i in range(m):
    nl = list(map(int, input().rstrip().split()))
    ht.append(nl)
    for j in nl:
        g[j].append(i)
print(bfs())

'''
# 빠른 코드

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(m)]
d = defaultdict(list)
for i in range(m):
    for station in data[i]:
        d[station].append(i)

def bfs(start):
    queue = deque()
    queue.append((start, 1))
    visited = [0] * (n + 1)
    tvisited = [0] * m
    visited[start] = 1

    while queue:
        now, dist = queue.popleft()

        if now == n: 
            return dist
        
        for i in d[now]:
            if tvisited[i]: continue
            tvisited[i] = 1
            for j in data[i]:

                if visited[j]: continue

                visited[j] = 1
                queue.append((j, dist + 1))
    
    return 0

result = bfs(1)
print(result if result else -1)
'''







'''
# 당당한 메모리 초과
def bfs():
    global n
    q = deque()
    v = [0]*(n+1)
    v[1] = 1
    q.append(1)
    while q:
        idx = q.popleft()
        for i in g[idx]:
            if v[i]:
                continue
            if i == n:
                return v[idx]+1
            v[i] = v[idx]+1
            q.append(i)
    return -1

n, k, m = map(int, input().rstrip().split())
g = [set() for _ in range(n+1)]
for _ in range(m):
    nl = list(map(int, input().rstrip().split()))
    for sta, end in combinations(nl, 2):
        g[sta].add(end)
        g[end].add(sta)
print(bfs())
'''