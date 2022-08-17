'''
파스칼의 삼각형

크기가 n인 파스칼의 삼각형을 만들어야 한다.
1. 첫번째 줄은 숫자 1이다.
두번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자 합으로 구성된다.
N이 4일 경우
1
11
121
1331
N을 입력 받아 크기가 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

제약 사항
파스칼의 삼각형의 크기 N은 1이상 10이하의 정수이다.

입력
테케T
삼각형 크기 숫자N

출력
#테케
삼
삼각
삼각형
'''
def semo(num):
    if num == 1:
        print(1)
        return
    if num == 2:
        print(1)
        print("1 1")
        return
    g = [[1]]
    n  = num
    for i in range(2, n+1):
        g.append([1] + [0]*(i-2) + [1])
    for i in range(2, n):
        for j in range(1, i):
            g[i][j] = g[i-1][j-1] + g[i-1][j]
    for i in g:
        print(*i)

for testcase in range(1, int(input())+1):
    n = int(input())
    print(f"#{testcase}")
    semo(n)


