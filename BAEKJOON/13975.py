'''
파일 합치기 3

두개의 파일을 합쳐서 하나의 임시 파일을 만들고, 임시파일이나 원래 파일을 계속 두개씩 합쳐서 파일을 합쳐 나가 최종적으로 하나의 파일로 합친다.
두개의 파일을 합칠 때 필요한 비용이 두 파일 크기의 합이다.
파일들을 하나의 파일로 합칠 때 필요한 최소 비용을 계산하는 프로그램을 작성하시오.

입력
테케 T 제시
각 테케는 두개의 행.
양정수k 제시
1장부터 k장까지 수록한 파일의 크기를 나타내는 양의 정수 k개 제시. 파일 크기 10000이하.

출력
각 테케마다 모든 장을 합치는데 필요한 최소 비용 출력
'''
import sys
from heapq import heappop, heappush, heapify
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    heap, ans = list(map(int, input().rstrip().split())), 0
    heapify(heap)
    while len(heap) > 1:
        a = heappop(heap) + heappop(heap)
        ans += a
        heappush(heap, a)
    print(ans)