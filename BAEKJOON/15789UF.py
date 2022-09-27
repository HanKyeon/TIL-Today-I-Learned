'''
CTP 왕국은 한솔 왕국을 이길 수 있을까?

왕국의 힘은 동맹의 힘. A와 B가 동맹, B와 C가 동맹, A와 C가 동맹.
K번 동맹 맺을 기회.
한솔 왕국과 동맹인 왕국과는 동맹을 맺을 수 없다. k번을 모두 사용하지 않아도 된다.

각 왕국들의 동맹 관계와 ctp 왕국의 번호, 한솔 왕국의 번호가 주어질 때, CTP 왕국의 힘 최댓값. 각 왕국의 번호는 1부터 n까지.

입력
왕국의 수 n, 동맹 관계 수 m. 3이상10만이하 1이상 20만이하.
m개 줄에 x, y 제시. x와 y가 동맹.
ctp왕국 번호, 한솔왕국 번호, 추가 동맹 기회 제시.

출력
ctp 왕국의 힘 최댓값 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서 넣기
    if x < y:
        parent[y] = x
        nodc[x] += nodc[y]
    else:
        parent[x] = y
        nodc[y] += nodc[x]

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
nodc = [1]*(n+1)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a == b:
        continue
    union(a, b)
c, h, k = map(int, input().rstrip().split())
c, h = find(c), find(h)
heap = []
for i in range(1, n+1):
    if parent[i] == h or parent[i] == c:
        continue
    if parent[i] != i:
        continue
    heappush(heap, (-nodc[i]))
while k:
    frz = heappop(heap)
    nodc[c] -= frz
    k -= 1
print(nodc[c])







