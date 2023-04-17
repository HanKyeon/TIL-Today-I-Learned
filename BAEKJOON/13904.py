'''
과제

하루 한 과제. 마감일이 지난 과제는 점수 x
점수 가장 많이 받고 싶다. 얻을 수 있는 점수 최댓값.

입력
n
n개 줄 d, w 제시. 마감일까지 남은 일수, 점수
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

heap = []
maxd = 0
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    heappush(heap, [-a, -b])
    if maxd < a:
        maxd = a
        
ans = 0
nheap = []
while maxd:
    while heap and -heap[0][0] == maxd:
        a, b = heappop(heap)
        heappush(nheap, b)
    if nheap:
        ans -= heappop(nheap)
    maxd -= 1
    if not heap and not nheap:
        break
print(ans)



