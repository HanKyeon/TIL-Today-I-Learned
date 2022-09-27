'''
최소 생산 비용

A사 공장 여러곳.
N종의 제품을 n곳의 공장 한 곳 당 한가지.
전체 제품 최소 생산 비용 계산.

입력
테케T
제품 수 n
공장 제시

출력
#테케T 최소비용
'''
def 레쓰고(h, val):
    global n, ans
    if h == n-1:
        ans = min(ans, val)
        return
    if (n-h-1)+val >= ans:
        return
    for i in range(n):
        if v[i]:
            continue
        v[i] = 1
        레쓰고(h+1, val + g[h+1][i])
        v[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    ans = int(10e9)
    v = [0] * n
    for i in range(n):
        v[i] = 1
        레쓰고(0, g[0][i])
        v[i] = 0
    print(f"#{tc} {ans}")



























