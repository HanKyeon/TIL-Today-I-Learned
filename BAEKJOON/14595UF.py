'''
동방 프로젝트 Large

동방이 갖고 싶던 병찬이. N개 방 중 하나 얻는다. N개 방은 일직선에 존재, 번호. 1번부터 n번까지.
빅-종빈 빌런 등장 벽 무너뜨린다.
x < y를 만족하는 두 방에 대해서 x번 방부터 y번 방 사이의 모든 벽을 허문다.
두 방 사이의 벽이 허물어지면 두 방은 하나의 방이 된다.
이미 허물어진 벽이 존재한다면 무시하고 다음 벽을 부순다.
외벽은 안부순다.
동방 갯수가 줄어들자 초조하다. 남는 동방 수를 구하고 싶어한다.
행동횟수 M과 동방 갯수 N이 주어졌을 때, 남은 동방 수를 구하자.

입력
동방 갯수 2이상 100만이하 n
행동횟수 0이상 5000이하 m 빌런 행동 횟수
m개줄에 걸쳐 행동 m개 제시. x번방부터 y번방 사이의 벽을 무너뜨리는 것.
동일 행동 가능.

출력
모든 행동이 끝난 후 남은 동방 갯수.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
parent = list(range(n+1))
heap = []
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    heappush(heap, (a, b))
if heap:
    wrk = []
    sva, svb = heappop(heap)
    while heap:
        a, b = heappop(heap)
        if sva <= a <= svb:
            svb = max(b, svb)
        else:
            wrk.append((sva, svb))
            sva, svb = a, b
    if wrk and wrk[-1] != (sva, svb):
        wrk.append((sva, svb))
    if not wrk:
        wrk.append((sva, svb))
    for a, b in wrk:
        parent[a] = b
a = 1
ans = 0
while a <= n:
    if parent[a] == a:
        a += 1
        ans += 1
    else:
        a = parent[a]
# print(parent)
print(ans)




'''
# 시간 초과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = int(input()), int(input())
parent = list(range(n+1))
bhvr = set()
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    bhvr.add((a, b))
while bhvr:
    a, b = bhvr.pop()
    parent[a:b+1] = [parent[b]]*(b+1-a)
ans = 0
for i in range(1, n+1):
    if parent[i] != i:
        continue
    ans+=1
print(ans)
'''













