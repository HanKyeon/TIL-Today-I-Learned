'''
주난의 난

n*m 학교에서 날뛰기 시작. 주난이의 파동은 상하좌우 4방향 친구들을 쓰러뜨릴 때까지 한다. 1회 점프는 한 겹의 친구를 쓰러뜨린다.
주난이는 *로 표현. 초코바는 # 0은 빈 공간, 1은 친구가 어 있음.

한겹씩 부수고 탐색 부수고 탐색 하면 될듯?

입력
n, m 제시.
주난이 x1y1 범인 x2y2 제시.
이후 n*m크기 교실 정보. 1은 친구 *은 주난 #은 범인

출력
범인 잡으려면 몇 번 점프 해야 하는지
'''
# 힙 쓰면 되지 않을까?
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

mov = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dij():
    global n, m, x1, y1, x2, y2
    heap = [(0, x1-1, y1-1)]
    v[x1-1][y1-1] = 1
    while heap:
        cnt, h, w = heappop(heap)
        for dh, dw in mov:
            nh, nw = h+dh, w+dw
            if 0<=nh<n and 0<=nw<m and not v[nh][nw]:
                v[nh][nw] = 1
                if g[nh][nw] == '0':
                    heappush(heap, (cnt, nh, nw))
                elif g[nh][nw] == '#':
                    return cnt+1
                elif g[nh][nw] == '1':
                    heappush(heap, (cnt+1, nh, nw))

n, m = map(int, input().rstrip().split())
x1, y1, x2, y2 = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(n)]
v = [[0]*m for _ in range(n)]
print(dij())
