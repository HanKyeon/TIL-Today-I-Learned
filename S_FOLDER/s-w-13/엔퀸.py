'''
엔퀸 구현
'''
def nq(h):
    global ans
    if h == n:
        ans += 1
        return
    for i in range(n):
        if not garo[i] and not hap.get(h+i, 0) and not cha.get(h-i, 0):
            garo[i] = 1
            hap[h+i] = 1
            cha[h-i] = 1
            nq(h+1)
            garo[i] = 0
            hap[h+i] = 0
            cha[h-i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    garo = [0]*n
    hap, cha = {}, {}
    ans = 0
    nq(0)
    print(f"#{tc} {ans}")