'''
Magnetic

위는 N 아래는 S
막아주는거 없으면 떨어진다.



입력 테케 10번 #1
100*100 테이블 주어진다. 1은 N 2는 S 0은 없음
N이 위 S가 아래

출력
교착상태 갯수
'''

for t in range(1, 11) :
    # 입력
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(100)]
    # 편하게 하기 위해 N이 좌, S가 우에 있는 테이블 제작
    s = [[0] * 100 for _ in range(100)]
    for i in range(100) :
        for j in range(100) :
            s[i][j] += g[j][i]
    c = 0 # 카운트

    # 실행
    for x in s :
        yn = False
        for y in x :
            if y == 1 :
                yn = True
            if yn == True and y == 2 :
                c += 1
                yn = False
                continue
    # 출력
    print(f"#{t} {c}")
