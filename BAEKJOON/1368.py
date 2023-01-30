'''
물대기

n개 논에 물을 댈 것이다.
1. 직접 논에 우물을 판다
2. 다른 논으로부터 물을 끌어온다.
각각의 논에 대해 우물을 파는 비용과 논들 사이에 물을 끌어오는 비용이 제시되었을 때, 최소의 비용으로 모든 논에 물을 대는 것이 문제이다.

입력
논의 수 n
n개 줄 i번째 논에 우물 팔 때 드는 비용.
n개 줄 n개 수 제시. i, j 길 연결 비용.

출력
모든 논에 물을 대는데 필요한 최소 비용 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x == y:
        return False
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return True

n = int(input())
egs = []
parent= list(range(n+1))
for i in range(1, n+1):
    s = int(input())
    heappush(egs, (s, 0, i))
for i in range(1, n+1):
    s = list(map(int, input().rstrip().split()))
    for j in range(i, n):
        heappush(egs, (s[j], i, j+1))

ans = 0
while egs:
    cost, i, j = heappop(egs)
    if union(find(i), find(j)):
        ans += cost
print(ans)





'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x == y:
        return
    wx, wy = wumul[x], wumul[y]
    if wx > wy:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())
egs, exegs = [], []
wumul = [int(input()) for _ in range(n)]
parent, v = list(range(n)), [0]*n

for i in range(n):
    s = list(map(int, input().rstrip().split()))
    for j in range(i+1, n):
        heappush(egs, (s[j], i, j))

ans = 0
while egs:
    cost, i, j = heappop(egs)
    if v[i] and v[j]:
        heappush(exegs, (cost, i, j))
        continue
    union(find(i), find(j))
    v[i], v[j] = 1, 1
    ans += cost

while exegs:
    cost, i, j = heappop(exegs)
    ri, rj = find(i), find(j)
    if ri == rj:
        continue
    if wumul[ri] > cost and wumul[rj] > cost:
        continue
    ans += cost
    union(ri, rj)

for i in range(n):
    ri = find(i)
    if i == ri:
        ans += wumul[i]

print(ans)
'''



