'''
소수의 곱

K개의 소수. 곱해서 얻게 되는 수 존재. 소수들을 선택 할 때는 같은 수 선택 가능, 주어지는 소수 자체도 포함.
2 5 7이라면 2 4 5 7 8 10 14 16 20 25 28 32 35
k개의 소수가 주어졌을 때, 소수 곱들 중 n번째 수를 구하라

입력
k, n 제시
k개의 소수 오름차순 제시
같은 소수 여러번 제시 x, 주어지는 소ㅜ는 541 아래 자연수
'''
import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
heap = nl[:]
heapify(heap)
while n:
    ans = heappop(heap)
    for i in nl:
        nod = i*ans
        heappush(heap, nod)
        # print(f"{n}번째 수는 {ans}이고, 들어가는 수는 {nod}, 곱하는 수는 {i}")
        if not ans%i:
            break
    n-=1
print(ans)

