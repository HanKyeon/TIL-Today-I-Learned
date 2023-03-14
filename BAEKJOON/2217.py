import sys
input = sys.stdin.readline
n = int(input())
nl = [int(input()) for i in range(n)]
nl.sort(reverse=True)
nl = [0]+nl
ans = 0
for i, v in enumerate(nl):
    ans = max(ans, i*v)
print(ans)