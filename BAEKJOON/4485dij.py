'''
녹색 옷 입은 애가 젤다지?

링크는 n*n 크기 동굴 0,0에 있다. n-1, n-1까지 이동해야 하는데 도둑 루피가 있는 곳을 지나면, 도둑 루피의 크기 만큼 소지금을 잃게 된다. 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야하며, 한 번에 상하좌우 인접한 곳으로 1칸 씩 이동 가능.
잃을 수 밖에 없는 최소 금액은?

입력
테케로 이루어짐. n이 0이면 끝.
n 제시
그래프 제시. 모든 칸에 도둑루피 존재.

출력
테케마다 정답 형식에 맞춰 출력.
Problem 1: 값
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

tc = 0
while True:
    tc+=1
    n = int(input())
    if not n:
        break
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]
    v[0][0] = 1
    heap = [(g[0][0], 0, 0)]
    while heap:
        val, h, w = heappop(heap)
        if h == n-1 and w == n-1:
            break
        for i in range(4):
            nh, nw = h + dh[i], w + dw[i]
            if 0<=nh<n and 0<=nw<n and not v[nh][nw]:
                v[nh][nw] = 1
                heappush(heap, (val+g[nh][nw], nh, nw))
    print(f"Problem {tc}: {val}")

















