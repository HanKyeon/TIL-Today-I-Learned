'''
도시 분할 계획

원숭이 한마리가 세상 구경 중.
n개 의 마을, m개의 길. 양방향.
마을을 두개의 마을로 분할 할 것이다. 분할 할 때 각 분리된 마을 안에 집들이 서로 연결 되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다. 집이 하나 이상 있어야 한다.
마을에 길을 없앨 수 있다.
분리된 마을 안에서도 두 집 사이에 경로가 존재하게 하면 길을 더 없앨 수 있다.
길들을 모두 없애고 유지비 합을 최소로 하고 싶다.

입력
n, m 제시. 집 갯수 길 갯수
n은 2이상 10만이하, m은 1이상 100만이하.
m개 줄 걸쳐 길의 정보가 a,b,c로 제시.

출력
남은 길 유지비 합의 최솟값.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서
    if x < y:
        parent[y] = x
        alive.remove(y)
    if x > y:
        parent[x] = y
        alive.remove(x)
    if len(alive) == 2:
        return True
    return False

n, m = map(int, input().rstrip().split())
heap = []
parent = list(range(n+1))
alive = set(range(1, n+1))
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))
ans = 0
while heap:
    c, a, b = heappop(heap)
    if find(a) == find(b):
        continue
    ans += c
    if union(parent[a], parent[b]):
        break
print(ans)

















