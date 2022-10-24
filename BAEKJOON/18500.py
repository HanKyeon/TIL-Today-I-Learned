'''
미네랄 2

미네랄에 막대기 던지며 싸운다. 클러스터가 분리될 수도 있다. 새로 생성된 클러스터가 떠있는 경우 중력에 의해 하강한다. 떨어지는 동안 클러스터 모양은 변하지 않는다. 땅을 만나기 전까지 계속해서 떨어진다. 다른 클러스터 위에 떨어지면 합쳐진다.
왼쪽-오른쪽 순서로 높이에서 던진다. 모든 막대를 던지고 난 이후에 미네랄 모양을 구해라.

입력
n, m  제시.
n개 줄 m개 문자 제시. .은 빈 칸 x는 미네랄.
막대를 던진 횟수 k 제시.
막대를 던진 높이들 제시. 모든 높이는 1과 R 사이, 높이 1은 행렬의 가장 바닥, n은 가장 위.
공중에 떠 있는 미네랄 클러스터는 없으며, 두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다.

출력
입력 형식과 같은 형식으로 미네랄 모양을 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    global n, m
    v = [[0]*m for _ in range(n)]
    val = 0
    isl = {}
    root = set()
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.' or v[i][j]:
                continue
            val += 1
            q = deque([(i, j)])
            v[i][j] = val
            isl[val] = [(i, j)]
            while q:
                h, w = q.popleft()
                for dh, dw in mov:
                    nh, nw = h+dh, w+dw
                    if 0<=nh<n and 0<=nw<m and g[nh][nw] == 'x' and not v[nh][nw]:
                        v[nh][nw] = val
                        isl[val].append((nh, nw))
                        q.append((nh, nw))
                        if nh == n-1:
                            root.add(val)
    for i in isl:
        if i in root:
            continue
        fla = True
        for h, w in isl[i]:
            g[h][w] = '.'
        while fla:
            for j in range(len(isl[i])):
                h, w = isl[i][j]
                h += 1
                if h == n-1 or g[h+1][w] == 'x':
                    fla = False
                isl[i][j] = (h, w)
        for h, w in isl[i]:
            g[h][w] = 'x'

def attack():
    global n, m
    for i in range(len(hgt)):
        h = hgt[i]
        idx = -1
        if i%2:
            for j in range(m-1, -1, -1):
                if g[h][j] == 'x':
                    idx = j
                    break
            if idx >= 0:
                g[h][idx] = '.'
                bfs()
        else:
            for j in range(m):
                if g[h][j] == 'x':
                    idx = j
                    break
            if idx >= 0:
                g[h][idx] = '.'
                bfs()

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
qst = int(input())
hgt = list(map(lambda x: n-int(x), input().rstrip().split()))
attack()

for i in g:
    print(''.join(i))


