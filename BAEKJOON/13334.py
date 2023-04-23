'''
철로

집과 사무실 통근하는 n명의 사람들. 수평선 상 서로 다른 점에 위치.
a, b 에 대해 a의 집 혹은 사무실 위치가 b의 집 혹은 사무실 위치와 같을 수 있다.
일직선 상의 어떤 두 점을 잇는 철로를 건설하여 기차를 운행. 제한된 예산, 철로 길이 d.
집과 사무실 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록 철로 선분을 정하고자 한다.
양정수 d와 n개 정수쌍 h,o 제시. h는 사람의 집 o는 사무실. 길이 d의 모든 선분 l에 대해 집과 사무실 위치가 모두 l에 포함되는 사람들의 최대 수를 구하는 프로그램 작성.

입력
양정수 n 제시.
n개 줄 h, o 제시. -1억 to 1억
철로 길이 d 제시

출력
길이 d의 임의의 선분에 대하여 집과 사무실 위치가 모두 그 선분에 포함되는 사람들의 최대 수를 한 줄에 출력
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

g = []
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    if a > b:
        a, b = b, a
    heappush(g, (b, a))
d = int(input())
heap = []
ans = 0
while g:
    b, a = heappop(g)
    if b-a > d:
        continue
    while heap and heap[0][0] < b-d:
        heappop(heap)
    heappush(heap, (a, b))
    if ans < len(heap):
        ans = len(heap)
print(ans)

'''
# 빠른 코드

import sys
import heapq

n = int(sys.stdin.readline())
houses = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    if start > end:  # 출발지와 도착지를 바꿔줌
        start, end = end, start
    houses.append((start, end))

d = int(sys.stdin.readline())
houses.sort(key=lambda x: x[1])  # 도착지 기준으로 오름차순 정렬

heap = []  # 출발지점을 저장할 최소힙
max_count = 0
for house in houses:
    start, end = house
    if end - start <= d:  # 선로 길이보다 짧은 집들만 골라서 최소힙에 추가
        heapq.heappush(heap, start)
        while heap and end - heap[0] > d:  # 선로 길이보다 큰 집은 최소힙에서 제거
            heapq.heappop(heap)
        max_count = max(max_count, len(heap))  # 최대 집의 개수 갱신

print(max_count)
'''











