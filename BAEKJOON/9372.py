'''
상근이의 여행

n개국 여행. 최대한 적은 종류의 비행기로 모든 국가 여행 가능하게. 다른 국가 거쳐가도 됨.

입력
테케t
n, m 제시. 국가수 뱅기 종류.
m개 줄 a,b쌍. a와 b를 왕복하는 비행기가 있다는 것.

출력
테케마다 비행기 최소 갯수 출력.
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    for _ in range(m):
        a = input()
    print(n-1)



