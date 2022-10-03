'''
행렬 곱셈 순서

n*m 행렬 A와 m*k 행렬 b를 곱할 때 필요한 곱셈 연산 수는 총 n*m*k이다. 행렬 n개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.
5*3 3*2 2*6 곱셈의 경우
123 순서로 곱할 경우 90번, 231 순서의 경우 126번.
행렬 n개 제시. 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값 제시.

입력
행렬 갯수 n 제시
n개 행렬 크기 r, c 제시.
순서대로 곱셈을 할 수 있는 크기만 제시.

출력
곱하는데 필요한 곱셈 연산의 최솟값 출력.
'''
'''
2차원 DP 또 못풀겠어서 결국 또 구글링....^^
'''

import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp =[[0 for _ in range(n)] for _ in range(n)] 

for i in range(1, n): #몇 번째 대각선?
    for j in range(0, n-i): #대각선에서 몇 번째 열?
        if i == 1: #차이가 1밖에 나지 않는 칸
            dp[j][j+i] = g[j][0] * g[j][1] * g[j+i][1]
            continue
        dp[j][j+i] = 2**32 #최댓값을 미리 넣어줌
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], 
                             dp[j][k] + dp[k+1][j+i] + g[j][0] * g[k][1] * g[j+i][1])
print(dp[0][-1]) #맨 오른쪽 위








