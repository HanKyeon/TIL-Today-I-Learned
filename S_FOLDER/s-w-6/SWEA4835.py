'''
구간합
'''

for testcase in range(1, int(input())+1) :
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    sta = 0
    end = k
    Ms = sum(nl[sta:end])
    ms = sum(nl[sta:end])
    nh = Ms
    while end < n :
        nh = nh - nl[sta] + nl[end]
        sta += 1
        end += 1
        if nh > Ms :
            Ms = nh
        if nh < ms :
            ms = nh
    print(f"#{testcase} {Ms-ms}")