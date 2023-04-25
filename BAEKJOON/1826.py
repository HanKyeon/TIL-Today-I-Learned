'''
연료 채우기

1km에 1L 새나간다. 그냥 가다가 연료 다 빠짐. 정글 곳곳에 주유소 n개. 멈추는 횟수 최소화.
연료 이빠이 가능. 주유소 위치, 얻을 수 있는 연료의 양 제시. 멈추는 횟수 구해라.
정글 일직선 트럭 주유소 일직선 주유소 모두 성경이 기준 우측

입력
주유소 갯수 n 제시
n개 줄 주유소 정보 제시. a, b 제시 a는 시작 위치에서 주유소까지 거리, b는 그 주유소에서 채울 수 있는 연료량.
l, p 제시 l은 마을까지 거리, p는 있던 연료 량.

출력
주유소애서 멈추는 횟수 출력.
도착 못하면 -1
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
g = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    heappush(g, (a, b))
l, p = map(int, input().rstrip().split())
if p >= l:
    print(0)
    exit()

def dij():
    global l, p
    heap = []
    ret = 0
    while p < l:
        while g and  g[0][0] <= p:
            a, b = heappop(g)
            heappush(heap, (-b, a))
        if not heap:
            return -1
        b, a = heappop(heap)
        p += -b
        ret += 1
    return ret
print(dij())















