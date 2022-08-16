
def hm(gr, num):
    for gs in gr:
        for i in range(len(gs)-num+1):
            ss = gs[i:i+num]
            if ss == ss[::-1]:
                return ''.join(ss)

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    s = list(map(list, zip(*g)))
    ans = hm(g, m)
    if ans == None:
        if hm(s, m):
            ans = hm(s, m)
    print(f"#{testcase} {ans}")
