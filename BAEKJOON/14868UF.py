'''
문명

n n 2차원 공간. 좌하단1,1 우상단n,n
두 정사각형 a,b와 a', b'이 두 조건 중 하나만 만족 할 때 인접해있다. a-a'이 1이고 b=b' b-b'이 1이고 a=a'. 그냥 한 칸 인접해있으면 된다는 것 같다.
문명의 최초 발상지는 모두 서로 다른 k곳에 있다. 각 정사각형에 해당하는 공간은 문명지역 혹은 미개지역.
최초 발생기는 문명지역. 최초 발상지가 인접해있다면 하나로 결합.
한 해가 지날 때마다 문명 지역은 자신과 인접한 지역에 문명 전파.
a,b가 문명지역이라면 사방에 문명 전파. bfs해서 전파. 인접하면 된다.
세계 크기, 문명 발상지의 수 및 위치를 입력으로 받아 모든 문명이 하나로 결합 될 때까지 걸리는 최소 햇수를 구해라.

입력
세계 크기 n, 발상지 수 k
k줄에 문명 발상지에 해당하는 정사각형의 위치 x,y를 나타내는 두 자연수 x와 y 제시.
'''


from collections import deque
import sys
input = sys.stdin.readline

def find(h, w):
    global parent, civs
    a = g[h][w]
    if parent.get((h, w), 0) != a:
        g[h][w] = find(civs[a][0], civs[a][1])
    return g[h][w]

def union(h1, w1, h2, w2):
    global civs
    a, b = find(h1, w1), find(h2, w2)
    if a == b:
        return
    if a == 0:
        g[h1][w1] = b
        return
    if b == 0:
        g[h2][w2] = a
        return
    if a in alive and not b in alive:
        g[h2][w2] = a
        return
    elif b in alive and not a in alive:
        g[h1][w1] = b
        return
    if 0 < a < b:
        g[h2][w2] = a
        civs[b] = civs[a]
        if b in alive:
            alive.remove(b)
        if civs[b] in parent:
            parent[(civs[b][0], civs[b][1])] = a
        return
    elif 0 < b < a:
        g[h1][w1] = b
        civs[a] = civs[b]
        if a in alive:
            alive.remove(a)
        if civs[a] in parent:
            parent[(civs[a][0], civs[a][1])] = b
        return

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, k = map(int, input().rstrip().split())
g = [[0] * n for _ in range(n)]
parent = {}
alive = set()
civs = [0]
q = deque()

for i in range(1, k+1):
    a, b = map(int, input().rstrip().split())
    a, b = a-1, b-1
    parent[(a, b)] = i
    g[a][b] = i
    alive.add(i)
    civs.append((a, b))
    q.append((a, b))

def bfs1t():
    global q, n
    nq = deque()
    while q:
        h, w = q.popleft()
        root = find(h, w)
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and find(nh, nw)!=root:
                union(h, w, nh, nw)
                nq.append((nh, nw))
                # print(parent)
                # print(0)
                # for i in g:
                #     print(*i)
                if len(alive) == 1:
                    return
    while nq:
        h, w = nq.popleft()
        q.append((h, w))
        root = find(h, w)
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and g[nh][nw] != 0:
                nth = find(nh, nw)
                if nth != root:
                    union(h, w, nh, nw)
                    if len(alive) == 1:
                        return

# print(parent)
# print(0)
# for i in g:
#     print(*i)

x = 0
c = 0
for i in range(1, k+1):
    h, w = civs[i][0], civs[i][1]
    for j in range(4):
        nh, nw = h+dh[j], w+dw[j]
        if (nh, nw) in parent:
            union(h, w, nh, nw)

print(parent)
print(civs, alive)
print(0)
for i in g:
    print(*i)
print('=======')

while len(alive) != 1:
    c+=1
    bfs1t()
    print(parent)
    print(civs, alive, parent)
    print(c)
    for i in g:
        print(*i)
    print('=======')
    print(civs, alive, parent)
print(c)




'''
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

'''






'''
5 4
1 1
2 1
2 5
5 2


10 3
1 1
1 3
1 8

2 2
1 1
1 2

4 2
1 1
4 4

20 4
2 2
15 16
19 11
7 9
'''

