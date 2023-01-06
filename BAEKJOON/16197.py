'''
두 동전

n*m 크기 보드, 4개 버튼. 보드 각 칸은 비어있더나 벽.
버튼은 상하좌우 4개. 동시에 두 동전이 이동.
동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
그 외의 경우는 이동하려는 방향으로 한 칸 이동한다.
이동하려는 칸에 동전이 있는 경우에도 한 칸 이동.
두 동전 중 하나만 보드에서 떨어뜨리기 위해 필요한 버튼 입력 횟수 최솟값

입력
n, m 제시.
n개 줄 보드 상태 o동전 .빈 칸 #벽

출력
최소 횟수 출력. 10번 이상 눌러야 하면 -1 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    """
    2초 512메가. 보드 크기가 꼴랑 20*20이 최대라 생각없이 짜도 될 듯
    """
    global cz, n, m
    v = set()
    cz.append(0)
    cz = tuple(cz)
    q = deque([cz])
    v.add(cz)
    while q:
        h1, w1, h2, w2, cnt = q.popleft()
        if cnt > 10:
            return -1
        for dh, dw in mov:
            nh1, nw1, nh2, nw2 = h1+dh, w1+dw, h2+dh, w2+dw
            c1f, c2f = 0<=nh1<n and 0<=nw1<m, 0<=nh2<n and 0<=nw2<m
            if c1f and c2f:
                if g[nh1][nw1]:
                    nh1, nw1 = h1, w1
                if g[nh2][nw2]:
                    nh2, nw2 = h2, w2
                if (nh1,nw1,nh2,nw2) in v:
                    continue
                q.append((nh1,nw1,nh2,nw2, cnt+1))
                v.add((nh1,nw1,nh2,nw2, cnt+1))
            elif (c1f and not c2f) or (c2f and not c1f):
                return cnt+1
    return -1

mov = [(-1,0),(0,1),(1,0),(0,-1)]

n, m = map(int, input().rstrip().split())
g, cz = [], []
for i in range(n):
    s = list(input().rstrip())
    for j in range(m):
        if s[j] == '.':
            s[j] = 0
        elif s[j] == '#':
            s[j] = 1
        elif s[j] == 'o':
            s[j] = 0
            cz.extend((i, j))
    g.append(s)

ans = bfs()
if ans > 10:
    ans = -1
print(ans)

'''
N, M = map(int, input().split())

board = []
coin_poses = []

for i in range(N):
    string = input()
    coin_pos = string.find('o')
    while coin_pos != -1:
        coin_poses.append((i, coin_pos))
        coin_pos = string.find('o', coin_pos + 1)
    string = string.replace('o', '.')
    board.append(string)

queue = [tuple(coin_poses)]

directions = ((1,0), (-1, 0), (0, 1), (0, -1))

def BFS():
    global queue
    count = 0
    while queue:
        new_queue = []
        count += 1
        if count > 10:
            break
        for items in queue:
            for direction in directions:
                poses = []
                for item in items:
                    poses.append([item[0], item[1]])
                dropped = 0
                for pos in poses:
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                    if 0 <= pos[0] < N and 0 <= pos[1] < M:
                        if board[pos[0]][pos[1]] == '#':
                            pos[0] -= direction[0]
                            pos[1] -= direction[1]
                    else:
                        dropped += 1
                if dropped == 2:
                    continue
                if dropped == 1:
                    return count
                if poses[0] == poses[1]:
                    continue
                new_queue.append((tuple(poses[0]), tuple(poses[1])))
        queue = list(set(new_queue))

    return -1
                
print(BFS())
'''

'''
20 20
####################
#o.................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#.................o#
####################
'''