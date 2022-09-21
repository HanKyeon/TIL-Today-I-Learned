'''
트리

트리와 에지.
정점 v와 w를 연결하는 경로가 존재하는가? 의 질문에 답해야 한다.
트리 정보 제시, 에지 제거 정보와 질의가 임의의 순서로 주어질 때, 작업을 순서대로 수행하며 질의에 대한 답을 출력하는 프로그램을 작성하시오.
루트는 항상 1

입력
트리 정점 갯수와 질의 갯수 n, q 1이상 20만이하.

n-1개 전체 간선 정보 제시. i번째 줄에는 정점 i+1의 부모 정점을 나타내는 정수 a 제시.

다음 n-1+q개 줄 중에서 n-1개는 두가지 형태로 제시.
1. 두 정수 0와 b 제시. b와 b의 부모 정점 에지 제거. 각 줄의 b는 모두 다르다.
2. 세 정수 1, c, d. c와 d를 연결하는 경로가 존재하는지?

출력
질문에 대한 답을 순서대로 q개 줄에 출력. 경로가 존재하면 YES 없으면 NO
'''
'''
저번처럼 반대 순서로 하면 되지 않을까?
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
egs = {}
for i in range(2, n+1):
    egs[i] = int(input())

stk = []

for i in range(0, n-1+m):
    s = list(map(int, input().rstrip().split()))
    if s[0]:
        ysz, a, b = s
        stk.append((a, b, ysz))
    else:
        ysz, a = s
        stk.append((a, egs[a], ysz))
        del egs[a]

for i in egs.keys():
    x, y = find(i), find(egs[i])
    union(x, y)

ans = []
while stk:
    info = stk.pop()
    nod1, nod2, ysz = info
    nod1, nod2 = find(nod1), find(nod2)
    if ysz:
        if nod1 == nod2:
            ans.append('YES')
        else:
            ans.append('NO')
    else:
        union(nod1, nod2)

while ans:
    print(ans.pop())


'''
# 런타임?

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
egs = {}
for i in range(2, n+1):
    egs[i] = int(input())
stk = []
for i in range(n-1+m):
    s = list(map(int, input().rstrip().split()))
    if len(s) == 2:
        _, a = s
        stk.append((a, egs[a], 0))
        del egs[a]
    else:
        _, a, b = s
        stk.append((a, b, 1))

for i in egs.keys():
    x, y = find(i), find(egs[i])
    union(x, y)

ans = []
while stk:
    nod1, nod2, ysz = stk.pop()
    if ysz:
        nod1, nod2 = find(nod1), find(nod2)
        if nod1 == nod2:
            ans.append('YES')
        else:
            ans.append('NO')
    else:
        nod1, nod2 = find(nod1), find(nod2)
        union(nod1, nod2)
        continue

while ans:
    print(ans.pop())
'''

'''
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write

n, q = map(int, input().split())
d = {}
for i in range(n - 1):
    d.update({i + 2: int(input())})
queries = [list(map(int, input().split())) for _ in range(q + n - 1)]

parent = list(range(n + 1))

def find(v):
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    if a > b:
        a, b = b, a
    parent[b] = a
        
result = []
for i in range(q + n - 2, -1, -1):
    query = queries[i]
    if query[0] == 1:
        if find(query[1]) == find(query[2]):
            result.append('YES')
        else:
            result.append('NO')
    else:
        union(find(query[1]), find(d[query[1]]))
        
print('\n'.join(reversed(result)))
'''

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N, Q = map(int,input().split())
parent=[0]*N
for i in range(1,N):
    p=int(input())
    parent[i]=p-1

union=list(range(N))
def Union(a,b):
    a=ancestor(a)
    b=ancestor(b)
    if a>b:
        union[a]=b
    else:
        union[b]=a
def ancestor(n):
    if n==union[n]:
        return n
    return ancestor(union[n])

command=[]
for i in range(N-1+Q):
    a=tuple(map(int,input().split()))
    command.append(a)

r=[]
for i in range(len(command)-1,-1,-1):
    if command[i][0]==0:
        Union(command[i][1]-1,parent[command[i][1]-1])
    else:
        if ancestor(command[i][1]-1)==ancestor(command[i][2]-1):
            r.append(1)
        else:
            r.append(0)
for i in r[::-1]:
    if i==1:
        print("YES")
    else:
        print("NO")
'''














