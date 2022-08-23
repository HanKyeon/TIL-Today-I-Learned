'''
배열 최소 합
'''
def 최소합(s, h, v):
    global n, ans
    if s > ans:
        return
    if sum(v) == n or h == n:
        ans = min(ans, s)
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            s += g[h][i]
            최소합(s, h+1, v)
            s -= g[h][i]
            v[i] = 0

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    ans = 100000
    v = [0]*n
    최소합(0, 0, v)
    print(f"#{testcase}", end=' ')
    print(ans)



