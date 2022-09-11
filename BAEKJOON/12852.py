'''
1로 만들기2

1. 3으로 나누어 떨어지면, 3으로 나눈다.
2. 2로 나눠 떨어지면 2 로 나눈다.
3. 1을 뺀다.

정수 N 제시, 1을 만들 것이다. 연산을 사용하는 횟수의 최솟값 출력.

입력
1이상 10**6 이하 n 제시.

출력
횟수 최솟값.
1로 만드는 방법에 포함되어 있는 수를 공백 구분 순서대로 출력.
'''
from collections import deque

n = int(input())
q = deque([(n, 0, [n])])
dp = [int(10e9)] * (n+1)
dp[n] = 0
while q:
    num, cnt, arr = q.popleft()
    if num == 1:
        break
    if dp[num] < cnt:
        continue
    if num % 3 == 0 and dp[num//3] > cnt+1:
        dp[num//3] = cnt+1
        q.append((num//3, cnt+1, arr+[num//3]))
    if num % 2 == 0 and dp[num//2] > cnt+1:
        dp[num//2] = cnt+1
        q.append((num//2, cnt+1, arr+[num//2]))
    if dp[num-1] > cnt+1:
        dp[num-1] = cnt+1
        q.append((num-1, cnt+1, arr+[num-1]))
print(cnt)
print(*arr)





