# 테스트 케이스 받기
for t in range(int(input())) :
    # 입력 받기
    a, b, x, c, d, y = map(int, input().split())
    # 조와 백의 거리
    dis = ((c - a)**2 + (d - b)**2) ** (1/2)
    # 실행
    if dis < x + y and dis > abs(y - x) :
        print('2')
    elif dis == 0 and x == y:
        print('-1')
    elif dis == x + y or dis == abs(y - x) :
        print('1')
    else :
        print('0')