def bs(sta, end, num) :
    while sta <= end :
        mid = (sta + end) // 2
        if g[mid] == num :
            return mid+1
        elif num > g[mid] :
            return bs(mid+1, end, num)
        elif num < g[mid] :
            return bs(sta, mid-1, num)
    return 0

for testcase in range(1, int(input())+1) :
    n, d = map(int, input().split())
    g = list(map(int, input().split()))
    print(f"#{testcase} {bs(0, n-1, d)}")