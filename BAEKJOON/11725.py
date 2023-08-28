'''
트리의 부모 찾기

루트 없는 트리 제시. 루트를 1이라 정했을 때, 각 노드의 부모를 구해라.

입력
노드 갯수 n 제시
n-1개 줄 연결된 두 정점 제시

출력
n-1개 줄 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g, v = [[] for _ in range(n)], [-1]*n
for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().rstrip().split())
    g[a].append(b)
    g[b].append(a)

q = deque([0])
while q:
    num = q.popleft()
    for i in g[num]:
        if v[i] >= 0: continue
        v[i] = num+1
        q.append(i)
for i in range(1, n):
    print(v[i])



