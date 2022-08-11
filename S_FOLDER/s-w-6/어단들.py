# 가능한 갯수 반환. li는 한 줄이고, w는 k
def check1(li, w) :
    l = len(li) # == n
    c = 0
    sta = [1] * w + [0]
    end = [0] + [1] * w
    nor = [0] + [1] * w + [0]
    # k가 n과 같으면 확인
    if l == w :
        if l == [1] * w :
            return 1
        else :
            return 0
    # k가 n보다 1 작으면 확인
    if l == w + 1 :
        if li[0:l-2] == sta :
            c += 1
        if li[1:l] == end :
            c += 1
        return c
    # 패스 했으면 시작, 끝, 중간에 1110 0111 01110 있는지 확인
    if li[0:w+1] == sta :
        c += 1
    if li[l-w-1:l] == end :
        c += 1
    for i in range(1, l-w) : # 인덱스 실수 주의
        if li[i-1:i+w+1] == nor :
            c += 1
    return c
# testcase!!!!!!!!!!!!!!!!!!
for testcase in range(1, int(input()) + 1) :
    # 입력
    n, k = map(int, input(). split())
    g = [list(map(int, input().split())) for _ in range(n)]
    s = list(map(list, zip(*g)))
    res = 0
    # 실행
    for i in range(n) :
        res += check1(g[i], k)
        res += check1(s[i], k)
    # 출력
    print(f"#{testcase}", end=' ')
    print(res)