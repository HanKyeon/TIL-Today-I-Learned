'''
사탕 가게

사탕은 쪼갤 수 없다.
가격과 칼로리가 주어졌을 때, 어떻게 하면 칼로리의 합이 가장 크게 되는지 구해라.

입력
가게의 사탕 종류 수 n, 돈의 양 m 1이상5000이하n 0.01이상 100.00이하 m m은 항상 소수점 둘째자리까지 제시.
다음 n개 줄에 각 사탕의 칼로리 c와 가격 p 제시. 칼로리는 1이상 5000이하 p는 0.01이상 100.00이하 항상 소수점 둘째자리까지 제시.
입력 마지막 줄에는 0 0.00 제시

'''
import sys
input=sys.stdin.readline

def func():
    while True:
        n, m = input().rstrip().split()
        n = int(n)
        m = int(float(m)*100+0.5)
        if n == 0 and m == 0.00:
            break
        g = [(0, 0)]
        for _ in range(n):
            cal, prc = input().rstrip().split()
            cal = int(cal)
            prc = int(float(prc)*100+0.5)
            g.append((cal, prc))
        dp = [0] * (m+1)
        for i in range(1, n+1):
            cal, prc = g[i]
            for j in range(1, m+1):
                dp[j] = max(dp[j], dp[j-1])
                if j - prc >= 0:
                    dp[j] = max(dp[j], dp[j-prc]+cal)
        print(dp[m])
func()


'''
메모리 초과 : 저번에 한줄 dp로 하니까 틀렸던 경우가 있는데 이번엔 그런게 없나봄?
def func():
    while True:
        n, m = input().rstrip().split()
        n = int(n)
        m = int(float(m)*100+0.5)
        if n == 0 and m == 0.00:
            break
        g = [(0, 0)]
        for _ in range(n):
            cal, prc = input().rstrip().split()
            cal = int(cal)
            prc = int(float(prc)*100+0.5)
            g.append((cal, prc))
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            cal, prc = g[i]
            for j in range(1, m+1):
                if j - prc >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-prc]+cal, dp[i][j-prc]+cal)
        print(dp[n][m])
'''

'''
빠른 코드

import sys
input = sys.stdin.readline

def solve(n, m):
	candy = [input().split() for _ in range(n)]
	dp = [0 for _ in range(10001)]

	m = int(m*100 + 0.5)
	for c, p in candy:
		c = int(c)
		p = int(float(p) * 100 + 0.5)
		for i in range(p, m+1):
			dp[i] = max(dp[i], dp[i-p] + c)
	
	return dp[m]

if __name__ == '__main__':
	while True:
		n, m = input().split()
		n = int(n)
		m = float(m)

		if n == 0 and m == 0.00:
			break

		print(solve(n, m))
'''









