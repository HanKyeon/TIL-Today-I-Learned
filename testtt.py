import sys
input = sys.stdin.readline
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

    . . v . .
    . . . < @
    ^ . > . .
    > . . v .
