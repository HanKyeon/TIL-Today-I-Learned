'''
평범한 배낭 2

물건을 넣을 때 어떤 물건을 넣느냐에 따라 민호의 만족도가 달라진다. 가방 무게는 정해져 있고, 이를 초과해 물건을 넣을 수 없다. 만족도가 최대가 되는 경우. 동일한 물건 존재. 숫자 크다.

입력
n, m 제시. 1이상 100이하, 1이상 10000이하. n은 물건 종류 갯수 m은 가방 최대 무게
v, c, k 제시. 1이상 m이하 v, 1이상 1만이하 c, k. v*k는 1이상 1만 이하.
v는 물건의 무게 c는 만족도 k는 물건의 갯수

출력
최대 만족도
'''
'''
저번에 풀었던 제곱수 4개의 합으로 다 표현 가능하다는거 써도 될듯? -> 어려워서 폐기
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dp = [0] * (m+1)
for _ in range(n):
    v, c, k = map(int, input().rstrip().split())
    q = deque()
    i = 1
    while k > 0: # 2의 제곱수의 합으로 전부 표현 가능
        l = min(i, k) # 2의 제곱수 혹은, 제곱수로 표현하고 남은 나머지
        q.append((v*l, c*l)) # 곱해준 값 더하기
        k -= i # k에서 i를 빼주기. 나머지 다 표현했으므로.
        i *= 2 # 제곱수 올리기
    ndp = dp[:] # 원래 중복을 처리하기 위해 필요했던 코드
    while q:
        v, c = q.popleft()
        for i in range(v, m+1):
            ndp[i] = max(dp[i], dp[i-v]+c, dp[i-1])
        if dp != ndp: # 마찬가지로 중복 처리를 위한 코드였다...만 확신을 위해 남겨둠.
            dp = ndp[:]

print(dp[m])
























