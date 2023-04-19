'''
순회강연

n개 대학에서 강연 요청. d일 안에 와서 강연을 해주면 p를 지불.
가장 많은 돈을 벌 것임. 하루 한 곳만 가능.

입력
정수 n 제시.
각 대학에서 제시한 p, d 제시.

출력
최대로 벌 수 있는 돈
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

heap = []
maxd = 0
for _ in range(int(input())):
    p, d = map(int, input().rstrip().split())
    heappush(heap, (-d, -p))
    if maxd < d:
        maxd = d
nheap = []
ans = 0
while maxd:
    while heap and -heap[0][0] >= maxd:
        heappush(nheap, heappop(heap)[1])
    maxd -= 1
    if nheap:
        ans -= heappop(nheap)
    if not nheap and not heap:
        break
print(ans)






