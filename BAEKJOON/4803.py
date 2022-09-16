'''
트리

그래프는 정점과 간선으로 이루어져 있다. 두 정점 사이에 간선이 있다면 연결된 것이다.
연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합ㄴ디ㅏ. 그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.
트리는 사이클이 없는 연결 요소이다.
그래프가 주어졌을 때, 트리의 갯수를 세라.

입력
n, m 제시. n은 500이하 노드 갯수, m은 1부터 n까지 연속합 이하 간선의 갯수
간선 두 정수 제시. 같은 간선 제시x
정점은 1번부터 n번까지 번호가 있다.
입력 마지막 줄에는 0이 두 개 제시.

출력
입력으로 주어진 그래프에 트리가 없다면 'No trees'를, 한개라면 'There is one tree.' 를, 2개 이상이라면 'A forest of {T} trees'를 테케 번호와 함께 출력.

'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a == b:
        return
    if a < b:
        parent[b] = a
        edgc[a] += edgc[b]
        nodc[a] += nodc[b]
    else:
        parent[a] = b
        edgc[b] += edgc[a]
        nodc[b] += nodc[a]

testcase = 0
while True:
    testcase += 1
    n, m = map(int, input().rstrip().split())
    if not n and not m: # 0, 0이면 종료
        break
    parent = list(range(n+1)) # 부모
    edgc = [0]*(n+1) # 간선 갯수
    nodc = [1]*(n+1) # 노드 갯수 (자손 갯수)
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        union(a, b)
        edgc[find(a)] += 1
    
    ans = 0
    for i in range(1, n+1):
        if i != parent[i]:
            continue
        if edgc[i] == nodc[i]-1:
            ans += 1

    if ans == 1:
        ans = 'There is one tree.'
        print(f"Case {testcase}: {ans}")
    elif ans > 1:
        print(f"Case {testcase}: A forest of {ans} trees.")
    else:
        print(f"Case {testcase}: No trees.")

'''
# 빠른 코드. DFS인듯?

import sys
input = sys.stdin.readline

def dfs(prev, node):
    visited[node] = True
    for n in graph[node]:
        if n == prev: # 다음 노드가 이전 노드와 같다면 DFS 수행 X
            continue
        if visited[n]: # 다음노드 != 이전 노드, 이미 방문했다면 사이클이 생긴 것, 즉 트리가 아님
            return False
        if not dfs(node, n): # 다음 노드 != 이전 노드, 첫 방문, DFS 수행, 수행 도중 사이클이 생긴 경우 False
            return False
    return True # DFS 수행 도중 사이클이 생기지 않으면 True

test_case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)] 
    visited = [False] * (n+1) # 방문 여부
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b) 
        graph[b].append(a)

    tree_cnt = 0 # 트리의 개수
    for v in range(1, n+1):
        if not visited[v]: # 방문하지 않은 경우만 DFS 수행
            if dfs(0, v):
                tree_cnt += 1 # 사이클이 없는 경우 트리 개수 증가
    if tree_cnt == 0:
        print(f'Case {test_case}: No trees.')
    elif tree_cnt == 1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {tree_cnt} trees.')
    test_case += 1
'''
















