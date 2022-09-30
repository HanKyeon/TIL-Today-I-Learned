'''
리그 오브 레게노

아이템 사이 구매 순서 존재.
두 아이템 간 선후관계 일부만 안다. 반복하여 아이템 살 때 전체 구매 순서.
같은 거라면 사전순 구매.

입력
n
문자열 a, b 제시.
b를 사기 위해 a를 사야한다.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
itmz = {}
g = {}
for _ in range(n):
    a, b = input().rstrip().split()
    if itmz.get(b, 0):
        itmz[b].add(a)
    else:
        itmz[b] = {a}
    if itmz.get(a, 0):
        pass
    else:
        itmz[a] = set()
    if g.get(a, 0):
        g[a].add(b)
    else:
        g[a] = {b}
heap = []
for i in itmz:
    if not itmz[i]:
        heappush(heap, (0, i))
ans = []
while heap:
    dep, inm = heappop(heap)
    ans.append(inm)
    del itmz[inm]
    delnm = []
    if g.get(inm, 0) == 0:
        continue
    for i in g[inm]:
        itmz[i].remove(inm)
        if not itmz[i]:
            heappush(heap, (dep+1, i))

if ans and not itmz:
    for i in ans:
        print(i)
else:
    print(-1)

'''
빠른 코드
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
ind = defaultdict(int)

for _ in range(n):
    a, b = input().split()
    graph[a].append(b)
    ind[b] += 1

q = deque([i for i in graph if not ind[i]])

s = []
while q:
    temp = []
    for _ in range(len(q)):
        now = q.popleft()
        temp.append(now)

        for i in graph[now]:
            ind[i] -= 1
            if not ind[i]:
                q.append(i)
    s += sorted(temp)

if len(s) == len(graph):
    for i in s:
        print(i)
else:
    print(-1)
'''









