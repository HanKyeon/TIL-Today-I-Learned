'''
치즈

사각형의 판. 빵꾸뚫린 치즈.
까생이는 치즈 없음. 공기와 접촉된 부분은 1시간에 녹음.
치즈 내의 공기가 공기와 만나면 그 부분들도 삭는다.

입력
가로 세로길이 양정수로 제시. 최대 100 100
치즈 없는 칸0 치즈 있는 칸 1 숫자 사이 빈 칸 제시.

출력
치즈가 모두 녹아 없어지는데 걸리는 시간.
모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여있는 칸의 갯수
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

def bfs1time(v, c): # bfs 한번만 하는 거다. 깊이를 정해서 큐에 넣고, 깊이가 정해져있다면 방문처리를 특수하게 바꿔도 될 듯 하다.
    global n, m
    q = deque()
    q.append((0, 0))
    while q:
        h, w = q.popleft()
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '0': # 0이면 탐색
                v[nh][nw] = 1
                q.append((nh, nw))
            elif 0<=nh<n and 0<=nw<m and v[nh][nw] == 0 and g[nh][nw] == '1': # 1이면 방문처리/0처리하고 큐에 넣지는 않는다.
                v[nh][nw] = 1
                g[nh][nw] = '0'
                c += 1
    return c

n, m = map(int, input().split())
g = [list(input().split()) for _ in range(n)]
hoxy = 0 # 혹시나 해서 치즈 갯수 세기
for i in g:
    hoxy += i.count('1')
if hoxy == 0: # 혹시 치즈 없으면
    print(0) # 시간 0이고
    print(0) # 치즈도 없다.
else:
    v = [[0]*m for _ in range(n)]
    cc = 0
    ans = [bfs1time(v, cc)] # 1차적으로 한 번 한 걸 담아준다.
    while ans[-1] != 0: # 바뀐 치즈가 없다면 끝낸다.
        v = [[0]*m for _ in range(n)]
        cc = 0
        ans.append(bfs1time(v, cc)) # 바뀐 치즈 갯수를 담는다.

    print(len(ans)-1)
    print(ans[-2])












'''
def bfs1time(stl):
    global n, m
    li = deque(stl)
    
    while li:
        x, y = li.popleft()
        g[x][y] -= 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 1:
                g[nx][ny] -= 1
            elif 0<=nx<n and 0<=ny<m and g[nx][ny] != 1:
                li.append((nx, ny))

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
startli = []
for i in range(n):
    startli.append((i, 0))
    startli.append((i, m-1))
for j in range(m):
    startli.append((0, j))
    startli.append((n-1, j))

for i in g:
    print(i)
bfs1time(startli)
for i in g:
    print(i)
'''
'''
1. 전치행렬 함께 뒤지며 01 10 있는거 바꾸기 -> 폐기. 중간 공기를 생각 못함.
2. bfs에 카운트 변수를 하나 받아서 count가 1이면 bfs를 실행하지 않기 (이전 방법과 다를게 있을까..?)
'''