'''
미로 만들기

n*n 격자 방.
검은방/흰방 존재. 검은 방은 진입 불가. 흰 방 사이 이동 가능. 시작 방은 흰 방, 도착 방 흰 방.
시작 방에서 끝 방으로 가야하는데, 되도록 적은 수의 방 색을 바꾸고 싶다.
검은 방에서 흰 방으로 바꿔야 할 최소의 수를 구하는 프로그램 작성.

입력
방의 수 n 제시.
수열 제시. 0은 벽 1은 통로

출력
흰 방으로 바꿔야 할 최소 검은 방의 수 출력
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
v = [[int(10e9)]*n for _ in range(n)]
heap = [(0, 0, 0)]
v[0][0] = 0
while heap:
    cost, h, w = heappop(heap)
    if h == n-1 and w == n-1:
        break
    if cost > v[h][w]:
        continue
    for i in range(4):
        nh, nw = h+dh[i], w+dw[i]
        if 0<=nh<n and 0<=nw<n and v[nh][nw] > cost:
            if g[nh][nw] == '1':
                v[nh][nw] = cost
                heappush(heap, (cost, nh, nw))
            else:
                if v[nh][nw] > cost+1:
                    v[nh][nw] = cost+1
                    heappush(heap, (cost+1, nh, nw))
print(cost)





