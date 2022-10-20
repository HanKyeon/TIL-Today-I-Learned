'''
방탈출

1번부터 n개 노드.
워프 설치 시간 ci. 출구로 바로 연결되는 비상탈출구 설치 시간 ti.
한 작업이 끝나야 다음 작업 가능.
워프는 최대 m개 설치 가능.
워프와 비상탈출구를 설치 하는 데 걸리는 최소 비용.

입력
n, m 제시. 2이상 20만이하, 1이상 10만이하.
M개 줄 워프 정보 세 정수 a, b, c 제시. a번방 b번방 잇는데 c 시간. 같은 방 잇는거 여러개일 수 있음.
n개 정수 리스트 제시. i번째 방에 비상탈출구를 설치하는데 드는 시간.

출력
워프/비상탈출구 설치 시간 최소.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 해서. 같아도 연결 해줘야 이득일 가능성 높음.
    if bsg[x] < bsg[y]:
        parent[y] = x
        bsg[y] = bsg[x]
    else :
        parent[x] = y
        bsg[x] = bsg[y]

n, m = map(int, input().rstrip().split())
heap = []
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    heappush(heap, (c, a, b))
bsg = [0] + list(map(int, input().rstrip().split()))
parent = list(range(n+1))

ans = 0
while heap:
    cost, nod1, nod2 = heappop(heap)
    root1, root2 = find(nod1), find(nod2)
    if root1 == root2:
        continue
    if bsg[root1] > cost or bsg[root2] > cost:
        union(root1, root2)
        ans += cost

for i in range(1, n+1):
    if parent[i] == i:
        ans += bsg[i]

print(ans)







