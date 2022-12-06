'''
조각 움직이기

최대 5개의 조각이 있는 5*5 크기 보드. 조각을 적절히 움직여서 모든 조각이 연결되에 하려 한다.
한 번의 이동으로 하나의 조각을 상하좌우로 인접한 칸으로 옮길 수 있다. 보드의 상태가 주어질 때 최소 몇 번 이동해야 모든 조각이 연결 요소를 이루게 되는가?

입력
보드 상태 제시. 빈 곳은 . 조각은 * 조각은 1개 이상 5개 이하.

출력
첫째 줄에 문제의 정답을 출력한다. 몇 번 이동해야 하는지 출력.
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 이동
mov = [(-1,0), (0,1), (1,0), (0,-1)]

# 하나로 합쳐졌는가? 확인
def findOne(li):
    nli = list(li)[:]
    nset = set(nli)
    q = deque()
    q.append(nli.pop())
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<5 and 0<=nw<5 and ((nh, nw) in nset):
                nset.remove((nh, nw))
                q.append((nh, nw))
    return len(li) - len(nset)

# 하나로 이어지는 scnt개의 별 좌표들 리턴
def comb(scnt):
    ret = []
    combli = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    for com in combinations(combli, scnt):
        a = findOne(com)
        if a == scnt:
            ret.append(com)
    return ret

g = [list(input().rstrip()) for _ in range(5)]
sc = 0
stz = []

# 별 좌표 및 갯수 확인
for i in range(5):
    for j in range(5):
        if g[i][j] == '*':
            sc += 1
            stz.append((i, j))
# 1개면 0이다
if sc == 1:
    print(0)
    exit()
checklist = comb(sc) # 확인해야 할 별 조합리스트
ans = 20000 # 최솟값을 구해야 하므로
for i in checklist: # 확인 할 별 조합들
    strz = set(stz[:]) # 현재 별 위치들
    ians = 0 # 안쪽 정답 갱신 할 값
    ni = set(i) # 세트로 만든 new i
    reli = [] # remove list. ni에서 지워줘야 할 h, w를 담을 것
    for h, w in ni: # 같은 좌표 있따면
        if (h, w) in strz: # strz에서 지워준다
            strz.remove((h, w))
            reli.append((h, w))
    while reli: # 지워준다
        h, w = reli.pop()
        ni.remove((h, w))
#############################################
# 근데 윗 부분과 아랫 부분은 힙을 통해 해결하는 것이 좋을 듯?
    for h, w in ni:
        ilen = 20000
        ph, pw = -1, -1
        for nh, nw in strz:
            if ilen > abs(h-nh)+abs(w-nw):
                ilen = abs(h-nh)+abs(w-nw)
                ph, pw = nh, nw
        strz.remove((ph, pw))
        ians += ilen
    if ians < ans:
        ans = ians
print(ans)




'''
.....
..**.
....*
...*.
.....

*...*
.....
.***.
.....
.....

'''
'''
# 어리석었음

import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

# 섬 찾기
def findPart(ih, iw, cnt):
    q = deque([(ih, iw)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<5 and 0<=nw<5 and not v[nh][nw] and g[nh][nw] == '*':
                q.append((nh, nw))
                v[nh][nw] = 1
                parts[cnt].append((nh, nw))

# 섬 간 거리 최솟값
def findLength(idx):
    ret = 0
    oli = parts[idx]
    for i in parts:
        if i == idx:
            continue
        addRet = 20
        ili = parts[i]
        for h, w in oli:
            for nh, nw in ili:
                addRet = min(abs(h-nh) + abs(w-nw), addRet)
        ret += addRet * len(ili)
    return ret

parts = {}
v = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
g = [list(input().rstrip()) for _ in range(5)]
num = 0

# 부분 나누기
for i in range(5):
    for j in range(5):
        if v[i][j]:
            continue
        v[i][j] = 1
        if g[i][j] == '*':
            num += 1
            parts[num] = [(i, j)]
            findPart(i, j, num)

print(parts)
ans = 0
if len(parts) == 1:
    print(ans)
else:
    for i in range(1, num+1):
        a = findLength(i)
        print(a)



# 하나로 합쳐졌는가? 확인
def findOne(ih, iw):
    c = 0
    v = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    v[ih][iw] = 1
    q = deque([(ih, iw)])
    while q:
        h, w = q.popleft()
        c += 1
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<5 and 0<=nw<5 and not v[nh][nw] and g[nh][nw] == '*':
                v[nh][nw] = 1
                q.append((nh, nw))
    return c
'''


