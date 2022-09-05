'''
나무 재테크

n*n 배열
r, c로 하고 1부터 시작.
초기 양분은 모든 칸에 5

봄 : 나무가 자기 나이만큼 양분 흡수, 나이 1 증가 각 자리만 가능. 하나의 칸에 여러나무가 있다면 어린놈부터. 땅에 양분이 부족해 자기 나이만큼 양분을못먹으면 즉사.
여름 : 죽은 나무가 양분이 된다. 죽은 나무 나이 // 2 만큼 양분으로 추가.
가을 : 나무 번식. 나무 나이가 5배수여야 번식 가능하며, 인접 8칸에 나이가 1인 나무가 생긴다. 땅 벗어나면 안생김.
겨울 : 기계가 땅에 양분 추가. 각 칸에 A[r][c]. 입력으로 제시.
k년 후 상도 땅에 살아있는 나무 갯수는?

입력
n, m, k 제시
n개 줄에 A배열 제시. r번째 c번째 값은 A[r][c]
m개 줄에 나무 정보 x, y, z 제시. 나무위치 x,y 나이 z
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

dh = [1, 1, 1, 0, 0, -1, -1, -1]
dw = [1, 0, -1, 1, -1, 1, 0, -1]

def bomyeoreum():
    global namu, g, A, yb
    namus = []
    ybs = []
    nope = set()
    while namu:
        ne, h, w = heappop(namu)
        yab = yb[h][w]
        if not (h, w) in nope and ne <= yab:
            yb[h][w] -= ne
            nope.add((h, w))
            heappush(namus, (ne+1, h, w))
        elif ne > yab:
            ybs.append((h, w, ne//2))
    namu = namus[:]
    while ybs:
        h, w, ybz = ybs.pop()
        yb[h][w] += ybz

def gaeul():
    global namu, g, A, n
    namus = []
    while namu:
        ne, h, w = heappop(namu)
        heappush(namus, (ne, h, w))
        if ne % 5 == 0:
            for j in range(8):
                nh, nw = h + dh[j], w + dw[j]
                if 0<=nh<n and 0<=nw<n:
                    heappush(namus, (1, nh, nw))
    namu = namus[:]

def gyeoul():
    for i in range(n):
        for j in range(n):
            yb[i][j] += A[i][j]

n, m, k = map(int, input().split()) # A배열은 n
yb = [[5]*n for _ in range(n)]
# g = [[0]*n for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]
namu = []
for _ in range(m):
    a, b, c = map(int, input().split())
    # g[a-1][b-1] = c
    heappush(namu, (c, a-1, b-1))

for _ in range(k):
    bomyeoreum()
    gaeul()
    gyeoul()
print(len(namu))



'''
# 힙 시간 초과 ㅗㅗ

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

dh = [1, 1, 1, 0, 0, -1, -1, -1]
dw = [1, 0, -1, 1, -1, 1, 0, -1]

def bomyeoreum():
    global namu, g, A, yb
    namus = []
    ybs = []
    nope = set()
    while namu:
        ne, h, w = heappop(namu)
        yab = yb[h][w]
        if not (h, w) in nope and ne <= yab:
            yb[h][w] -= ne
            nope.add((h, w))
            heappush(namus, (ne+1, h, w))
        elif ne > yab:
            ybs.append((h, w, ne//2))
    namu = namus[:]
    while ybs:
        h, w, ybz = ybs.pop()
        yb[h][w] += ybz

def gaeul():
    global namu, g, A, n
    namus = []
    while namu:
        ne, h, w = heappop(namu)
        heappush(namus, (ne, h, w))
        if ne % 5 == 0:
            for j in range(8):
                nh, nw = h + dh[j], w + dw[j]
                if 0<=nh<n and 0<=nw<n:
                    heappush(namus, (1, nh, nw))
    namu = namus[:]

def gyeoul():
    for i in range(n):
        for j in range(n):
            yb[i][j] += A[i][j]

n, m, k = map(int, input().split()) # A배열은 n
yb = [[5]*n for _ in range(n)]
# g = [[0]*n for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]
namu = []
for _ in range(m):
    a, b, c = map(int, input().split())
    # g[a-1][b-1] = c
    heappush(namu, (c, a-1, b-1))

for _ in range(k):
    bomyeoreum()
    gaeul()
    gyeoul()
print(len(namu))
'''

'''
from collections import deque

n, m, k = map(int, input().split(' '))

a = [list(map(int, input().split(' '))) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split(' '))
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def spring_summer():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if graph[i][j] < trees[i][j][k]:
                    for _ in range(k, len(trees[i][j])):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                else:
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2


def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)

            graph[i][j] += a[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)
'''