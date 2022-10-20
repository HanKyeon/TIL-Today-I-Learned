'''
전기가 부족해

전기가 부족함. 발전소 이미 건설되어 있음. 케이블 비용 최소화.
n개 도스 m개 간선 k개 발전소 노드.
모든 도시에 전기가 공급되도록 해결해야 한다.
케이블 당 발전소는 1개만.
-> MST를 만드는데, find해서 root가 발전소들이라면 pass

입력
n, m , k 제시. 도시 갯수, 간선 갯수(10만), 발전소 갯수 제시.
발전소 설치된 도시 번호. 한 줄 제시.
m개 줄 u, v, w 제시. u, v 연결 시 비용 w

출력
최소 비용 출력.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 안하고
    x, y = find(x), find(y)
    if x == y:
        return
    fla1, fla2 = x in bzs, y in bzs
    if fla1 and fla2:
        return False
    elif fla1 and not fla2:
        parent[y] = x
        alive.remove(y)
        return True
    elif not fla1 and fla2:
        parent[x] = y
        alive.remove(x)
        return True
    else:
        if x < y:
            parent[y] = x
            alive.remove(y)
            return True
        if y < x:
            parent[x] = y
            alive.remove(x)
            return True

def lego():
    global n, k
    # if n == k:
    #     return 0
    ret = 0
    while heap:
        cost, nod1, nod2 = heappop(heap)
        if union(nod1, nod2):
            ret += cost
        if len(alive) == k:
            return ret

n, m, k = map(int, input().rstrip().split())
bzs = set(map(int, input().rstrip().split()))
heap = []
parent = list(range(n+1))
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))
alive = set(range(n+1))
alive.remove(0)
print(lego())







