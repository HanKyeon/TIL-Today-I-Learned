'''
가운데를 말해요

백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
백준이 외치는 정수 갯수 n 제시. 1이상 10만이하 자연수.
n개 줄 정수 제시. -10000~10000

출력
n줄에 걸쳐 중간값 출력
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
lheap, rheap = [], []
heappush(lheap, -int(input()))
print(-lheap[0])
for _ in range(n-1):
    s = int(input())
    if -lheap[0] < s:
        heappush(rheap, s)
        if len(rheap) > len(lheap):
            heappush(lheap, -heappop(rheap))
    else:
        heappush(lheap, -s)
        if len(lheap) - len(rheap) == 2:
            heappush(rheap, -heappop(lheap))
    print(-lheap[0])










