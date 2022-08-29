'''
절댓값 힙

배열에 정수x를 넣는다.
배여렝서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 빈 배열에서 시작.

입력
연산의 갯수 1이상 10만이하 N 제시.

연산에 대한 정보 x. x가 0이 아니라면 배열에 x라는 값을 추가하는 연산이고,
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우. -2**31~2**31

출력
입력에서 0이 주어진 횟수만큼 답을 출력. 빈 배열인데 0이 나오면 0을 출력
'''
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
nl = []
for _ in range(n):
    i = int(input())
    if i == 0:
        if nl:
            print(heappop(nl)[1])
        elif not nl:
            print(0)
    else:
        heappush(nl, (i**2, i))




