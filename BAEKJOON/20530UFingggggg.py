'''
양분

나무 T는 양분을 먹고 자란다.
정점 N과 N-1로 구성되어야 하지만 N개의 간선을 가지게 되었다.

N개 정점과 N개의 간선으로 이루어진 연결 그래프 T가 주어진다.
정점은 1번부터 N번까지 번호가 매겨져 있고, 간선도 1번부터 N번까지 번호가 매겨져 있다. 아래 쿼리를 수행하라.
쿼리
u v : u번 정점에서 v번 정점으로 가는 단순 경로의 수 출력

입력
N, Q 제시. 간선 갯수 N, 쿼리 갯수 Q
N개 줄 a, b 제시 간선.
Q개 줄 쿼리 제시.
'''
'''
간선 정보를 입력한 뒤 어느 한 지점에서 dfs해서 사이클을 찾는다.
사이클의 부모는 사이클에서 가장 작은 수로.
나머지 union 할 때 root가 사이클이라면 continue 하는걸로.

아래처럼 구성이 된다.
트리 - 사이클 - 트리
같은 트리 내 -> 1회
다른 트리-> 다른 트리 -> 2회
사이클을 set()로 만들어주고
사이클의 숫자 중에 있다면 
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # union 해서.
    if x in cyc:
        parent[y] = x
        return
    elif y in cyc:
        parent[x] = y
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def dfs(idx): # 사이클 찾는 dfs 함수
    if not g[idx]:
        stk.pop()
        return False
    for i in g[idx]:
        if v[i]:
            ret = {i}
            while stk[-1] != i:
                num = stk.pop()
                ret.add(num)
            return ret
        v[i] = 1
        g[i].remove(idx)
        stk.append(i)
        a = dfs(i)
        if a:
            return a
    return False

n, qst = map(int, input().rstrip().split())
parent = list(range(n+1))
g = [set() for _ in range(n+1)]
egs = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    g[a].add(b)
    g[b].add(a)
    egs.append((a, b))

stk = [1]
v = [0]*(n+1)
v[1] = 1
cyc = dfs(1)

for a, b in egs:
    if a in cyc and b in cyc:
        continue
    ra, rb = find(a), find(b)
    union(ra, rb)

for _ in range(qst):
    a, b = map(int, input().rstrip().split())
    if find(a) == find(b):
        print(1)
    else:
        print(2)
print(parent)



'''
7 6
1 2
2 3
3 4
4 5
5 6
6 7
1 3
1 2
1 3
1 4
3 4
4 5
6 7
'''

'''
import sys

# 재귀깊이해제
sys.setrecursionlimit(300000)

# go : 현재 정점이 now고 사이클의 끝점이 base일 때 사이클 내부의 정점을 검출하는 함수
def go(now, base):
    while now != base:
        is_cycle[now] = True
        now = parent[now]
    is_cycle[base] = True

# dfs : 현재 정점이 now이고 이전 정점이 prev일 때, 사이클의 여부를 리턴하는 함수
def dfs(now, prev):
    # 방문 표시
    check[now] = True
    for i in adj[now]:
        if i == prev:
            continue
        if not check[i]:
            # 방문하지 않은 정점이라면 현재 정점이 부모 정점이 된다
            parent[i] = now
            # 사이클이 검출되면 계속 True를 리턴
            res = dfs(i, now)
            if res:
                return res
        # 현재 정점이 사이클의 끝점이라면 go 함수 호출 후 사이클 검출의 의미로 True 리턴
        elif not fin[i]:
            go(now, i)
            return True
    # 현재 정점 종료 표시
    fin[now] = True
    return False

# get_tree_num : 현재 정점이 now고 이전 정점이 prev일 때 트리 번호를 채우는 함수
def get_tree_num(now, prev):
    tr_num[now] = num
    for i in adj[now]:
        if i == prev:
            continue
        if is_cycle[i]:
            continue
        if tr_num[i] == -1:
            get_tree_num(i, now)

# 입력부
n, q = map(int, sys.stdin.readline().split())

# 인접 리스트
adj = [[] for _ in range(n + 1)]
# is_cycle : 현재 정점이 사이클인지 아닌지 저장하는 리스트
is_cycle = [False] * (n + 1)
# check : 현재 정점을 방문했는지 아닌지 저장하는 리스트
check = [False] * (n + 1)
# fin : 현재 정점의 방문이 끝났는지 아닌지 저장하는 리스트
fin = [False] * (n + 1)
# parent : 현재 정점의 부모 정점을 저장하는 리스트
parent = [-1] * (n + 1)

for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

# 사이클 검출
dfs(1, -1)

# tr_num : 현재 정점의 트리 번호를 저장하는 리스트
tr_num = [-1] * (n + 1)
# num : 현재 트리 번호
num = 0
for i in range(1, n + 1):
    # 사이클 내부의 각 정점에 대해 트리 번호를 채움
    if is_cycle[i]:
        no_cycle(i, -1)
        num += 1

# 트리 번호가 같으면 1, 아니면 2 출력
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    if tr_num[a] == tr_num[b]:
        print(1)
    else:
        print(2)
'''


import sys
input=sys.stdin.readline
sys.setrecursionlimit(300000)

def go(now, base):
    while now != base:
        is_cycle[now] = True
        now = parent[now]
    is_cycle[base] = True

def dfs(now, prev):

    check[now] = True
    for i in adj[now]:
        if i == prev:
            continue
        if not check[i]:
            parent[i] = now
            res = dfs(i, now)
            if res:
                return res
        elif not fin[i]:
            go(now, i)
            return True
    fin[now] = True
    return False

def get_tree_num(now, prev):
    tr_num[now] = num
    for i in adj[now]:
        if i == prev:
            continue
        if is_cycle[i]:
            continue
        if tr_num[i] == -1:
            get_tree_num(i, now)

n, q = map(int, input().rstrip().split())

adj = [[] for _ in range(n + 1)]
is_cycle = [False] * (n + 1)
check = [False] * (n + 1)
fin = [False] * (n + 1)
parent = [-1] * (n + 1)

for i in range(1, n + 1):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1, -1)

tr_num = [-1] * (n + 1)
num = 0
for i in range(1, n + 1):
    if is_cycle[i]:
        no_cycle(i, -1)
        num += 1

for _ in range(q):
    a, b = map(int, input().rstrip().split())
    if tr_num[a] == tr_num[b]:
        print(1)
    else:
        print(2)







