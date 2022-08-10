# sum 대체
def sumli(li) :
    s = 0
    for i in li :
        s+=i
    return s
# max 대체
def maxn(li) :
    Mn = -10e9
    for i in li :
        if Mn < i :
            Mn = i
    return Mn

# 10번 실행
for _ in range(10) :
    # 입력
    t = int(input())
    tl = [list(map(int, input().split())) for _ in range(100)]
    # 가로 세로 대각선. 테이블 초기화
    garo = [0] * 100
    sero = [0] * 100
    cros = [0, 0]
    # 값 저장
    for i in range(100) :
        garo[i] = sumli(tl[i])
        cros[0] += tl[i][i]
        cros[1] += tl[i][99-i]
        for j in range(100) :
            sero[i] += tl[j][i]
    # 출력
    print(f"#{t} {maxn([maxn(garo), maxn(sero), maxn(cros)])}")

