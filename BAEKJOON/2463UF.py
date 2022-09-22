'''
비용

간선에 가중치가 있는 그래프.
정점 수 n. 1부터 n까지 번호. 가중치 서로 다름.
서로 다른 두 정점 u, v에 대해 Cost(u, v)는 다음에서 제거되는 간선들의 가중치 합. u와 v 사이의 경로가 있으면 이 그래프의 최소 가중치 간선을 그래프에서 제거한다. 이 과정을 u와 v 사이의 경로가 없을 때까지 반복한다.

간선에 가중치가 있는 그래프가 주어질 때, u<v인 모든 두 정점 u,v에 대한 cost(u,v)들의 총 합을 구하는 프로그램 작성. 총 합합이 10억 이상이라면 10억으로 나눠서 출력.

입력
정점 수 n, m. n은 10만이하 m도 10만이하 제시.
간선 하나에 대한 정보를 나타내는 세 양정수 x, y, w 제시.
x,y의 간선 가중치가 w다.

출력
u<v인 모든 두 정점에 대한 cost(u,v)들의 총 합을 첫째 줄에 출력한다.
단 총합이 10**9 나머지로 출력한다.
'''
'''
연결 하기 전에 parent가 같다면 pass
union을 하게 된다면 여태 간선 가중치 합 넣어주기.
'''
# 메모리 해결 해보자!
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global ans
    x, y = find(x), find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
        ans += nodc[x]*nodc[y] * (egsum-sval)
        nodc[x] += nodc[y]
    else:
        parent[x] = y
        ans += nodc[x]*nodc[y] * (egsum-sval)
        nodc[y] += nodc[x]

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]
nodc = [1] * (n+1)
heap = []
egsum = 0
for _ in range(m):
    x, y, w = map(int, input().rstrip().split())
    egsum += w
    heappush(heap, (-w, x, y))
sval = 0
ans = 0
while heap:
    val, x, y = heappop(heap)
    union(x, y)
    sval -= val
print(ans%(10**9))




'''
import sys
input = sys.stdin.readline

def nCr(x):
    return (x-1)*x // 2

def find(x):
    if head[x] == x: return head[x]
    head[x] = find(head[x])
    return head[x]


def union(a, b):
    global S
    a = find(a)
    b = find(b)
    if a == b: return
    S -= nCr(counter[a])
    S -= nCr(counter[b])

    if a < b:
        head[b] = a
        counter[a] += counter[b]
        S += nCr(counter[a])
    else:
        head[a] = b
        counter[b] += counter[a]
        S += nCr(counter[b])
N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
info.sort(key = lambda x: x[2], reverse = True)
head = [x for x in range(N+1)]
S = 0
res = 0
counter = [1]*(N+1)
for a, b, v in info:
    union(a, b)
    res += S*v
if res >= 10**9:
    print(res%10**9)
else:
    print(res)
'''





