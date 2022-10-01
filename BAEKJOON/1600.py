'''
말이 되고픈 원숭이

원숭이는 k번만 말처럼 이동 가능. 그 외에는 사방이동만 가능.
최소 동작으로 시작 지점에서 도착 지점까지 갈 수 있는 방법을 알아내라.

정수 k 제시.
가로m 세로n 제시.
0은 평지 1은 장애물 장애물 이동 불가. 시작점과 도착점은 항상 평지

출력
원숭이 동작 수의 최솟값 출력. 시작점에서 도착점까지 갈 수 없는 경우, -1 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

knt = [(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1),(1, -2),(-1, -2),(-2, -1)]
mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    global n, m, k
    if n==1 and m==1:
        return 0
    q = deque([(0, 0, k)])
    v[0][0][k] = 1
    while q:
        h, w, num = q.popleft()
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not g[nh][nw] and not v[nh][nw][num]:
                if nh==n-1 and nw == m-1:
                    return v[h][w][num] # 시작 방문이 1이라서 1 빼야함
                v[nh][nw][num] = v[h][w][num]+1
                q.append((nh, nw, num))
        if num > 0:
            for dh, dw in knt:
                nh, nw = h+dh, w+dw
                if 0<=nh<n and 0<=nw<m and not g[nh][nw] and not v[nh][nw][num-1]:
                    if nh==n-1 and nw == m-1:
                        return v[h][w][num]
                    v[nh][nw][num-1] = v[h][w][num]+1
                    q.append((nh, nw, num-1))
    return -1

k = int(input())
m, n = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 3차원 방문 배열 사용
v = [[[0]*31 for _ in range(m)] for _ in range(n)]
print(bfs())

'''
빠르다!

import sys
from collections import deque

k = int(sys.stdin.readline().strip())

width, height = map(int, sys.stdin.readline().strip().split(" "))

li = []

move0 = [0, 0, 1, -1]
move1 = [1, -1, 0, 0]
movehorse0 = [1, 1, -1, -1, 2, 2, -2, -2]
movehorse1 = [2, -2, 2, -2, 1, -1, 1, -1]

for i in range(height):
    li.append(list(map(int, sys.stdin.readline().strip().split(" "))))


def bfs():
    que = deque()
    que.append([0, 0, 0, k + 2])
    # [x좌표, y좌표, depth, k 의 사용수]
    # 좌표에 0과 1이 저장되어있기때문에 2부터 시작하여 계산.
    li[0][0] = k + 2
    check = False
    while True:
        if not que:
            return -1

        top = que.popleft()

        if top[0] == height-1 and top[1] == width-1:
            return top[2]

        for i in range(4):
            x = top[0] + move0[i]
            y = top[1] + move1[i]
            if 0 <= x < height and 0 <= y < width and li[x][y] != 1 and li[x][y] < top[3]:
                if x == height - 1 and y == width - 1:
                    que.appendleft([x, y, top[2] + 1, top[3]])
                    check = True
                    break
                li[x][y] = top[3]
                que.append([x, y, top[2] + 1, top[3]])

        if top[3] > 2 and not check:
            for i in range(8):
                x = top[0] + movehorse0[i]
                y = top[1] + movehorse1[i]

                if 0 <= x < height and 0 <= y < width and li[x][y] != 1 and li[x][y] < (top[3] - 1):
                    if x == height - 1 and y == width - 1:
                        que.appendleft([x, y, top[2] + 1, top[3] - 1])
                        break
                    li[x][y] = top[3] - 1
                    que.append([x, y, top[2] + 1, top[3] - 1])

print(bfs())
'''







