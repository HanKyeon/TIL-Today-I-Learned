'''
시니컬한 개구리

n*m 격자. 1,1 ~ n,m
격자의 값만큼 상하좌우로 뛴다.
근데 이번엔 밥 안먹음.
밥 안 먹고 한 번 자유자재로 뛴다.
개구리가 집에 가기 위한 최소 점프 횟수.

입력
n, m 제시.
sh, sw, eh, ew 제시. 시작 hw 도착hw임
n개 줄 격자 제시.

출력
최소 점프 횟수 출력. 집 못가면 -1 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

mov = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs():
    global n, m, eh, ew
    while q:
        h, w, cnt = q.popleft()
        d = g[h][w]
        if cnt and (h==eh or w==ew):
            return v[h][w]
        for dh, dw in mov:
            nh, nw = h+dh*d, w+dw*d
            if 0<=nh<n and 0<=nw<m and not v[nh][nw][cnt]:
                if nh==eh and nw==ew:
                    return v[h][w][cnt]
                v[nh][nw][cnt] = v[h][w][cnt]+1
                q.append((nh, nw, cnt))
            if cnt:
                for i in range(1, n if n > m else m):
                    nh, nw = h+dh*i, w+dw*i
                    if 0<=nh<n and 0<=nw<m:
                        if not v[nh][nw][0]:
                            v[nh][nw][0] = v[h][w][cnt]+1
                            q.append((nh, nw, 0))
                    else:
                        break
    return -1

n, m = map(int, input().rstrip().split())
sh, sw, eh, ew = map(lambda x: int(x)-1, input().rstrip().split())
if sh==eh and sw==ew:
    print(0)
    exit()
v = [[[0, 0]for _ in range(m)] for _ in range(n)]
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v[sh][sw][1] = 1
q = deque([(sh, sw, 1)])

print(bfs())

for i in v:
    print(i)
print(">>>>>>>>>")

'''
# 시간초과

def bfs():
    global n, m, eh, ew
    while q:
        h, w, cnt = q.popleft()
        d = g[h][w]
        if cnt and (h==eh or w==ew):
            return v[h][w]
        for dh, dw in mov:
            nh, nw = h+dh*d, w+dw*d
            if 0<=nh<n and 0<=nw<m and not v[nh][nw][cnt]:
                if nh==eh and nw==ew:
                    return v[h][w][cnt]
                v[nh][nw][cnt] = v[h][w][cnt]+1
                q.append((nh, nw, cnt))
            if cnt:
                for i in range(1, 1001):
                    nh, nw = h+dh*i, w+dw*i
                    if 0<=nh<n and 0<=nw<m:
                        if not v[nh][nw][0]:
                            v[nh][nw][0] = v[h][w][cnt]+1
                            q.append((nh, nw, 0))
                    else:
                        break
    return -1

'''











