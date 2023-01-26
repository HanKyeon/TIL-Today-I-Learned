'''
우주신과의 교감.

아직 연결되지 않은 우주신들을 연결해야 한다. 정신적 통로 길이의 합이 최소가 되게 통로를 만들어라.

입력
노드 갯수 n, 이미 연결된 통로 ㅅ갯수 m 제시.
n개 줄에 좌표 제시.
m개 줄 이미 연결된 통로 제시.

출력
최소 통로 길이 출력. 소수점 둘째자리까지.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
        alive.remove(y)
    else:
        parent[x] = y
        alive.remove(x)
    return True if len(alive) == 1 else False

n, m = map(int, input().rstrip().split())
godzp = [[]]+[list(map(int, input().rstrip().split())) for _ in range(n)]
alrd = [list(map(int, input().rstrip().split())) for _ in range(m)]
parent = list(range(n+1))
alive = set(range(1, n+1))
while alrd:
    a, b = alrd.pop()
    ra, rb = find(a), find(b)
    if ra == rb:
        continue
    union(ra, rb)

egs = []
for a in range(1,n):
    for b in range(a+1,n+1):
        if a == b:
            continue
        if find(a) == find(b):
            continue
        ax, ay = godzp[a]
        bx, by = godzp[b]
        heappush(egs, (((ax-bx)**2 + (ay-by)**2)**0.5, a, b))

ans = 0
while egs:
    cost, a, b = heappop(egs)
    ra, rb = find(a), find(b)
    if ra == rb:
        continue
    ans += cost
    if union(ra, rb):
        break

print(f"{ans:.2f}")




