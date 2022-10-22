'''
회장 뽑기

bfs해서 깊이가 가장 얕은 사람이 회장 후보.
점수는 bfs 깊이
점수, 후보 수
회장 후보 오름차순 출력해라.

입력
회원 수 n 제시.
2개의 수 제시. -1 -1 등장 시 끝

출력
회장 후보 점수, 회장 후보의 수
회장 후보들 오름차순
'''
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def bfs(prm):
    global n
    v = [0]*(n+1)
    v[prm] = 1
    q = deque([(prm, 0)])
    while q:
        num, dep = q.popleft()
        for i in g[num]:
            if v[i]:
                continue
            v[i] = 1
            q.append((i, dep+1))
    return dep, prm

n = int(input())
g = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().rstrip().split())
    if a == -1 and b == -1:
        break
    g[a].append(b)
    g[b].append(a)
heap = []
for i in range(1, n+1):
    heappush(heap, bfs(i))
fla = heap[0][0]
cnt = 0
ans = []
while heap and heap[0][0] == fla:
    a, b = heappop(heap)
    cnt += 1
    ans.append(b)
print(fla, cnt)
print(*ans)




