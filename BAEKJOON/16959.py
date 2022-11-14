'''
n*n 체스판. 1부터 n**2까지의 정수.
나이트, 숍, 룩.
1 있는 칸부터 시작. 1,2,3... 순서로 이동해야 한다.
1에 나/비/룩 중 하나 놓기. 이동시켜서 2가 적힌 칸으로 이동.
1에서 2로 이동 시킬 때 다른 수가 적힌 칸을 방문 가능. 1회만에 방문이 아니어도 된다는 뜻 같음.
1초에 할 수 있는 행동은
말을 이동시키거나
다른 말로 바꾸거나.
n**2까지 도착하는데 걸리는 시간의 최솟값

입력
n
체스판

출력
1,2,3... 방문하는데 필요한 시간 최솟값.
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# 0은 나이트 행마, 1은 비숍 행마, 2는 룩 행마
mov = [[(-2, 1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)], [], []]
g = []
di = {}
for i in range(n):
    mov[1].append((i,i))
    mov[1].append((i,-i))
    mov[1].append((-i,-i))
    mov[1].append((-i,i))
    mov[2].append((0, i))
    mov[2].append((i, 0))
    mov[2].append((-i, 0))
    mov[2].append((0, -i))
    s = list(map(int, input().rstrip().split()))
    for j in range(n):
        di[s[j]] = (i, j)
        di[(i, j)] = s[j]
        if s[j] == 1:
            sh, sw = i, j
    g.append(s)

v = [[[[0,0,0] for _ in range(n)] for _ in range(n)] for _ in range(n**2)] # [몇개 밟았는지][h][w][말 종류]
def bfs():
    global n, sh, sw
    n2 = n**2
    q = deque([(sh, sw, 0, 0),(sh, sw, 1, 0),(sh, sw, 2, 0)]) # h, w, 행마 종류, 몇개 먹었는지
    v[0][sh][sw] = [1,1,1]
    while q:
        h, w, che, cnt = q.popleft()
        for dh, dw in mov[che]:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n:
                if g[nh][nw] == cnt+2 and not v[cnt+1][nh][nw][che]:
                    if g[nh][nw] == n2:
                        return v[cnt][h][w][che]
                    v[cnt+1][nh][nw][che] = v[cnt][h][w][che]+1
                    q.append((nh, nw, che, cnt+1))
                elif not v[cnt][nh][nw][che]:
                    v[cnt][nh][nw][che] = v[cnt][h][w][che]+1
                    q.append((nh, nw, che, cnt))
        for i in range(3):
            if i == che:
                continue
            else:
                if not v[cnt][h][w][i]:
                    v[cnt][h][w][i] = v[cnt][h][w][che]+1
                    q.append((h,w,i,cnt))

print(bfs())





