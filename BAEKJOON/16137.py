'''
견우와 직녀

견우와 직녀는 여러 섬과 절벽으로 이루어진 지역에 살고 있다. 격자로 나타낼 수 있으며, 상하좌우로 인접한 칸으로 가는데 1분 걸린다.
7.7 오작교날. 고령화로 인해 까마귀랑 까치가 일부 절벽에만 다리를 만들어준다. 몇 분 주기로 짓고 해체한다. 한 번 지은 오작교는 1분만 유지된다.
두 번 연속 오작교 건너기X
절벽을 정확히 하나 골라 주기가 M분인 오작교를 하나 더 놓아주기로 했다.
이미 짓기로 예정한 절벽에는 오작교를 하나 더 놓을 수 없고, 아래와같이 절벽이 가로 세로로 교차해서 놓을 수 없는 위치도 있다.
견우가 직녀에게 도착 할 수 있는 최소 시간.

입력
n, m 제시. m은 오작교 주기 m이다.
n개 줄 그래프 제시.
1은 이동 가능한 땅,
0은 절벽,
2이상의 수는 적혀있는 수 만큼의 주기를 가지는 오작교.
견우의 시작점은 0,0 직녀는 n-1,n-1. 출발 시간은 0분. 무조건 만날 수 있음.

출력
최소 시간 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def check(h, w):
    for dh, dw in [(1,1),(-1,1),(1,-1),(-1,-1)]:
        nh = h+dh
        nw = w+dw
        try:
            if g[nh][w]<1 and g[h][nw]<1:
                g[h][w] = -1
                return
        except:
            continue

def dij():
    global n, m
    heap = [(0, 0, 0, 1)]
    v[0][0][1] = 0 # 시작점
    while heap:
        cnt, h, w, fla = heappop(heap)
        if v[h][w][fla] < cnt:
            continue
        if h==n-1 and w==n-1: # 정답
            return cnt
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<n: # 범위 내
                if g[nh][nw] == 1 and v[nh][nw][fla] > cnt+1: # 길이고 시간이 덜 걸릴 때
                    v[nh][nw][fla] = cnt+1
                    heappush(heap, (cnt+1, nh, nw, fla)) 
                elif g[nh][nw] > 1 and g[h][w] == 1: # 오작교이고 이전이 길 일 때
                    a = cnt + (g[nh][nw]-cnt%g[nh][nw]) # 다음 불 켜지는 때
                    if v[nh][nw][fla] > a:
                        v[nh][nw][fla] = a
                        heappush(heap, (a, nh, nw, fla))
                elif fla and not g[nh][nw] and g[h][w] == 1: # 임의 오작교 안썼고 뚫을거고 이전이 길 일 때
                    a = cnt+(m-cnt%m) # 다음 불 켜지는 때
                    if v[nh][nw][0] > a:
                        v[nh][nw][0] = a
                        heappush(heap, (a, nh, nw, 0))

mov = [(-1,0),(0,1),(1,0),(0,-1)]
n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[[20000, 20000] for _ in range(n)] for _ in range(n)] # 10*10에 다리 주기가 최대 20이므로 2000이 최대겠지만 2만으로.
for i in range(n):
    for j in range(n):
        if not g[i][j]:
            check(i, j) # 교차 확인
print(dij())






'''
            if 0<=nh<n and 0<=nw<n:
                if nh == n-1 and nw == n-1:
                    return v[h][w][cnt]+1
                if v[nh][nw][cnt] < 0:
                    if g[nh][nw] == 1:
                        heappush(heap, ())
                        heap.append((nh, nw, cnt))
                        v[nh][nw][cnt] = v[h][w][cnt]+1
                        continue
                    elif g[nh][nw] > 1:
                        if g[h][w] > 1:
                            continue
                        heap.append((nh, nw, cnt))
                        v[nh][nw][cnt] = v[h][w][cnt] + (g[nh][nw]-v[h][w][cnt]%g[nh][nw])
                elif cnt and  v[nh][nw][cnt-1]
                if not g[nh][nw] and cnt and v[nh][nw][cnt-1]<0 and g[h][w] == 1:
                    heap.append((nh, nw, cnt-1))
                    v[nh][nw][0] = v[h][w] + (m - v[h][w][cnt]%m)
'''