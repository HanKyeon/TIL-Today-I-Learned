'''
퍼즐

3*3 칸 옮기기 

입력
수 아홉게

출력
최소 이동 횟수.
불가능 할 경우 -1 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

# 일렬 리스트로 가정했을 때
# -1, +1, -3, +3 과 위치 교환 가능.
# 줄바꿈 생각을 못했다. 줄바꿈 고려 해야한다.

tg = [8,0,1,2,3,4,5,6,7]

def bfs(li):
    if li == tg:
        return 0
    q = deque()
    q.append((li, 0))
    while q:
        li, cnt = q.popleft()
        idx = li[0]
        if 0<=idx+1<9 and idx//3 == (idx+1)//3:
            p1idx=li.index(idx+1)
            li[0], li[p1idx] = li[p1idx], li[0]
            if tuple(li) not in sets:
                if li == tg:
                    return cnt+1
                q.append((li[:], cnt+1))
                sets.add(tuple(li))
            li[0], li[p1idx] = li[p1idx], li[0]
        if 0<=idx-1<9 and idx//3 == (idx-1)//3:
            m1idx=li.index(idx-1)
            li[0], li[m1idx] = li[m1idx], li[0]
            if tuple(li) not in sets:
                if li == tg:
                    return cnt+1
                q.append((li[:], cnt+1))
                sets.add(tuple(li))
            li[0], li[m1idx] = li[m1idx], li[0]
        if 0<=idx+3<9:
            p3idx = li.index(idx+3)
            li[0], li[p3idx] = li[p3idx], li[0]
            if tuple(li) not in sets:
                if li == tg:
                    return cnt+1
                q.append((li[:], cnt+1))
                sets.add(tuple(li))
            li[0], li[p3idx] = li[p3idx], li[0]
        if 0<=idx-3<9:
            m3idx = li.index(idx-3)
            li[0], li[m3idx] = li[m3idx], li[0]
            if tuple(li) not in sets:
                if li == tg:
                    return cnt+1
                q.append((li[:], cnt+1))
                sets.add(tuple(li))
            li[0], li[m3idx] = li[m3idx], li[0]
    return -1

nl = []
jp = [0]*9
for i in range(3):
    a, b, c = map(int, input().rstrip().split())
    nl.append(a)
    jp[a]=i*3
    nl.append(b)
    jp[b]=i*3+1
    nl.append(c)
    jp[c]=i*3+2
sets = {tuple(jp)}
print(bfs(jp))

'''
# 비트마스킹의 신

from collections import deque
#보드의 상태를 0~8까지로 표현한다면,
"""
0000
0001
0010
0011
0100
0101
0110
0111
1000 #다음과 같은 9개 값들의 집합으로 나타낼 수 있음
set으로 표현
"""
resultSet = set()
#
def getBit(status,index):  #원하는 인덱스에 있는 번호 불러오기
    return (status >> (8 - index) * 4) & 15

def setBit(status,index,number): #원허는 인덱스에 있는 번호 세팅하기
    status &= ~(15 << (8-index)*4)
    status |= (number << ((8 - index) * 4))
    return status

cur = 0
hole = 0
goal = 0

for i in range(8):  goal = setBit(goal,i,i+1)

for i in range(3):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        cur = setBit(cur,i*3+j,line[j])
        if not line[j]: hole = i * 3 + j

resultSet.add(hole)
q = deque([(cur,hole,0)])

dx,dy = [1,0,-1,0],[0,1,0,-1]

while q:
    val,hole,depth = q.popleft()
    if val == goal:
        print(depth)
        exit(0)

    x, y = hole // 3, hole % 3
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < 3 and 0 <= ny < 3): continue
        #값 변경하기

        nxyVal = getBit(val,nx * 3 + ny)

        nextVal = setBit(val, x * 3 + y, nxyVal)
        nextVal = setBit(nextVal, nx * 3 + ny, 0)

        if nextVal in resultSet: continue
        resultSet.add(nextVal)
        q.append((nextVal,nx*3+ny,depth+1))
print(-1)
'''

'''
# 단순 bfs
from collections import deque

li = [list(map(int, input().split())) for _ in range(3)]

target = 123456789

to_coord = lambda index: (index // 3, index % 3)
to_index = lambda x, y: x * 3 + y

def get_w(x, y):
    index = to_index(x, y)
    return 10 ** (8 - index)
    
cur = 0
for i in range(3):
    for j in range(3):
        if li[i][j] == 0:
            li[i][j] = 9
        cur += get_w(i, j) * li[i][j]
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
        
result = -1

vt = {cur}

queue = deque()
queue.append((cur, 0))
while queue:
    cur, c = queue.popleft()
    
    if cur == target:
        result = c
        break
    
    scur = str(cur)
    index = scur.index('9')
    x, y = to_coord(index)
    
    temp_ncur = cur - get_w(x, y) * 9
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
            continue
        nindex = to_index(nx, ny)
        
        ncur = temp_ncur
        num = int(scur[nindex])
        ncur -= num * get_w(nx, ny)
        
        ncur += 9 * get_w(nx, ny)
        ncur += num * get_w(x, y)
        
        if ncur not in vt:
            vt.add(ncur)
            queue.append((ncur, c + 1))
            
print(result)
'''






