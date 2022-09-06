'''
숨바꼭질 2

숨바꼭질. n, k 0이상 10만이하.

동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지, 가장 빠른 시간으로 찾는 방법이 몇가지인지 구하시오.
'''
from collections import deque

n, k = map(int, input().split())
if k <= n:
    print(n-k)
    print(1)
else:
    dp = [int(10e9)] * (2*k+1)
    q = deque([[0, n]])
    dp[n] = 0
    ans = 0
    while q:
        tz, nod = q.popleft()
        # print(tz, nod)
        if tz > dp[k]:
            break

        if nod == k and tz == dp[k]:
            ans += 1
            continue
        elif nod == k and tz < dp[k]:
            dp[k] = tz
            ans = 1
            continue

        if nod-1 >= 0 and dp[nod-1] >= tz+1:
            q.append([tz+1, nod-1])
            if nod-1 == k:
                ans = 0
            else:
                dp[nod-1] = tz + 1
        if 0 <= nod+1 <= k*2 and dp[nod+1] >= tz+1:
            q.append([tz+1, nod+1])
            if nod+1 == k:
                ans = 0
                
            else:
                dp[nod+1] = tz + 1
        if 0 <= nod*2 <= k*2 and dp[nod*2] >= tz+1:
            q.append([tz+1, nod*2])
            if nod*2 == k:
                ans = 0
                
            else:
                dp[nod*2] = tz + 1

    print(dp[k])
    print(ans)



