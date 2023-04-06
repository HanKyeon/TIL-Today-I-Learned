'''
행렬 곱셈

n*m 행렬과 m*k 행렬 b를 곱해라.

입력
n, m 제시.
n개 줄 m개씩.
m, k 제시.
m개 줄 k개씩.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]
m, k = map(int, input().rstrip().split())
b = [list(map(int, input().rstrip().split())) for _ in range(m)]
b = list(zip(*b))
ans = [[0]*k for _ in range(n)]
for i in range(n):
    li1 = a[i]
    for j in range(k):
        li2 = b[j]
        for s in range(m):
            ans[i][j] += li1[s]*li2[s]
for i in ans:
    print(*i)
'''
1 2
3 4
5 6

-1 -2 0
0 0 3
'''



