'''
이분 그래프

그래프의 정점의 집합을 둘로 분할하여 각 집합에 속한 정점 끼리는 서로 인접하지 않도록 분할 할 수 있을 때, 이분 그래프라 부른다.
그래프 제시, 이분 그래프 판별.

입력
테케 갯수
노드갯수n, 간선 갯수m 1부터 n번.
m개 줄 간선 정보

출력
YES or NO
'''
import sys
from collections import deque
input=sys.stdin.readline

def bfs(idx):
    global n
    v[idx] = 1
    q = deque([(idx, 1)])
    while q:
        num, fla = q.popleft()
        for i in g[num]:
            nfla = 0 if fla else 1
            if v[i] < 0:
                v[i] = nfla
                q.append((i, nfla))
            elif v[i] != nfla:
                return True
    return False

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        g[a].append(b)
        g[b].append(a)
    ans = False
    v = [-1]*(n+1)
    for i in range(1, n): # 마지막이 방문 안된거면 걍 패스해도 됨
        if v[i] < 0:
            ans = bfs(i)
            if ans: break
    print("NO" if ans else "YES")









