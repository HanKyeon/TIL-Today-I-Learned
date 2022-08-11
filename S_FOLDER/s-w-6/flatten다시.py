
def fMmi(li) :
    M, m = 0, 0
    for i in range(len(li)) :
        if li[M] < li[i] :
            M = i
        if li[m] > li[i] :
            m = i
    return (M, m)

for testcase in range(1, 11) :
    k = int(input())
    hl = list(map(int,  input().split()))
    
    for i in range(k) :
        a, b = fMmi(hl)
        hl[a] -= 1
        hl[b] += 1
        if hl[a] - hl[b] <2 :
            break
    a, b = fMmi(hl)
    print(f"#{testcase} {hl[a] - hl[b]}")
    
