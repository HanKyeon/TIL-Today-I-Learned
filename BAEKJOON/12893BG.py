'''
적의 적

A와 적대인 B, B와 적대인 C. A과 C는 우호. C와 D가 적대 시 A와 D도 적대.

입력
사람 수 n, 적대 관계의 수 m
m개 줄에 걸쳐 적대 관계 사람 번호 A, B 제시.

출력
이론이 성립 할 수 있다면 1, 아니면 0 출력
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기. find해서 밖에서 먼저 확인해야한다.
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def lego():
    global n, enm
    for i in range(1, n+1):
        if not enm[i]:
            continue
        a = len(enm[i])
        if a == 1:
            if find(i) == find(enm[i][0]):
                return 0
        for j in range(a-1):
            for k in range(j+1, a):
                root = find(i)
                rj, rk = find(enm[i][j]), find(enm[i][k])
                if rj==root or rk==root:
                    return 0
                if rj==rk:continue
                union(rj, rk)
    return 1

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
enm = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    enm[a].append(b)
    enm[b].append(a)
print(lego())

'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    if x == y:
        return
    if x > y:
        parent[y] = x
    else:
        parent[x] = y

def check(x,y):
    return find(x) == find(y)

def eef(x,y):
    for i in enm[x]:
        union(y, i)
    for i in enm[y]:
        union(x, i)

n, m = map(int, input().rstrip().split())
ans = 1
parent = list(range(n+1))
enm = [[] for _ in range(n+1)] 
for _ in range(m):
    a, b = map(int, input().split())
    if check(a, b):
        ans = 0
        break
    enm[a].append(b)
    enm[b].append(a)
    eef(a, b)
print(ans)
'''


'''
# dfs로도 풀린다

import sys
input=sys.stdin.readline

def dfs():
    U=set(range(1,N+1))
    while U:
        stack=[U.pop()]
        friend=set(stack)
        enemy=set()
        while stack:
            current=stack.pop()
            if current in enemy:
                for e in E[current]:
                    if e in enemy:
                        return 0
                    if e in U:
                        U.discard(e)
                        stack.append(e)
                    friend.add(e)
            if current in friend:
                for e in E[current]:
                    if e in friend:
                        return 0
                    if e in U:
                        U.discard(e)
                        stack.append(e)
                    enemy.add(e)
    return 1
        

N,M=map(int,input().split())
E=[None]+[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)

print(dfs())
'''

'''

'
while 입력(n1,n2)이 끝날때까지
    if n1,n2의 부모가 같으면
        모순 -> 부모를 찾은 후에 같으면 동료인데 적이라 했으니까 모순
        break
    n1의 적에 n2 추가
    n2는 n1의 적에 대해서 동료가 됨(부모 동기화) 
    n2의 적에 n1 추가
    n1은 n2의 적에 대해서 동료가 됨(부모 동기화)
적 -> 부모가 다르다
동료 -> 부모가 같다

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    if x == y:
        return
    if x > y:
        parent[y] = x
    else:
        parent[x] = y

def check(x,y):
    return find(x) == find(y)

def eef(x,y):
    for i in enm[x]:
        union(y, i)
    for i in enm[y]:
        union(x, i)

n, m = map(int, input().rstrip().split())
ans = 1
parent = list(range(n+1))
enm = [[] for _ in range(n+1)] 
for _ in range(m):
    a, b = map(int, input().split())
    if check(a, b):
        ans = 0
        break
    enm[a].append(b)
    enm[b].append(a)
    eef(a, b)
print(ans)
'''




