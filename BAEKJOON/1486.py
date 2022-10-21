'''
등산

가려는 산의 지도 제시. i, j의 높이가 g[i][j]이다.
A-25일 경우 0~25, a~z일경우 26~51
호텔은 0,0에 존재. 인접한 좌표 중 높이 차이가 T보다 크지 않은 곳으로만 다닐 수 있다.
낮거나 같은 곳 이동에는 1초
높은 곳 이동에는 높이 차의 제곱.
산의 지도 T, 어두워지는 시간 D가 주어졌을 때, 세준이가 D보다 크지 않은 시간 동안 올라갈 수 있는 최대 높이를 구하는 프로그램 작성.

입력
n, m t, d 제시. 세로n 가로m, 가능한 높이차 t, 어두워지는 시간 d
지도 제시

출력
세준이가 갈 수 있는 가장 높은 곳의 높이를 출력한다.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

mov = [(-1,0), (0,1), (1,0), (0,-1)]

def grph():
    global n, m, bgg
    for _ in range(n):
        s = list(input().rstrip())
        for i in range(m):
            a = ord(s[i])
            if a >= 97:
                a -= 71 # 97-25
                s[i] = a
                if a > bgg:
                    bgg = a
            else:
                a -= 65
                s[i] = a
                if a > bgg:
                    bgg = a
        g.append(s)

def dij():
    global n, m, t, d, bgg
    ret = g[0][0]
    if ret == bgg:
        return ret
    vst = [[int(10e9)]*m for _ in range(n)]
    vst[0][0] = 0
    heap = [(0, 0, 0)] # time, now, h, w
    while heap:
        cost, h, w = heappop(heap)
        if vst[h][w] < cost:
            continue
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if nh<0 or nh>=n or nw<0 or nw>=m: # 범위 제한
                continue
            cha = g[nh][nw] - g[h][w]
            if cha < -t or cha > t: # 높이 차이 제한
                continue
            if cha > 0 and cost+cha**2 <=d and cost+cha**2 < vst[nh][nw]:
                vst[nh][nw] = cost+cha**2
                heappush(heap, (cost+cha**2, nh, nw))
            elif cha <= 0 and cost+1 <= d and cost+1 < vst[nh][nw]:
                vst[nh][nw] = cost+1
                heappush(heap, (cost+1, nh, nw))
    heap = [(0, 0, 0)]
    dp = [[int(10e9)]*m for _ in range(n)]
    dp[0][0] = 0
    while heap:
        val, h, w = heappop(heap)
        if val > dp[h][w]:
            continue
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if nh<0 or nh>=n or nw<0 or nw>=m: # 범위 제한
                continue
            cha = g[nh][nw] - g[h][w]
            if cha < -t or cha > t: # 높이 차이 제한
                continue
            if cha >= 0 and dp[nh][nw] > val+1:
                dp[nh][nw] = val+1
                heappush(heap, (val+1, nh, nw))
            elif cha < 0 and dp[nh][nw] > val+cha**2:
                dp[nh][nw] = val+cha**2
                heappush(heap, (val+cha**2, nh, nw))
    for i in range(n):
        for j in range(m):
            if vst[i][j] + dp[i][j] <= d:
                ret = max(g[i][j], ret)
    return ret

n, m, t, d = map(int, input().rstrip().split())
bgg = 0
g = []
grph()
print(dij())










'''
def dij():
    global n, m, t, d, bgg
    ret = g[0][0]
    if ret == bgg:
        return ret
    vst = [[int(10e9)]*m for _ in range(n)]
    vst[0][0] = 0
    heap = [(0, 0, 0, 0)] # time, back, h, w
    while heap:
        cost, bcost, h, w = heappop(heap)
        if vst[h][w] < cost:
            continue
        if g[h][w] > ret:
            ret = g[h][w]
        if ret == bgg:
            for i in vst:
                print(i)
            return ret
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if nh<0 or nh>=n or nw<0 or nw>=m: # 범위 제한
                continue
            cha = g[nh][nw] - g[h][w]
            if cha < -t or cha > t: # 높이 차이 제한
                continue
            if cha > 0 and cost+cha**2+bcost+1 <= d and cost+cha**2 < vst[nh][nw]:
                vst[nh][nw] = cost+cha**2
                heappush(heap, (cost+cha**2, bcost+1, nh, nw))
            elif cha <= 0 and cost+1+bcost+cha**2 <= d and cost+1 < vst[nh][nw]:
                vst[nh][nw] = cost+1
                heappush(heap, (cost+1, bcost+cha**2, nh, nw))
    for i in vst:
        print(i)
    return ret
'''













# print(ord('A')) # 65
# print(ord('Z')) # 90
# print(ord('a')) # 97
# print(ord('z')) # 122