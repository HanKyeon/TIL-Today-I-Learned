'''
배열 최소 합.

n*n 배열 한 줄에서 하나 씩 n개의 숫자를 골라 합이 최소가 되도록 할 것. 조건에 맞게 숫자를 돌랐을 때의 최소 합 출력.

입력
테케T
n
그래프

출력
테케T 최솟값
'''
def 함수(li):
    global n, ans
    a = li[:]
    if len(a) == n:
        ret = 0
        for i, val in enumerate(a):
            ret += g[i][val]
        ans = min(ret, ans)
        return

    for i in range(n):
        if i not in a:
            a.append(i)
            함수(a)
            a.pop()

for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    inl = []
    ans = int(10e9)
    함수(inl)
    print(f"#{tc} {ans}")

'''
def 함수(s, dep):
    global n, ans
    if dep == n:
        ans = min(ans, s)
        return
    if s >= ans:
        return
    for i in range(n):
        if v[i] == 0:
            s += g[dep][i]
            v[i] = 1
            함수(s, dep+1)
            v[i] = 0
            s -= g[dep][i]

for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    ans = int(10e9)
    v = [0]*n
    함수(0, 0)
    print(f"#{tc}", end=' ')
    print(ans)
'''






