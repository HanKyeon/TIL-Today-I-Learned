'''
중앙값 구하기

어떤 수열을 읽고, 홀수번째 수를 읽을 때마다 지금까지 입력받은 값의 중앙값을 출력하는 프로그램 작성.
1,5,4,3,2라면 1,3,5번째 수에 1 4 3 출력하면 된다.

입력
테케 갯수 T
각 테케 수열 크기 수열 원소 차례 제시. 한 줄에 10개씩, 32비트 부호있는 정수.

출력
출력하는 중앙값 갯수, 홀수번째 수를 읽을 때마다 구한 중앙값을 공백 구분 출력. 한 줄에 10개씩 출력.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    print(m//2+1 if m%2 else m//2)
    ans = []
    lheap, rheap = [], [] # 좌측은 최대힙, 우측은 최소힙
    while m>0:
        g = list(map(int, input().rstrip().split()))
        for i in range(len(g)):
            if not rheap:
                heappush(rheap, g[i])
                ans.append(g[i])
                continue
            if rheap[0] >= g[i]:
                heappush(lheap, -g[i])
            elif rheap[0] < g[i]:
                heappush(rheap, g[i])
                heappush(lheap, -heappop(rheap))
            while len(lheap) > len(rheap):
                heappush(rheap, -heappop(lheap))
            if not i%2:
                ans.append(rheap[0])
                if len(ans) == 10:
                    print(*ans)
                    ans = []
        m-=10
    if ans:
        print(*ans)

















