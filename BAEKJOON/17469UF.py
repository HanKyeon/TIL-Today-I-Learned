'''
트리의 색깔과 쿼리

N개의 정점으로 구성된 트리. 1번부터 n까지 정점 번호. 1이상 10만이하 자연수로 표현되는 색 보유.
루트는 1번, 트리이기에 임의의 서로 다른 두 점을 잇는 경로는 반드시 한 개 존재.
정점 u, v를 잇는 경로가 존재하면 u에서 v로 이동 가능.

두가지 쿼리 처리해야한다.
1 a : 정점 a와 a의 부모 정점을 연결하는 간선 제거. 간선이 존재하는 경우만 제시.
2 a : 정점 a에서 갈 수 있는 정점들만 보았을 때, 색깔의 종류 갯수 출력.

입력
정점의 갯수, 쿼리의 갯수 n, q 10만이상 100만이하
간선 n-1개 제시. i번째 줄에 i+1 정점의 부모 정점 제시.
정점의 색깔 n개 제시. i번째 줄에 정점 i의 색깔 숫자로 제시.
n+q-1개에 쿼리 제시. 간선 제거는 n-1개, 쿼리는 q개.
쿼리는 한 줄에 하나씩 쿼리 종류 x 쿼리에서 처리 할 정점 번호 a 제시.

출력
Q개의 쿼리에 대한 답 출력.
'''
'''
모든 edges를 뺀다는 것을 고려하지 못했었다. 멍청이.....
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(110000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    # 시간을 줄이기 위해 더 짧은 것을 부모로 설정.
    if len(clrz[x]) <= len(clrz[y]):
        parent[x] = y
        for i in clrz[x]:
            clrz[y].add(i)
        clrz[x] = set()
    else:
        parent[y] = x
        for i in clrz[y]:
            clrz[x].add(i)
        clrz[y] = set()

n, q = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]
prt = [0] * (n+1)
clrz = [set() for _ in range(n+1)]
for i in range(2, n+1):
    prt[i] = int(input())
for i in range(1, n+1):
    clrz[i].add(int(input()))

stk = [list(map(int, input().rstrip().split())) for _ in range(n+q-1)]
ans = []
while stk:
    a, b = stk.pop()
    if a == 1:
        union(b, prt[b])
    else:
        ans.append(len(clrz[find(b)]))

while ans:
    print(ans.pop())





'''
# 시간초과 6%

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
        clrz[x].update(clrz[y])
        del clrz[y]
    else:
        parent[x] = y
        clrz[y].update(clrz[x])
        del clrz[x]

n, q = map(int, input().rstrip().split())
parent = list(range(n+1))
# val = [0]*(n+1)
clrz = {}
egs = {}
for i in range(2, n+1):
    egs[i] = int(input())
for i in range(1, n+1):
    clrz[i] = {int(input())}

stk = []
for i in range(n+q-1):
    ysz, nod = map(int, input().rstrip().split())
    if ysz == 1:
        stk.append((1, nod, egs[nod]))
        del egs[nod]
    else:
        stk.append((0, nod))

for i in egs.keys():
    x, y = find(i), find(egs[i])
    if x == y:
        del egs[i]
        continue
    union(x, y)
    del egs[i]

ans = []
while stk:
    info = stk.pop()
    if info[0]:
        ysz, nod1, nod2 = info
        nod1, nod2 = find(nod1), find(nod2)
        union(nod1, nod2)
    else:
        ysz, nod1 = info
        nod1 = find(nod1)
        ans.append(len(clrz[nod1]))

while ans:
    print(ans.pop())
'''






'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
        clrz[x] = clrz[y]|clrz[x]
        del clrz[y]
    else:
        parent[x] = y
        clrz[y] = clrz[y]|clrz[x]
        #  clrz[y].update(clrz[x])
        del clrz[x]

n, q = map(int, input().rstrip().split())
parent = list(range(n+1))
# val = [0]*(n+1)
clrz = {}
egs = {}
for i in range(2, n+1):
    egs[i] = int(input())
for i in range(1, n+1):
    clrz[i] = {int(input())}

stk = []
for i in range(n+q-1):
    ysz, nod = map(int, input().rstrip().split())
    if ysz == 1:
        stk.append((1, nod, egs[nod]))
        del egs[nod]
    else:
        stk.append((0, nod))

for i in egs.keys():
    x, y = find(i), find(egs[i])
    if x == y:
        del egs[i]
        continue
    union(x, y)
    del egs[i]

ans = []
while stk:
    info = stk.pop()
    if info[0]:
        ysz, nod1, nod2 = info
        nod1, nod2 = find(nod1), find(nod2)
        union(nod1, nod2)
    else:
        ysz, nod1 = info
        nod1 = find(nod1)
        ans.append(len(clrz[nod1]))

while ans:
    print(ans.pop())
'''





