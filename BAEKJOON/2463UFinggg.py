'''
비용

간선에 가중치가 주어진 그래프.
정점의 수가 N
모든 정점은 1부터 N까지 번호가 붙여져 있고, 모든 간선들의 가중치는 서로 다르다.
이 때 서로 다른 두 정점 u, v에 대하여 cost(u, v)는 제거되는 간선들의 가중치 합이다. u와 v 사이의 경로가 있으면 이 그래프의 최소 가중치 간선을 그래프에서 제거한다. u와 v 사이에 경로가 없을 때까지 반복.
간선을 가중치 순으로 제거하면서 u와 v 사이의 경로가 없을 때까지 뺀 간선 가중치의 합은? 10**9로 나눈 나머지로 출력.

입력
정점의 수 n 1이상 10만이하 간선의 수 m 1이상 10만이하
간선 정보 x, y, z
x, y 간선의 가중치가 w임을 의미.

출력
u<v인 모든 두 정점에 대한 cost(u, v) 총합을 첫째 줄에 출력. 10**9로 나눠서
'''
'''
1. 두 정점에 대해 오직 하나로만 연결되어 있다는 말이 없다.
2. 간선 정보를 m개 주니까 간선 m이라고 해두자
3. 두 간선의 가중치가 같다면 어떤 순서로 빠지는거지? -> u < v 형태로 빠진다...
4. 10만을 10만번 돌면 100억번 연산이다. 주의. 최소한으로 돌아야 함
'''
from heapq import heappop, heappush
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
        parent[y] = a
    else:
        parent[x] = b

def check(x, y):
    return find(x) == find(y)

n, m = map(int, input().rstrip().split())
heap = []
parent = list(range(n))
for i in range(m):
    x, y, w = map(int, input().rstrip().split())
    x, y = x-1, y-1
    if y < x:
        heappush(heap, (-w, y, x))
    else:
        heappush(heap, (-w, x, y)) # 가중치, 간선 번호, 시작 도착 방향x

while heap:
    val, nod1, nod2 = heappop(heap)





















