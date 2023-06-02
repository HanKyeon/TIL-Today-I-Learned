'''
달리기

n*m 체육관. 사방 중 하나 고르고 최소 1, 최대 k칸 이동 가능.
시작점, 도착점 제시. 시작 to 도착 최소 시간.

입력
n, m, k 제시
n개 줄 그래프
.은 빈 칸 #은 벽
sh sw eh ew 제시

출력
최소 시간. 안되면 -1
'''

# 시간초과 난 코드. 왜 시간초과인지 모르겠음. 로직 상 똑같은데..
import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open("./BAEKJOON/input.txt")

mov = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs():
    global n, m, k, sh, sw, eh, ew
    q = deque([(sh, sw)])
    g[sh][sw] = 1
    while q:
        h, w = q.popleft()
        for dh, dw in mov:
            nh, nw = h, w
            for _ in range(k):
                nh, nw = nh+dh, nw+dw
                if 0<=nh<n and 0<=nw<m and g[nh][nw] > g[h][w]:
                    if nh==eh and nw==ew:
                        return g[h][w]
                    g[nh][nw] = g[h][w]+1
                    q.append((nh, nw))
                else: break
    return -1

n, m, k = map(int, input().rstrip().split())
g = [[] for _ in range(n)]
for i in range(n):
    s = input().rstrip()
    for j in s:
        if j == ".":
            g[i].append(1111111)
        else:
            g[i].append(0)
sh, sw, eh, ew = map(lambda x: int(x)-1, input().rstrip().split())
print(bfs())


import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())

v = [[1111111]* (M) for _ in range(N)]
dh = [-1,0,1,0]
dw = [0,-1,0,1]
g = []
for i in range(N):
    text = list(input().rstrip())
    g.append(list(text))
sh,sw,eh,ew = map(lambda x: int(x)-1,input().split())
q = deque([(sh,sw)])
v[sh][sw] = 0
while q:
    h,w= q.popleft()
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        cnt = 1
        while cnt<=K and 0<=nh<N and 0<=nw<M and g[nh][nw]!='#' and v[nh][nw]>v[h][w]:
            if v[nh][nw] == 1111111:
                q.append((nh,nw))
                v[nh][nw] = v[h][w] + 1
            nh += dh[i]
            nw += dw[i]
            cnt += 1
if v[eh][ew] == 1111111:
    print(-1)
else:
    print(v[eh][ew])

'''
3 3 3
..#
..#
#..
1 1 3 3
답 3

3 3 3
..#
..#
#..
3 3 1 1
답 3
'''

