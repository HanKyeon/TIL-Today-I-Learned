'''
제곱 ㄴㄴ

어떤 수 N이 1이 아닌 제곱수로 나눠지지 않을 때, 이 수를 제곱 ㄴㄴ수라 한다. 1,2,3,5,6,7,10,11,13...
K가 주어졌을 때, K번째 제곱 ㄴㄴ수를 구해라.

입력
K 제시

출력
K번째 제곱 ㄴㄴ 수 출력.
'''


def nono(n):
    ret = 0
    for i in range(1, int(n**0.5)+1):
        ret += g[i] * (n // (i**2))
    return ret

k = int(input())
g = [0, 1] + [0]*999999
for i in range(1, 1000001):
    if g[i]:
        for j in range(i * 2, 1000001, i):
            g[j] -= g[i]
lft, rgt = 0, 2000000000
while lft < rgt-1:
    mid = (lft + rgt) // 2
    if nono(mid) < k:
        lft = mid
    else:
        rgt = mid
print(rgt)






