'''
N과 M 8

N개 자연수 중 M개를 고른 수열
같은 수르 여러번 골라도 된다.
고른 수열은 비내림차순이어야 한다. - a1<=a2<=a3... 를 만족하면 비내림차순이다.

입력
n, m 제시.
n개 수 제시. 1만 이하 자연수

출력
한 줄에 하나씩 만족하는 수열 출력. 중복 수열 다수 출력 금지, 공백 구분 출력. 사전 순으로 증가하는 순서
'''
import sys
input = sys.stdin.readline

def dfs(idx):
    global m
    if len(stk) == m:
        print(*stk)
        return
    for i in range(idx, n):
        stk.append(nl[i])
        dfs(i)
        stk.pop()

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
nl.sort()
stk = []
for i in range(n):
    stk.append(nl[i])
    dfs(i)
    stk.pop()


