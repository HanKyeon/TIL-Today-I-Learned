'''
자고 일어나서 하자

합 구하기

배열 100 100
10개 테케 (직접 입력해줌. 1,2,3, ... 10까지)

'''
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
        garo[i] = sum(tl[i])
        cros[0] += tl[i][i]
        cros[1] += tl[i][99-i]
        for j in range(100) :
            sero[i] += tl[j][i]
    # 출력
    print(f"#{t} {max(max(garo), max(sero), max(cros))}")

