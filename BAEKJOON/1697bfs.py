'''
숨바꼭질

수빈이는 n 0이상 10만이하 지점에 있고
동생은 k 0이상 10만이하 지점에 있다.
수빈이는 걷거나 순간이동 가능
걷기 : 1초후에 x-1 or x+1
순간이동 : 1초 후에 2*x 위치로 이동
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후?

입력
수빈이위치 N, 동생 위치 K

출력
가장 빠른 시간
'''
import sys
sys.setrecursionlimit(100000)

def mollu(num):
    global k
    dp[num] = 0
    li = [num]
    while li :
        #print(li, end=' ')
        nnum = li.pop(0)
        #print(nnum, li)
        if 0 <= nnum-1 <= 100000 and dp[nnum-1] > dp[nnum]+1:
            li.append(nnum-1)
            dp[nnum-1] = dp[nnum]+1
        if 0 <= nnum+1 <= 100000 and dp[nnum+1] > dp[nnum]+1:
            li.append(nnum+1)
            dp[nnum+1] = dp[nnum]+1
        if 0 <= nnum*2 <= 100000 and dp[nnum*2] > dp[nnum]+1:
            li.append(nnum*2)
            dp[nnum*2] = dp[nnum]+1
    return dp[k]

n, k = map(int, input().split())
if n >= k: # 동생이 왼쪽에 있으면 걸어가는 수 밖에 없다.
    print(n-k)
else :
    dp = [100000] * (100001)
    dp[n] = 0
    print(mollu(n))


