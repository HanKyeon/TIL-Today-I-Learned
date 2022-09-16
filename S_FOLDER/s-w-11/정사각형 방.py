'''
정사각형 방

n*n 방. i,j에는 1이상 n제곱 이하 수 모든 방 다름
어떤 방에 있다면 상하좌우 다른 방 이동 가능
이동하려는 방이 존재해야하고 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 1 더 커야한다. 어떤 수가 적힌 방에서 있어야 가장 많은 갯수의 방을 이동 할 수 있는지

입력
테케T
1이상 1000이하 정수 n 제시.
i번째 줄에 N개의 정수가 공백 하나로 구분되어 제시.
Aij는 모두 서로 다른 수

출력
#테케T 처음 출발해야하는 방 번호, 최대 몇개 방 이동 가능한지.
여러개라면 적힌 수가 가장 적은 것.
'''
from heapq import heappop, heappush
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
def 탐색(i, j):
    for k in range(4):
        ni, nj = i+dh[k], j+dw[k]
        if 0<=ni<n and 0<=nj<n and g[ni][nj] == g[i][j]-1:
            dp[ni][nj]=dp[i][j]+1
    if not heap:
        heappush(heap, (-dp[i][j], g[i][j]))
    elif heap[0][0] >= -dp[i][j]:
        heappush(heap, (-dp[i][j], g[i][j]))
for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dp = [[1]*n for _ in range(n)]
    좌표 = [() for _ in range(n**2)]
    for i in range(n):
        for j in range(n):
            좌표[g[i][j]-1] = (i, j)
    heap = []
    for i in reversed(좌표):
        탐색(i[0], i[1])
    a = heappop(heap)
    print(f"#{testcase} {a[1]} {-a[0]}")

'''
from collections import deque
from heapq import heappop, heappush

dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]

def bfs(hh, ww):
    global n
    q = deque()
    q.append((hh, ww, 1))
    while q:
        h, w, c = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and g[h][w]+1 == g[nh][nw]:
                q.append((nh, nw, c+1))
    return (-c, g[hh][ww])

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    heap = []
    for i in range(n):
        for j in range(n):
            heappush(heap, bfs(i, j))
    a = heappop(heap)
    print(f"#{testcase} {a[1]} {-a[0]}")
'''

'''
# dfs 핵별로
from heapq import heappop, heappush
dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]
def dfs(i, j):
    for k in range(4):
        ni, nj = i+dh[k], j+dw[k]
        if 0<=ni<n and 0<=nj<n and g[ni][nj] == g[i][j]-1:
            dp[ni][nj]=dp[i][j]+1
            dfs(ni, nj)
    if not heap:
        heappush(heap, (-dp[i][j], g[i][j]))
    elif heap[0][0] >= -dp[i][j]:
        heappush(heap, (-dp[i][j], g[i][j]))
for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dp = [[1]*n for _ in range(n)]
    heap = []
    for i in range(n):
        for j in range(n):
            dfs(i, j)
    a = heappop(heap)
    print(f"#{testcase} {a[1]} {-a[0]}")
'''

'''
# 빠른 코드

# 상 하 좌 우 
 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
for tc in range(1, int(input())+1):
    N = int(input())
 
    nums = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N**2 +1) # 0, 1 ~ N^2 까지 숫자가 하나씩은 나와야 함 (문제 조건)
 
    for row in range(N):
        for col in range(N):
            # 현재 위치에서 사방 탐색
            here = (row, col)
            for direction in range(4):
                nr = here[0] + dr[direction]
                nc = here[1] + dc[direction]
 
                if 0 <= nr < N and 0 <= nc < N:
                    if nums[row][col] + 1 == nums[nr][nc]:
                        visited[nums[row][col]] = 1
 
 
    # visited 끝에서부터 순회
    # 0을 만나면 초기화 후 continue
    # 쌓인 cnt가 있다면
    # 시작 위치는 0을 만난 인덱스 + 1
    # 방의 개수 = cnt + 1
    cnt = 0
    room = []
    for idx in range(len(visited)-1, -1, -1):
        if not visited[idx]:
            if cnt:
                room_start = idx + 1
                room_cnt = cnt + 1
                room.append([room_start, room_cnt])
                cnt = 0
            continue
 
        cnt += 1
 
    room.sort(key=lambda x : (-x[1], x[0]))
 
    print('#{}'.format(tc), *room[0])
'''










