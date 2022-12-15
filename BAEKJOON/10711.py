'''
모래성

명우와 친구들 놀러 갈 것.
모래성을 쌓을 것이다.
2차원 격자 단위, 격자마다 튼튼함의 정도가 다르다.
튼튼함은 1~9 사이 숫자로 표현, 자기 격자 주변 8방향을 확인하여 모래성이 쌓여있지 않은 부분의 갯수가 자기 모래성의 튼튼함보다 많거나 같은 경우 파도에 의해 무너질 수 있다.
이 외의 경우느 파도가 쳐도 무너지지 않는다.
모래성이 무너진 경우, 그 격자는 모래성이 쌓여있지 않은 것으로 취급.
모래성은 파도 1회 당 특정 부분이 무너져 내리는 방식으로 모양이 변화.
모래성의 모양이 변하지 않으려면 파도가 몇 번 쳐야 하나?

입력
모래성 n, m  제시. 1이상 1000이하.
n개 줄 m개 문자 그래프 제시.
1~9 사이 숫자 혹은 .
1~9는 모래 강도, .은 모래가 없다.

출력
몇 번의 파도가 몰려오고 나서야 모래성의 상태가 수렴하는가?
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def check():
    global n, m
    ret = set()
    for i in range(n):
        for j in range(m):
            if dp[i][j] >= g[i][j]>0:
                ret.add((i, j))
    return ret

def ing(pli):
    global n, m
    li = set()
    while pli:
        h, w = pli.pop()
        g[h][w] = 0
        li.add((h, w))
    ret = set()
    while li:
        h, w = li.pop()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m:
                dp[nh][nw] += 1
                if dp[nh][nw] >= g[nh][nw] > 0:
                    ret.add((nh, nw))
    return ret

n, m = map(int, input().rstrip().split())
g = []
dp = [[0]*m for _ in range(n)]
numz = []
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == '.':
            s[j] = 0
            for dh, dw in mov:
                nh, nw = i+dh, j+dw
                if 0<=nh<n and 0<=nw<m:
                    dp[nh][nw] += 1
        else:
            s[j] = int(s[j])
    g.append(s)

oli = check()
cnt = 0
if oli:
    while oli:
        cnt += 1
        oli = ing(oli)
    print(cnt)
else:
    print(-1)

'''
# 빠른 코드

R, C = map(int, input().split())
origin = [list(map(lambda x: int(x) if x!='.' else 0, input())) for _ in range(R)]
board = [[v for v in row] for row in origin]

q = []
for r in range(R):
    for c in range(C):
        if origin[r][c] == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0<= nc < C:
                        if board[nr][nc] > 0:
                            board[nr][nc] -= 1
                            if board[nr][nc] == 0:
                                q.append((nr, nc))

cnt = 0
while len(q):
    nq = []
    for r, c in q:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = r+dr, c+dc
                if board[nr][nc] > 0:
                    board[nr][nc] -= 1
                    if board[nr][nc] == 0:
                        nq.append((nr, nc))
    q = nq
    cnt += 1
print(cnt)
'''


