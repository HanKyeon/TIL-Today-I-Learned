for testcase in range(1, int(input())+1):
    n = int(input())
    N = int(input())
    nl = [0] * 10
    while N > 0 :
        a = N % 10
        nl[a] += 1
        N = N // 10
    ml = list(zip(nl, range(10)))
    ml.sort(reverse=True)
    print(f"#{testcase} {ml[0][1]} {ml[0][0]}")
