'''
나이트의 이동

나이트가 움직여서 시작칸에서 도착 칸으로 이동을 최소 몇번만에 가능?

입력
테케T
체스판 한 변의 길이 4이상 300이하 l 좌표는 0,0~l-1,l-1
나이트 현재 칸
나이트 목표 칸

출력
나이트가 몇번만에 이동 가능한지 출력
'''
import sys
input = sys.stdin.readline

dh = [2, 2, -2, -2, 1, 1, -1, -1]
dw = [1, -1, 1, -1, 2, -2, 2, -2]
for _ in range(int(input())):
    l = int(input())
    g = [[0]*l for _ in range(l)]
    sta = list(map(int, input().split()))
    end = list(map(int, input().split()))
    li = [sta]
    g[sta[0]][sta[1]] = 1
    while li:
        h, w = li.pop(0)
        if [h,w] == end: # 여기서 조건을 걸어주고 찾자마자 끝내면 시간 초과가 나지 않는다.
            print(g[h][w]-1)
            break
        for i in range(8):
            nh, nw = h + dh[i], w + dw[i]
            if 0 <= nh < l and 0 <= nw < l and g[nh][nw] == 0:
                g[nh][nw] = g[h][w] + 1
                li.append((nh, nw))
# 실행을 다 하고 최종적으로 인덱싱해서 출력하려하면 파이썬으로 패스가 안된다.

'''
from collections import deque
import sys
input = sys.stdin.readline
pos = [(2,1),(1,2),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]

def bfs():
    L = int(input())
    sx, sy = map(int, input().split(" "))
    end = tuple(map(int, input().split(" ")))
    visited = [[False for _ in range(L)] for _ in range(L)]
    dq = deque()
    dq.append((sx,sy))
    visited[sx][sy] = True
    dept = -1
    while dq:
        dept+=1
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr == end:
                return dept
            for p in pos:
                x, y = curr[0]+p[0], curr[1]+p[1]
                if 0<=x<L and 0<=y<L and not visited[x][y]:
                    visited[x][y]=True
                    dq.append((x,y))
    return 0


for _ in range(int(input())):
    print(bfs())
'''