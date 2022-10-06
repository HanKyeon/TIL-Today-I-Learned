'''
나만 안되는 연애

대학 간 도로 데이터.
1. 사심 경로는 남초-여초 대학만 연결하는 도로로만 이루어져 있다.
2. 어떤 대학교에서든 모든 댛가교로 이동 가능해야한다.
3. 최단거리여야 한다.
경로의 길이는?

입력
학교 수 n, 도로 수 m
남초면 M 여초면 W
a, b, c 제시. a와 b 연결 거리 c

출력
mst 최대치
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x < y:
        parent[y] = x
        nodc[x] += nodc[y]
    else:
        parent[x] = y
        nodc[y] += nodc[x]

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
nodc = [1]*(n+1)
mw =['']+ list(input().rstrip().split())
heap = []
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))

ans = 0
fla = False
while heap:
    cost, nod1, nod2 = heappop(heap)
    if mw[nod1] == mw[nod2]:
        continue
    nod1, nod2 = find(nod1), find(nod2)
    if nod1 == nod2:
        continue
    ans += cost
    union(nod1, nod2)
    if nodc[find(nod1)] == n:
        fla = True
        break
if fla:
    print(ans)
else:
    print(-1)


'''
# 빠름

input = sys.stdin.readline

def find(n):
	if p[n] < 0:
		return n
	t = n
	while p[t] >= 0:
		t = p[t]		
	p[n] = t
	return p[n]

def merge(a, b):
	a, b = find(a), find(b)
	if a == b:
		return
	p[b] = a

N, M = map(int, input().split())
t = input().split()
edge = []
p = [-1] * N
for i in range(M):
	a, b, c = map(int, input().split())
	a -= 1; b -= 1
	if t[a] == t[b]:
		continue
	edge.append((a, b, c))
edge.sort(key=lambda x:x[2])
total = 0
for fr, de, cost in edge:
	if find(fr) == find(de):
		continue
	merge(fr, de)
	total += cost
print(total if p.count(-1) == 1 else -1)
'''



