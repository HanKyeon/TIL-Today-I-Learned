'''
1, 2, 3 더하기 3

정수 n이 주어졌을 대, 1,2,3 합으로 나타내는 방법의 수를 구해라.

입력
테케 t
n 제시

출력
n을 1,2,3으로 나타내는 방법의 수를 1000000009로 나눈 나머지 출력
'''
dp = [1,2,4,7]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n): dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])
