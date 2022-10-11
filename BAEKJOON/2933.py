'''
미네랄

동굴 소유권 분쟁중. 막대기를 서로 던져 결정. 동굴에는 미네랄이 있고, 막대기가 미네랄 깰 수 있다.
r, c로 표현, 각 칸은 미네랄 포함. 네 방향 중 하나로 인접한 미네랄이 포함된 두 칸은 클러스터.
창왼 상오. 막대기는 땅과 수평을 이루며 날아간다. 미네랄을 만나면 그 칸의 미네랄은 파괴, 막대기는 이동 정지.
미네랄 파괴 이후 남은 클러스터가 분리될 수 있다. 생성된 클러스터가 떠있는 경우 중력에 의해 낙하.
클러스터는 낙하 이후 합쳐진다.
모든 막대를 던진 후 미네랄 모양.

입력
n, m  제시.
n개 줄 m개 문자 . 빈칸 x 미네랄
막대 던진 횟수 qst 제시.
막대 던진 높이 제시. 공백 구분. 모든 높이는 1과 R 사이이며, 높이 1은 행렬 가장 바닥, n은 가장 위 의미.
첫 막대는 왼쪽에서 오른쪽, 다음은 오왼 순서로.
공중에 떠있는 미네랄 클러스터는 없으며 두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다.
클러스터가 떨어질 때 그 클러스터 각 열의 맨 아래 부분 중 하나가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다.

출력
입력 형식과 같은 형식으로 미네랄 모양을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

mov = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs_down():
    global n, m
    v = [[0]*m for _ in range(n)]
    val = 0
    isl = {}
    root = set()
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.' or v[i][j]:
                continue
            if not v[i][j] and g[i][j] == 'x':
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
                h+=1
                if h == n-1 or g[h+1][w] == 'x':
                    fla = False
                isl[i][j] = (h, w)
        for h, w in isl[i]:
            g[h][w] = 'x'

def attack():
    global n, m
    for i in range(len(hgt)):
        h = hgt[i]
        if i % 2:
            idx = -1
            for j in range(m-1, -1, -1):
                if g[h][j] == 'x':
                    idx = j
                    break
            if idx >= 0:
                g[h][idx] = '.'
                bfs_down()
        else:
            idx = -1
            for j in range(m):
                if g[h][j] == 'x':
                    idx = j
                    break
            if idx>=0:
                g[h][idx] = '.'
                bfs_down()

n, m = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
qst = int(input())
hgt = list(map(lambda x: n-x, map(int, input().rstrip().split())))
attack()

for i in g:
    print(''.join(i))




