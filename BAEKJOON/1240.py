'''
노드 사이의 거리

N개 노드, m개 간선, 두 노드 사이 거리

입력
n, m  제시
n-1개 줄 간선 제시
m개 노드 쌍 제시

출력
m개 줄 제시된 노드 거리 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b):
    q = deque()
    q.append((a,0))
    v = [False] * (n+1)
    v[a] = True
    while q:
        nnod, d = q.popleft()
        if nnod == b: #찾는 노드와 번호가 일치하면 거리 리턴
            return d
        for i, l in g[nnod]: #연관된 노드에 대한 노드번호와 간선길이
            if not v[i]:
                v[i] = True
                q.append((i,d+l)) #지금까지 노드를 찾으면서 거리를 기록

n, m = map(int, input().rstrip().split())
g = [[] for _ in range(n+1)]
for _ in range(1, n):
    a, b, c = map(int, input().rstrip().split())
    g[a].append((b, c))
    g[b].append((a, c))
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    print(bfs(a, b))















