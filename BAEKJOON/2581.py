'''
소수

M이상 N이하 자연수 중 소수인 것을 골라 합과 최솟값 출력
'''
m, n = int(input()), int(input())
g = [False, False] + [True] * (n-1)
for i in range(n):
    if g[i]:
        j = 2
        while i*j <= n:
            g[i*j] = False
            j += 1
pn = [i for i, v in enumerate(g) if v]
an = []
for i in pn:
    if m<= i <=n:
        an.append(i)
if not an:
    print(-1)
else:
    print(sum(an))
    print(an[0])

