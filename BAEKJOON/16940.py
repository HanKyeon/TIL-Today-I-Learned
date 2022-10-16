'''
BFS 스페셜 저지

노드 갯수 N, 1부터 N까지 양방향 그래프.
1. 큐에 시작 정점 1을 넣는다. 방문처리
2. 큐가 비어있지 않은 동안 다음 반복
BFS 순서느 중요치 않으나 답이 여러개 나온다. 올바른 BFS인지 확인해라.

입력
정점 갯수 n 제시
n-1개 간선 정보 제시.
bfs 순서 제시.

출력
올바른 순서면 1, 아니면 0 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

def check():
    sta = bfsq.popleft()
    if sta != 1:
        return 0
    q = deque()
    q.append(sta)
    v[sta] = 1
    while q:
        num = q.popleft()
        while g[num]:
            a = bfsq.popleft()
            if a in g[num] and not v[a]:
                v[a] = 1
                g[num].remove(a)
                g[a].remove(num)
                q.append(a)
            else:
                return 0
    return 1

n = int(input())
g = [set() for _ in range(n+1)]
v = [0]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    g[a].add(b)
    g[b].add(a)
bfsq = deque(list(map(int, input().rstrip().split())))
print(check())





'''

def bfs():
    q = deque()
    q.append((0, 1))
    v[1] = 1
    while q:
        sta, num = q.popleft()
        for i in g[num]:
            if not v[i]:
                v[i] = v[sta]+1
                q.append((num, i))

def check():
    val = v[bfsq.popleft()]
    while bfsq:
        a = v[bfsq.popleft()]
        if val == a:
            continue
        elif val + 1 == a:
            val = a
            continue
        else:
            return 0
    return 1
'''




