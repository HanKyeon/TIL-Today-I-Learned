'''
암호 생성기

n개의 수를 처리하면 8자리 암호 생성 가능.

8개의 숫자 입력
첫째 숫자를 1 빼고 맨 뒤로.
둘째 숫자는 2빼고 맨 뒤, 다음은 3 빼고 ,4, 5까지 하면 한 사이클이다.
0보다 작아지는 경우 0이 되면서 종료되며, 이게 암호가 됨.

입력
테케 번호
8데이터
테케번호
8데이터

출력
#테케 8개 암호
'''

for testcase in range(1, 11):
    _ = input()
    nl = list(map(int, input().split()))
    while nl:
        for i in range(1, 6):
            a = nl.pop(0)
            b = a-i
            if b > 0:
                nl.append(b)
            else:
                b = 0
                nl.append(b)
                break
        if 0 in nl: break
    print(f"#{testcase}", end=' ')
    print(*nl)



