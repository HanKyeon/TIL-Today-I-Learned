'''
소문난 칠공주

총 25명의 여학생 반. 이다솜파 임도연 파.
칠공주는 7명의 여학생들로 구성. 가로나 세로로 인접해야함. 이다솜파로만 구성 될 필요는 없음. 이다솜파가 우위를 점해야 함. 4명 이상의 이다솜파.
소문난 칠공주를 결성 할 수 있는 모든 경우의 수를 구해라.

입력
S 이다솜파 Y임도연파 5*5 행렬 5개줄 제시.

출력
소문난 칠공주 결성 가능한 모든 경우의 수 출력.
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(h, w):
    v = set(combi[:])
    v.remove(h*5+w)
    ycnt = 1 if g[h][w] == "Y" else 0
    q = deque([(h, w)])
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<5 and 0<=nw<5:
                if nh*5+nw not in v:
                    continue
                q.append((nh, nw))
                v.remove(nh*5+nw)
                if g[nh][nw] == "Y":
                    ycnt += 1
                    if ycnt > 3:
                        return False
    return False if v else True

mov = [(-1,0),(0,1),(1,0),(0,-1)]
g = [list(input().rstrip()) for _ in range(5)]
ans = 0
comb = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
for combi in combinations(comb, 7):
    ih, iw = combi[0]//5, combi[0]%5
    if bfs(ih, iw):
        ans += 1
print(ans)



'''
# 빠른 코드

import sys


def move(x, y):
    dirs = []
    if x + 1 < 5:
        dirs.append((x + 1, y))
    if x - 1 >= 0:
        dirs.append((x - 1, y))
    if y + 1 < 5:
        dirs.append((x, y + 1))
    if y - 1 >= 0:
        dirs.append((x, y - 1))
    return dirs


def back_tracking(N, board, visited, route, S, path, found):
    if N == 0:
        if S >= 4:
            ans = tuple(sorted(path))
            if ans not in found:
                found.add(ans)
        return

    for i, (x, y) in enumerate(route):
        if visited[y][x]:
            continue

        visited[y][x] = True
        path.append(y * 5 + x)
        back_tracking(N - 1, board, visited, route[i + 1:] + move(x, y), S + (board[y][x] == "S"), path, found)
        visited[y][x] = False
        path.pop()


def solution(board):
    visited = [[False] * 5 for _ in range(5)]
    cnt = 0
    for y in range(5):
        for x in range(5):
            found = set()
            back_tracking(7, board, visited, [(x, y)], 0, [], found)
            cnt += len(found)
            visited[y][x] = True
    return cnt


IBoard = [sys.stdin.readline().rstrip() for _ in range(5)]
print(solution(IBoard))
'''
