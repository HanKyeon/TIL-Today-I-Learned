'''
수 정렬하기 2

입력
n 제시
n개 줄 n개 수 제시.
첫째 줄부터n개 줄에 오름차순 정렬 결과 출력.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heappush(heap, int(input()))
while heap:
    print(heappop(heap))







