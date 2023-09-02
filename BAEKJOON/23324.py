'''
어려운 모든 정점 쌍 최단 거리

n개 정점, m개 양방향 간선. 하나의 간선만 1 가중치, 나머지 없음
모든 정점쌍의 최단거리 합을 구하려 한다. 모든 쌍 i,j에 대해 i와 j간 최단 거리를 전부 더한 값을 구할 것이다.

입력
n, m, k 제시.
m개 줄 a, b 제시
k번째 간선의 가중치는 1이고, 나머지 간선의 가중치는 0이다.

출력
모든 정점 쌍의 최단 거리 합 출력.
'''
'''
유파로, k일 때 받은 정점을 부모로 갖도록 짠다.
그 후에 같은 부모를 갖는다면 0, 다른 부모를 갖는다면 1
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x in roots and y in roots:
        if x < y: parent[y] = x; return
        else: parent[x] = y; return
    elif x in roots: parent[y] = x; return
    elif y in roots: parent[x] = y; return
    if x < y: parent[y] = x; return
    parent[x] = y

n, m, k = map(int, input().rstrip().split())
roots, queries = None, []
parent = list(range(n+1))

for i in range(1, m+1):
    a, b = map(int, input().rstrip().split())
    if i == k:
        roots = {a, b}
        continue
    queries.append((a, b))

for a, b in queries:
    union(a, b)

cnt = 1
a = find(1)
for i in range(2, n+1):
    if find(i) == a:
        cnt+=1
print(cnt*(n-cnt))

# 마지막에 조합 형태라서 곱으로 처리한다는 생각을 못했음

'''
import sys
input=sys.stdin.readline


def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])

    return disjoint[x]

def Union(a,b):

    a=Find(a)
    b=Find(b)

    if a>b:
        disjoint[a]=b
    else:
        disjoint[b]=a

def Answer(parent):

    tmp=0
    for i in range(1,N+1):
        if Find(i)==parent:
            tmp+=1
    return tmp

N,M,K=map(int,input().split())

disjoint=[ i for i in range(N+1) ]

Node1,Node2=0,0

for i in range(M):

    u,v=map(int,input().split())

    if i!=K-1: # 가중치가 있는 지점은 합치지않는다.
        Union(u,v)
    else:
        Node1,Node2=u,v

if Find(Node1)==Find(Node2): # 예제 2와 같다면
    print(0)
else:
    total=Answer(disjoint[1])

    print(total*(N-total))

'''
