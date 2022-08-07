'''
쉬운 거스름 돈

그리디 기초!

입력
10이상 100만 이하 정수, 10의 배수

출력
#1 오만원 만원 오천원 천원 오백원 백원 오십원 십원
#1 오만원 만원 오천원 천원 오백원 백원 오십원 십원
'''
#testcase!!!!!!!!!!! testcase!!!
for testcase in range(1, int(input())+1) :
    n = int(input())
    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    c = [0] * 8

    for i in range(8) :
        c[i] = n // m[i]
        n = n % m[i]
    
    print(f"#{testcase}")
    print(' '.join(map(str, c)))


