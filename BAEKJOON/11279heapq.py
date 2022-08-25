'''
최대 힙
1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

입력
연산갯수 1~10만.
연산 정보.
자연수면 heappush 0이면 heappop

출력
0이 주어질 때마다 출력.
빈 상태로 출력하라고 하면 0출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

heap = []
for _ in range(int(input().rstrip())):
    i = int(input().rstrip())
    if i:
        heappush(heap, -i)
    elif not i and heap:
        print(-heappop(heap))
    elif not i and not heap:
        print(0)





