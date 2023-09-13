'''
n과 m 6

n개 자연수 중 m개 고른 수열, 고른 수열 오름차순

출력
만족하는 수열 출력, 사전순 증가 순서
'''
import sys
input = sys.stdin.readline

def dfs(idx):
    global n, m
    if len(ans) == m: print(*ans); return
    for i in range(idx+1, n): v[i]=1; ans.append(nl[i]); dfs(i); ans.pop(); v[i]=0

n, m = map(int, input().rstrip().split())
nl = list(sorted(map(int, input().rstrip().split())))
v, ans = [0]*n, []
for i in range(n): v[i]=1; ans.append(nl[i]); dfs(i); ans.pop(); v[i]=0

'''
# 빠름
from sys import stdin

def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b

def dfs(a, b):
    if b == m:
        print(' '.join(print_nums))
        return
    for i in range(a, len(nums)):
        if checks[i]:
            continue
        checks[i] = True
        print_nums[b] = str(nums[i])
        dfs(i + 1, b + 1)
        checks[i] = False

if __name__ == '__main__':
    n, m = get_two_input()
    nums = list(map(int, stdin.readline().split(" ")))
    nums.sort()
    print_nums = ['0' for _ in range(m)]
    checks = [False for _ in range(n)]
    dfs(0, 0)
'''
