'''
최소힙. 우선순위 큐로 뺀다는 것 같다.

1. 배열에 자연수 x를 넣는다.
2. 배열의 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

입력
연산의 갯수 1~10만 N 제시.
연산 정보. 0이라면 heappop(li), 자연수라면 heappush(li, val)

출력
0이 주어진 횟수만큼 답을 출력.
배열이 비어있는데 출력하라 하면 0 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    i = int(input().rstrip())
    if i:
        heappush(heap, i)
    elif not i and heap:
        print(heappop(heap))
    else:
        print(0)






