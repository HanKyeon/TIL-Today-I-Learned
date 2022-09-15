'''
컵라면

N개의 문제. 컵라면 몇개 줄 것인지 제시.

동호가 받을 수 있는 최대 컵라면 수 구하기.
문제를 푸는데 단위시간 1. 데드라인은 N 이하 자연수. 각 문제를 풀 때 받을 수 있는 컵라면 수와 최대로 받을 수 있는 컵라면 수는 모두 2**31보다 작거나 같은 자연수.

입력
숙제 갯수 1이상20만이하n 제시.
문제에 대한 데드라인과 컵라면 수가 공백 제시.

출력
동호가 받을 수 있는 최대 컵라면 수.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    a, b = map(int, input().rstrip().split()) # a데드라인 풀면 b개의 컵라면.
    heappush(heap, (a, -b))

nd = []
ans = 0
while heap:
    dl, cup = heappop(heap)
    heappush(nd, -cup)
    ans += -cup
    while len(nd) > dl:
        ans -= heappop(nd)

print(ans)

'''
# 빠른 코드

import heapq
import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    deadline, cupNoodle = map(int, sys.stdin.readline().split())
    array.append((deadline, cupNoodle))

array.sort()

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
    
print(sum(queue))
'''

'''
# 시간 초과

n = int(input())
heap = []
for i in range(n):
    a, b = map(int, input().rstrip().split()) # a데드라인 풀면 b개의 컵라면.
    heappush(heap, (-b, a))

v = []
ans = 0
while heap:
    cup, nod = heappop(heap)
    while nod != 0:
        if v[nod] == 1:
            nod -= 1
            continue
        else:
            break
    if nod == 0:
        continue
    v[nod] = 1
    ans += cup

print(-ans)
'''



















