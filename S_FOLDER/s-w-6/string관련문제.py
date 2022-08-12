#import sys
#sys.stdin = open("input.txt", "r", encoding="UTF-8")

T = 10
def cmp(st, N, p, M, i) :
    for j in range(M) :
        if st[i+j] != p[j] :
            return 0
    return 1

for testcase in range(1, T+1) :
    _ = input()
    p = input()
    st = input()
    ans = 0
    N, M = len(st), len(p)

    for i in range(N-M+1) :
        if cmp(st, N, p, M, i) :
            ans += 1

    print(f"#{testcase} {ans}")
    