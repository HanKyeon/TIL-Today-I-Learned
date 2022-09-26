'''
움직이는 미로 탈출

8*8 체스판 탈출해야 한다.
모든 칸은 빈 칸 또는 벽 중 하나.
좌하단에서 우상단 이동.
벽이 움직인다. 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 알 ㅐ행이 없다면 벽이 사라진다. 욱제 캐릭은 1초에 팔방으로 한 칸 이동하거나, 가만히 있을 수 있다. 빈칸으로만 이동 가능.
1초동안 욱제 캐릭 이동한 후 벽이 이동한다. 벽이 캐릭터 칸으로 이동하면 더 이상 캐릭터는 이동 할 수 없다.
캐릭터가 가장 우상단으로 이동 할 수 있는지 없는지 구해보자.

입력
8줄에 걸쳐 체스판 상태 제시.
.은 빈 칸 #은 벽

출력
도착 할 수 있으면 1, 없으면 0
'''
from collections import deque
import sys
input = sys.stdin.readline

dh = [1,1,1,0,0,-1,-1,-1, 0]
dw = [1,0,-1,1,-1,1,0,-1, 0]

def play1():
    global ans, q, g
    nq = deque()
    while q:
        bbq = q.popleft()
        h, w = bbq
        if g[h][w] == '#':
            continue
        if h == 0 and w == 7:
            ans = 1
            return ans
        for i in range(9):
            nh, nw = h+dh[i], w+dw[i]
            if 0<=nh<8 and 0<=nw<8 and g[nh][nw] == '.':
                nq.append((nh, nw))
    g.pop()
    g = [['.','.','.','.','.','.','.','.']]+g
    q = nq
    if not q:
        return True

g = [list(input().rstrip()) for _ in range(8)]
q = deque([(7, 0)])
ans = 0
while not ans:
    a = play1()
    if a:
        break
print(ans)

'''
# 빠름
import sys
input = sys.stdin.readline

def sol16954():
    walls = set()
    for i in range(8):
        line = input().rstrip()
        for j in range(8):
            if line[j] == '#':
                walls.add((i, j))
    directions = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (-1, 1), (0, -1), (-1, -1)]
    q = [(7, 0)]
    visited = [[0] * 8 for _ in range(8)]
    visited[7][0] = 1
    turn = 1
    while q:
        nq = []
        turn += 1
        for r, c in q:
            if (r, c) in walls:
                continue
            for d in range(9):
                nr, nc = r + directions[d][0], c + directions[d][1]
                if not (0 <= nr < 8 and 0 <= nc < 8):
                    continue
                if (nr, nc) in walls:
                    continue
                if visited[nr][nc] == turn:
                    continue
                if nr == 0 and nc == 7:
                    return 1
                visited[nr][nc] = turn
                nq.append((nr, nc))
        nwalls = set()
        for wr, wc in walls:
            if wr < 7:
                nwalls.add((wr + 1, wc))
        walls = nwalls
        q = nq
    return 0

if __name__ == '__main__':
    print(sol16954())
'''














