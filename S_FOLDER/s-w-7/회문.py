
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



def hm(hl) :
    for i in range(100-hl+1) :
        for j in range(100) :
            p, q = g[j][i:i+hl], s[j][i:i+hl]
            if p == p[::-1] :
                return True
            if q == q[::-1] :
                return True
    return False

for t in range(1, 11) :
    _ = input()
    g = [input() for _ in range(100)]
    s = [''.join(x) for x in zip(*g)]

    for i in range(100, 0, -1) :
        if hm(i):
            l = i
            break
    print(f"#{t} {l}")