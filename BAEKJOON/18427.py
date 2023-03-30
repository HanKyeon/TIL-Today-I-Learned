'''
함께 블록 쌓기

1~n개 블록 학생들 각각. 최대 m개 블록. 가지고 있는 모든 블록 높이는 서로 다름.
1~n 학생들이 가진 블록을 차례로 사용해서 바닥에서부터 쌓아 하나의 탑을 만들 것.
어떤 애는 안써도 되고, 한 명 당 최대 1개만 쓸 수 있음.
1~n 학생들이 갖고 있는 블록 정보 제시.
높이가 정확히 H인 탑을 만들 수 있는 경우의 수 계산하는 프로그램.

입력
n, m, h 공백 구분 제시.
n개 줄 애들 가진 블록 높이 공백 기준 구분 제시.
높이는 1000이하 자연수, 한 명이 가진 모든 블록 높이는 서로 다름.

출력
높이가 H인 탑을 만드는 경우의 수를 10007로 나눈 나머지
'''
import sys
input = sys.stdin.readline

n, m, h = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [1]+[0]*h
for li in g:
    ndp = dp[:]
    for i in li:
        for j in range(h+1-i):
            if dp[j]:
                ndp[j+i] += dp[j]
    dp = ndp[:]
print(dp[-1]%10007)


# dp = [[0]*(h+1) for _ in range(n)]
# for i in g[0]:
#     dp[0][i] = 1

# for i in range(1, n): # 학생 번호
#     dp[i] = dp[i-1][:]
#     for j in g[i]: # 블록 높이
#         # 냅색
#         for k in range(h+1):
#             if k+j <= h:
#                 dp[i][k+j] += dp[i-1][k]+1
# for i in dp:
#     print(i)






