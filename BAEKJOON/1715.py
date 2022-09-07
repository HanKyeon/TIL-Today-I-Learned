'''
카드 정렬하기

정렬된 두 묶음의 숫자 카드. 카드 수 A, B. 묶음을 합쳐 하나로 만들 때 A+B번 비교.
많은 숫자 카드 묶음. 두개씩 합쳐나가면 고르는 순서에 따라 비교 횟수가 매우 달라진다.
10장 20장 40장 묶음이 있다면 10 20, 30 40 순으로 합치면 최소이다.
최소한 몇 번의 비교가 필요한지?

입력
1이상 10만이하 n 제시.
n개줄에 걸쳐 숫자 카드 묶음의 각각 크기 제시. 1000이하 양정수

출력
최소 비교 횟수
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    heappush(heap, int(input()))
ans = 0
a, b = 0, 0
while heap:
    a = heappop(heap)
    if not heap:
        break
    b = heappop(heap)
    ans += a+b
    heappush(heap, a+b)
print(ans)
