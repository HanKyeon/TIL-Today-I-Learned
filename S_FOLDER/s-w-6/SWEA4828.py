'''
min max 간단 구현
'''

for testcase in range(1, int(input())+1) :
    mi, ma = 1e6 + 1, 1
    n = int(input)
    nl = list(map(int, input().split()))
    for n in nl :
        if n > ma :
            ma = n
        if n < mi :
            mi = n
    print(f"#{testcase} {ma - mi}")


