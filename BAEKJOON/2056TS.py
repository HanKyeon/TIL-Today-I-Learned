'''
작업

수행해야 할 작업 n개. 걸리는 시간은 1이상 100이하 정수
선행관계 존재.
k번 작업에 대해 선행 관계에 있는 작업들의 번호는 모두 k-1이하이다. 선행관계가 없는 작업이 하나 이상 존재.
모든 작업을 완료하기 위해 필요한 최소 시간.

입력
첫째 줄에 n 제시.
n개 줄 제시. i번 작업 시간, 선행 관계에 있는 작업들의 갯수, 선행 관계에 있는 작업들의 번호 제시.

출력
모든 작업을 완료하기 위한 최소 시간 출력.
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
reqn = [0]*(n+1)
g = [[] for _ in range(n+1)]
cst = [0] * (n+1)
q = deque()
ans = 0
for i in range(1, n+1):
    nl = list(map(int, input().rstrip().split()))
    cst[i], reqn[i] = nl.pop(0), nl.pop(0)
    for j in nl:
        g[j].append(i)
    if reqn[i] == 0:
        q.append(i)
dp = cst[:]
while q:
    num = q.popleft()
    for i in g[num]:
        reqn[i] -= 1
        dp[i] = max(dp[i], cst[i]+dp[num])
        if reqn[i] == 0:
            q.append(i)
print(max(dp))

'''
# 빠른 코드
import sys

N = int(sys.stdin.readline().rstrip())

store = [ _ for _ in range(N)]

for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    store[i] = a[0]
    
    if a[1] > 0:
        max_sto = 0
        for sto in a[2:]:
            if store[sto-1] > max_sto:
                max_sto = store[sto-1]
        store[i] = store[i] + max_sto
            
    # print(store)
            
print(max(store))
'''







