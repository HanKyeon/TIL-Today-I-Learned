'''
개구리 점프

통나무 n개가 떠있다. 수평방향으로. 개구리는 A에서 B로 수직 방향으로 점프 가능.
점프 할 때 다른 통나무가 있으면 안된다.
통나무 좌표를 받아 주어진 통나무 쌍에 대해 한 번 이상의 점프로 이동이 가능한지 판단해라.

입력
통나무 갯수 N과 질문 갯수 Q 제시. 둘 다 10만 이하
N개 줄에 통나무의 x1, x2, y 세 정수 제시. 두 점 x1,y x2,y를 잇는 선분 형태. 모든 좌표는 0이상 1억 이하. 주어진 순서대로 1번부터 번호 제시. 서로 다른 두 통나무는 만나지 않는다.
다음 Q개의 줄에 서로 다른 두 통나무의 번호 제시.

출력
Q개 줄에 정답 출력. 이동 가능하다면 1, 불가능하다면 0
'''
'''
사이에 통나무 있어도 상관 없지 않음? 어차피 union 되는건데. 한 번 더 뛰면 되잖아.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 한 값 넣기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, q = map(int, input().rstrip().split())
parent = list(range(n+1))
heap =[]
for i in range(1, n+1):
    x1, x2, y = map(int, input().rstrip().split())
    heappush(heap, [x1, x2, i]) 

x1, x2, idx = heappop(heap)
while heap:
    nx, nx2, nidx = heappop(heap)
    if x1<=nx<=x2:
        union(find(idx), find(nidx))
        x2 = max(x2, nx2)
    else:
        x1, x2, idx = nx, nx2, nidx

for _ in range(q):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a == b:
        print('1\n')
    else:
        print('0\n')

'''
# 시간 초과

import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 한 값 넣기
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, q = map(int, input().rstrip().split())
parent = list(range(n+1))
g = [[] for _ in range(n+1)]
for i in range(1, n+1):
    x1, x2, y = map(int, input().rstrip().split())
    g[i] = [x1, x2, y]

for i in range(1, n):
    x1, x2, y = g[i]
    for j in range(i+1, n+1):
        xx, yy = find(i), find(j)
        if xx == yy:
            continue
        a1, a2, b = g[j]
        if x1<=a1<=x2 or x1<=a2<=x2 or a1<=x1<=a2 or a1<=x2<=a2:
            union(xx, yy)

for _ in range(q):
    a, b = map(int, input().rstrip().split())
    a, b = find(a), find(b)
    if a == b:
        print('1\n')
    else:
        print('0\n')
'''










