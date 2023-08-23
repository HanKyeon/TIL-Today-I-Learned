'''
신기한 소수

n자리씩 끊었을 때 모두 소수인 수가 신기한 소수이다. n자리 신기한 소수를 모두 찾자

입력
n 제시

출력
n자리 수 신기한 소수를 오름차순 정렬 한 줄에 하나 출력
'''
def check(num):
    if num < 2: return
    for i in range(2, int(num**0.5)+1):
        if not num%i: return
    return True

def dfs(num):
    global n
    if not check(num): return
    if len(str(num)) == n:print(num);return
    for i in (1,3,5,7,9):dfs(num*10+i)

n = int(input())
for i in (2,3,5,7): dfs(i)
'''
# 빠른 코드
import sys
input = sys.stdin.readline

n = int(input())

def isPrime(x):
    if not x%2:
        return False
    for i in range(3, int(x**.5)+1, 2):
        if not x%i:
            return False
    return True

dp = [[] for _ in range(n)]
dp[0].extend([2, 3, 5, 7])
for cnt in range(1, n):
    for i in dp[cnt-1]:
        for j in [1, 3, 5, 7, 9]:
            tmp = i*10 + j
            if isPrime(tmp):
                dp[cnt].append(tmp)
print(*dp[-1], sep='\n')
'''
'''
# 시간 초과
def lego(num):
    k = 1
    while num+num*k < 10**n+2:
        che[num+num*k] = 0
        k+=1
    for i in range(len(str(num))-1, 0, -1):
        if not che[num//10**i]:
            return
    memo[len(str(num))].append(num)

n = int(input())
che = [0, 0]+[1]*(10**n)
memo = {i: [] for i in range(1, n+1)}
for i in range(2, 10**n+2):
    if not che[i]: continue
    lego(i)
for i in memo[n]:
    print(i)
'''
