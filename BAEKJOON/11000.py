'''
강의실 배정

s에 시작해서 t에 끝나는 수업 n개 제시. 모든 수업이 가능하게 해야한다.
최소 강의실 갯수 출력

입력
n 제시.
n개 줄 s, i 제시.

출력
강의실 갯수
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    heappush(heap, (s, e))
rh = [heappop(heap)[1]]
while heap:
    s, e = heappop(heap)
    if s < rh[0]:
        heappush(rh, e)
    else:
        heappop(rh)
        heappush(rh, e)

print(len(rh))