'''
from sys import stdin
from collections import deque

# 1. 유니온 함수.
def union(a_row, a_col, b_row, b_col):
    # 1) 예외 처리
    origin_a = find(a_row, a_col)
    origin_b = find(b_row, b_col)
    # 만약 a 지점과 b 지점의 조상이 같다면
    if origin_b == origin_a:
        return  # 연산하지 않음.
    # 2) 연산
    # (1) b가 통합된 문명일 때
    if origin_b not in origin_set:
        # b의 좌표에 a의 조상 문명 번호를 지도에 기입.
        MAP[b_row][b_col] = origin_a
        return
    # (2) a가 통합된 문명일 때
    if origin_a not in origin_set:
        # a의 좌표에 b의 조상 문명 번호를 지도에 기입.
        MAP[a_row][a_col] = origin_b
        return
    # (3) a와 b 모두가 존재할 때
    # 문명 번호가 더 작은 것을 우선순위로 통합.
    if origin_a < origin_b:
        MAP[b_row][b_col] = origin_a
        origin_set.remove(origin_b)
        origin_location[origin_b] = origin_location[origin_a]
        return
    else:
        MAP[a_row][a_col] = origin_b
        origin_set.remove(origin_a)
        origin_location[origin_a] = origin_location[origin_b]
        return


# 2. find 함수
def find(row, col):
    # 1) 선언
    # 현재 조상을 확인하고 싶은 값.
    x = MAP[row][col]
    # 2) 연산
    # (1) 예외처리: 현재 좌표값이 '근원지' 중 하나일 때
    if x in origin_set:
        return x    # 그대로 리턴
    # (2) 부모 정보 업데이트
    # a. origin_location 딕셔너리에서 x값의 '근원지' 값을 가져옴
    x_row, x_col = origin_location[x]
    # b. find
    origin = find(x_row, x_col)
    # c. 조상 정보 갱신
    MAP[row][col] = origin      # 조상 정보를 갱신.
    # 3) 반환
    return origin


# 델타를 이용한 2차원 배열 탐색.
DX = (0, 0, -1, 1)  # 상, 하, 좌, 우
DY = (-1, 1, 0, 0)  # 상, 하, 좌, 우
# 1. 입력
N, K = map(int, stdin.readline().split())
# 1-1. 추가 입력을 위한 선언
# 1) 각 좌표별 문명 정보를 기록하는 2차원 배열
MAP = [[0] * N for _ in range(N)]
# 2) key: 문명 번호, value: 문명 번호의 발상지
origin_location = dict()
# 3) 아직 통합되지 않은 발상지 번호들의 집합.
origin_set = set(range(1, K + 1))
# 2. 선언
civ_que = deque()   # 문명들 정보를 저장하는 que
next_que = deque()  # BFS 연산을 위한 que (2)
# 1-2. 문명 발상지 정보 입력.
# 문명 번호 1번부터 K 번 까지
for civilization in range(1, K + 1):
    # 1) 입력
    # 행, 열 좌표를 입력받아
    row, col = map(int, stdin.readline().split())
    row -= 1
    col -= 1
    # 2) 연산
    # (1) 지도에 배치
    MAP[row][col] = civilization
    # (2) 딕셔너리에 기입
    origin_location[civilization] = (row, col)
    # (3) 큐에 기입
    civ_que.append((row, col))

# 1-3. 문명 발상지 상쇄 .
for civ in civ_que:
    row, col = civ
    # 4방향을 순회하며
    for direction in range(4):
        next_row = row + DY[direction]
        next_col = col + DX[direction]
        # 인접 문명이 있을 경우
        if N > next_row >= 0 and N > next_col >= 0 and MAP[next_row][next_col]:
            # 문명 통합.
            union(row, col, next_row, next_col)

# 2. 연산
result = 0

# 종료조건:
# 문명들이 모두 1개로 통합되었을 때
while len(origin_set) != 1:
    result += 1

    # BFS 연산
    while civ_que:
        # 큐에 있는 모든 문명 좌표를 순회.
        row, col = civ_que.popleft()
        # 현재 좌표에 인접한 4 방향을 순회하며
        for direction in range(4):
            next_row = row + DY[direction]
            next_col = col + DX[direction]
            # 인덱스 값이 정상이고
            if N > next_row >= 0 and N > next_col >= 0:
                # 1) 문명이 전파되지 않은 지역이라면
                if not MAP[next_row][next_col]:
                    # 문명을 전파
                    MAP[next_row][next_col] = MAP[row][col]
                    # 다음 큐에 입력
                    next_que.append((next_row, next_col))
                    # (1) 문명 전파 후 옆에 다른 문명이 있는지 다시 확인.
                    for next_direction in range(4):
                        nnext_row = next_row + DY[next_direction]
                        nnext_col = next_col + DX[next_direction]
                        # 4 방향 순회 후
                        if N > nnext_row >= 0 and N > nnext_col >= 0 and MAP[nnext_row][nnext_col] and MAP[nnext_row][nnext_col] != MAP[next_row][next_col]:
                            # 인접한 문명을 다시 통합.
                            union(next_row, next_col, nnext_row, nnext_col)

                # 2) 문명이 전파되었으며 아직 통합되지 않았다면
                elif MAP[next_row][next_col] != MAP[row][col]:
                    union(row, col, next_row, next_col)
    print(origin_location)
    print(origin_set)
    for i in MAP:
        print(*i)
    # 현재 큐-다음 큐 교체 연산.
    next_que, civ_que = civ_que, next_que

# 4 .출력.
print(result)
'''

'''
# 시간 초과

from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n, k = map(int, input().rstrip().split())
v = [[0] * n for _ in range(n)]
g = [[0] * n for _ in range(n)]
q = deque()
opq = deque()
lst = []
okdk = set()

for _ in range(k):
    a, b = map(int, input().rstrip().split())
    g[a-1][b-1] = 2

# 합쳐주기
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            q = deque()
            g[i][j] = 1
            q.append((i, j))
            okdk.add((i, j))
            lst.append((i, j))
            while q:
                h, w = q.popleft()
                for k in range(4):
                    nh, nw = h + dh[k], w + dw[k]
                    if 0<=nh<n and 0<=nw<n and g[nh][nw] == 2:
                        g[nh][nw] = 1
                        q.append((nh, nw))
                        lst.append((nh, nw))
opq.append(lst[0])
A, B = lst[0]
v[A][B] = 1
q = deque(lst)


def bfs1():
    global q, n
    li = []
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and g[nh][nw] == 0:
                li.append((nh, nw))
                g[nh][nw] = 1
    q = deque(li)

def bfs2():
    global opq, n
    li = []
    while opq:
        h, w = opq.popleft()
        if h!=A and w!=B and (h, w) in okdk:
            okdk.remove((h, w))
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and g[nh][nw] == 1 and v[nh][nw] == 0:
                v[nh][nw] = 1
                opq.append((nh, nw))
            if 0<=nh<n and 0<=nw<n and g[nh][nw] == 0 and v[nh][nw] == 0:
                v[nh][nw] = 1
                li.append((nh, nw))
    opq = deque(li)

i = 0
while len(okdk) > 1:
    i += 1
    bfs1()
    bfs2()


print(i)
'''









