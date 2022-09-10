'''
클레어와 물약

세상에는 N종류의 물약, 클레어는 M개의 레시피.
레시피는 k개 1,2,3 물약번호3 이런식으로 제시.
가진 물약 무한대. 만들 수 있는 물약들을 전부 알아내기.

입력
3이상 20만이하 n 1이상 20만이하 m
레시피정보
클레어 물약 종류 갯수
물약 종류
'''
from collections import deque
import sys
input = sys.stdin.readline
# 레시피로 위상 정렬
n, m = map(int, input().rstrip().split())
reqn = [0] * (m) # 레시피의 요구 노드
g = [set() for _ in range(n+1)] # 어떤 숫자의 포션을 순회하면 몇번 레시피의 요구 노드를 깔 수 있는지
potion = [0]*m # 몇번 레시피를 완성하면 몇번 레시피가 생기는지
for i in range(m): # 데이터 입력
    s = list(map(int, input().rstrip().split()))
    num, idx = s.pop(0), s.pop()
    reqn[i] = num
    potion[i] = idx
    for j in s:
        g[j].add(i)

l = int(input()) # 필요 없음
ll = list(map(int, input().rstrip().split())) # 현재 가진 포션
ans = set(ll) # 정답을 set로 담아줄 것. visited처럼 쓸 것이다.
ll = deque(ll) # 덱으로 bfs 할 것
while ll: # bfs
    a = ll.popleft() # 이 포션이 있다.
    for i in g[a]: # 이 포션을 하면 깔 수 있는 노드들을 둘러보며
        reqn[i] -= 1 # 요구 노드 까주고
        if reqn[i] == 0 and not potion[i] in ans: # 요구 노드가 0이고 이미 만든 포션이 아니라면
            ans.add(potion[i]) # 정답에 넣고
            ll.append(potion[i]) # 큐에 넣는다.
ans = sorted(list(ans)) # 정답 출력
print(len(ans))
print(*ans)


'''
# 시간초과
from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
rcp = deque()
for _ in range(m):
    s = list(map(int, input().rstrip().split()))
    num, idx = s.pop(0), s.pop()
    rcp.append((len(s), set(s), idx))

l = int(input())
ll = list(map(int, input().rstrip().split()))
ans = set(ll)
while ll:
    a = ll.pop()
    b = len(rcp)
    for _ in range(b):
        req, vi, idx = rcp.popleft()
        if idx in ans:
            continue
        if a in vi:
            req -= 1
            vi.remove(a)
        if req == 0:
            ll.append(idx)
            ans.add(idx)
            continue
        rcp.append((req, vi, idx))
ans = sorted(list(ans))
print(len(ans))
print(*ans)
'''


'''
from heapq import heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rcp = []
for i in range(m):
    s = list(map(int, input().rstrip().split()))
    num, idx = s.pop(0), s.pop()
    rcp.append((set(s), idx))
l = int(input())
ll = set(map(int, input().rstrip().split()))
ans = []
while ll:
    mynum = ll.pop()
    ans.append(mynum)
    for i in rcp:
        if len(i[0]) == 0:
            continue
        if mynum in i[0]:
            i[0].remove(mynum)
        if len(i[0]) == 0:
            ll.add(i[1])
print(len(ans))
print(*sorted(ans))
'''


'''
# 3% 시간 초과
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rcp = []
for i in range(m):
    s = list(map(int, input().rstrip().split()))
    num, idx = s.pop(0), s.pop()
    rcp.append((set(s), idx))
l = int(input())
ll = set(map(int, input().rstrip().split()))
ans = []
while ll:
    mynum = ll.pop()
    ans.append(mynum)
    for i in rcp:
        if len(i[0]) == 0:
            continue
        if mynum in i[0]:
            i[0].remove(mynum)
        if len(i[0]) == 0:
            ll.add(i[1])
print(len(ans))
print(*sorted(ans))
'''


'''
# 시간 초과 파이썬10 파이파이12
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rcp = []
for _ in range(m):
    s = list(map(int, input().rstrip().split()))
    num, idx = s.pop(0), s.pop()
    rcp.append((set(s), idx))
l = int(input())
ll = set(map(int, input().rstrip().split()))
lll = -1
while lll != len(ll):
    lll = len(ll)
    for i in rcp:
        if i[1] in ll:
            continue
        if i[0].issubset(ll):
            ll.add(i[1])
ll = sorted(list(ll))
print(len(ll))
print(*ll)
'''










'''
# 임시 폐쇄. 사유 : 하나의 포션에 여러개의 레시피가 존재한다면?
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rcp = {}
for _ in range(m):
    s = list(map(int, input().rstrip().split()))
    num, idx = s.pop(0), s.pop()
    for i in range(num):
        if rcp.get(idx, 0):
            rcp[idx].append(s[i])
        elif rcp.get(idx, 0) == 0:
            rcp[idx] = [s[i]]
l = int(input())
nl = list(map(int, input().rstrip().split()))

print(rcp)
'''