'''
체스 토너먼트

체스 대회. 체스 플레이어는 배심원에게 자기 경기 보고 가능. 상대방 확인 불가능. 따라서 경쟁자가 경기를 만들어 자신을 승자로 허위 신고 가능.
플레이어의 기술 수준이 더 높으면 항상 상대를 이긴다. 기술이 같으면 무승부이다.
선수의 실력은 모른다.
보고된 일치 목록이 주어지면 이 목록이 일치하는지 결정하는 프로그램 만들어달라.
잘못 보고 되었음을 확인 할 수 있으면 맞ㄴ냐 틀리냐 판단.

입력
두개의 정수 n, m 2이상 5만이하, 1이상 25만이하. n명의 플레이어와 m개의 보고된 경기.
m줄에 정수 k, = > L 제시. k와 l은 플레이어, =은 무승부, >는 k가 승리.
주어진 플레이어 간 경기는 최대 한 번. 각 플레이어는 보고된 경기에 최소 한 번 이상 참여.

출력
consistent or inconsistent 맞으면 consistent인듯?
'''
'''
= 연산자는 union으로
> 연산자는 count[root]를 조정해서 find(val)을 통해

= 연산자 우선 처리. union으로.
> 연산자의 초기값이 문제네.
a > b
find(b) = find(a) -1
find(a) = find(b) +1
둘 중 하나로 해야하나?
> 연산자를 후처리 하면서
if find(a) < find(b): return False
이런식으로 하면 되려나?

1. 같은 그룹 내 대소비교 시 inconsistent
2. 작고 작은 것 보다 크다 라고 나오면 inconsistent : 위상정렬에서 사이클이 나온다거나, 등.
'''
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find 한 상태로
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
parent = list(range(n))
cal = []
for _ in range(m):
    a, ysz, b = input().rstrip().split()
    a, b = int(a), int(b)
    if ysz == '=':
        a, b = find(a), find(b)
        union(a, b)
    else:
        heappush(cal, (a, b))
reqn = [0]*(n)
g = [[] for _ in range(n)]
grp = []
for i in range(n):
    if parent[i] == i:
        grp.append(i)

ans = ''

while cal:
    a, b = heappop(cal)
    # print('before find :', a, b)
    a, b = find(a), find(b)
    # print('after find : ', a, b)
    if a == b:
        ans = 'inconsistent'
        break
    reqn[a] += 1
    g[b].append(a)
# print(f"grp : {grp}")
# print(f"reqn : {reqn}")
# print(f"graph : {g}")
if not ans:
    li = deque([i for i in grp if reqn[i]==0])
    while li:
        a = li.popleft()
        a = find(a)
        for i in g[a]:
            reqn[i] -= 1
            if reqn[i] == 0:
                li.append(i)
    if [v for v in reqn if v > 0]:
        ans = 'inconsistent'
if not ans:
    ans = 'consistent'
# print(f"grp : {grp}")
# print(f"reqn : {reqn}")
# print(f"graph : {g}")
print(ans)











