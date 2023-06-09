'''
n과 m 7

n개 자연수 중 m개 고른 수열
같은 수 여러번 골라도 됨

입력
n과 m 제시
1줄 n개 수 제시

출력
만족되는 수열 출력. 중복수열 여러번 출력 x  공백 구분 출력, 사전순 증가
'''
def rec(cnt):
    global m
    if cnt == m:
        print(*ans)
        return
    for i in nl:
        ans.append(i)
        rec(cnt+1)
        ans.pop()

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
nl.sort()
ans = []
for i in nl:
    ans.append(i)
    rec(1)
    ans.pop()

'''
# 빠른 코드

import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

print('\n'.join(list(map(' '.join, product(map(str, arr), repeat=M)))))
'''
