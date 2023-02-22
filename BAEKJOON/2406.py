'''
안정적인 네트워크

네트워크 고장나도 연결되어 있도록 안정적인 네트워크 구축 원함.
1. 직접 연결된 두 컴이 끊어져도 경유하여 연결되길 바람.
2. 고장난 경우 고장나지 않은 컴 끼리 연결되어 있기를 바람.
컴 연결 비용은 일정치 않다. 네트워크 연결 상태를 입력 받아 안정적ㅇ니지 아닌지 판별하고 아닌경우 최소 비용.

입력
n, m  제시. 컴, 간선.
m개 줄 x, y 제시. 직접 연결.
n개 줄에 그래프 제시. 연결 할 때 비용. 
i, j == j, i 비용 본사컴 1번

출력
최소비용X와 연결할 컴 쌍 갯수 K 출력.
K개 줄 연결 할 컴퓨터들 번호 출력. 안정적이라면 X=0, K=0
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

n, m = map(int, input().rstrip().split())
parent = list(range(n))
alive = set(range(n))
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    i, j = find(i-1), find(j-1)
    if i == j:
        continue
    union(i, j)
egs = []
for i in range(n):
    s = list(map(int, input().rstrip().split()))
    for j in range(i+1, n):
        ri = find(i)
        rj = find(j)
        if ri == rj:
            continue
        heappush(egs, (s[j], i, j))

ans, ansli = 0, []
while egs and len(alive) > 1:
    cost, i, j = heappop(egs)
    ri, rj = find(i), find(j)
    if ri == rj or not ri or not rj:
        continue
    union(ri, rj)
    ans += cost
    ansli.append((i+1, j+1))

print(ans, len(ansli))
for i in ansli:
    print(*i)

# cost = [list(map(int, input().rstrip().split())) for _ in range(n)]



