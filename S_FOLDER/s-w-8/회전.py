'''
회전

N개의 숫자로 이루어진 수열
맨 앞 숫자를 뒤로 보내는 작업 n회 시행
맨앞숫자 출력

입력
테케T
10억이하 자연수 N개. 3이상 20이하, N이상 1000이하 M

출력
#T 맨 앞 값
'''
for testcase in range(1, int(input())+1):
    n, m = map(int, input().split())
    nl = list(input().split())
    x = m % n # 나머지
    print(f"#{testcase} {nl[x]}")

