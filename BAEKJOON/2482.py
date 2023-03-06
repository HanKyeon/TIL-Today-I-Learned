'''
색상환

n, k 에 대해 n개 색으로 구성되어 있는 색상환에서 어떤 인접한 두 색도 동시에 선택하지 않으면서 서로 다른 k개의 색을 선택하는 경우의 수를 구해라.

입력
n
k

출력
n색상환에서 어떤 인접한 두 색도 동시에 선택하지 않고 k개의 색을 고를 수 있는 경우의 수를 10억3으로 나눈 나머지 출력.
'''
from math import factorial
n, k = int(input()), int(input())
# if n/2 < k:
#     print(0)
#     exit()
# if n/2 == k:
#     print(2)
#     exit()
# if k == 1:
#     print(n)
#     exit()

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0], dp[i][1] = 1, i
for i in range(2, n+1):
    for j in range(2, k+1):
        if i == n:
            dp[i][j] = (dp[i-3][j-1]+dp[i-1][j])
            continue
        dp[i][j] = (dp[i-1][j]+dp[i-2][j-1])
# for i in dp:
#     print(i)
print(dp[n][k]%1000000003)

n, k = int(input()), int(input())

def nCr(n, r):
    if n<0 or r<0 or r>n:
        return 0
    ret = factorial(n) // (factorial(r) * factorial(n-r))
    print("/ : ", factorial(n) / (factorial(r) * factorial(n-r)))
    print("// : ", factorial(n) // (factorial(r) * factorial(n-r)))
    return ret
print(int(nCr(n-k+1, k)-nCr(n-k-1, k-2))%1000000003)

'''
N = int(input()); K = int(input())
if K == 1:
    print(N)
    quit()
X = N - (2*K - 1)
if X >= 1:
    l = [j for j in range(1, X+1)]
    for _ in range(K-2):
        tl = [l[0]]
        for i in range(1, len(l)):
            tl.append((tl[i-1] + l[i]) % 1000000003)
        l = tl[:]
    print((l[-1] + sum(l)) % 1000000003)
else:
    print(0)
'''
'''
n, k = int(input()), int(input())
dp=[[-1]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
    dp[i][1]=i

def lego(i, j):
    if j>(i/2):
        return 0
    if dp[i][j]>=0:
        return dp[i][j]
    dp[i][j]=lego(i-1,j)+lego(i-2,j-1)
    if dp[i][j]>1000000003:
        dp[i][j]%=1000000003
    return dp[i][j]

print(lego(n,k))
'''
'''
import sys
I=sys.stdin.readline
d=1_000_000_003

def nCr(n,r):
    if n<0: return 0
    if r<0 or r>n: return 0
    r=min(r,n-r)
    ans=1
    for i in range(r):
        ans=ans*(n-i)//(i+1)
    return ans%d
n=int(I())
k=int(I())
print((nCr(n-k+1,k)-nCr(n-k-1,k-2))%d)
'''


# n, k = int(input()), int(input())
# dp=[[-1]*(k+1) for _ in range(n+1)]
# for i in range(n+1):
#     dp[i][0]=1
#     dp[i][1]=i

# def lego(i, j):
#     if j>(i/2):
#         return 0
#     if dp[i][j]>=0:
#         return dp[i][j]
#     dp[i][j]=lego(i-1,j)+lego(i-2,j-1)
#     if dp[i][j]>1000000003:
#         dp[i][j]%=1000000003
#     return dp[i][j]

# print(lego(n,k))




