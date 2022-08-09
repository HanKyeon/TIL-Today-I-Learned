'''
현주의 상자 바꾸기



입력
테케T
1이상 1000이하 N, Q 공백 구분 제시
Q개의 줄 i번째 줄에 1이상 Li Ri N 제시

출력
#t Q개의 작업 수행 후 1번부터 N번까지 상자에 적힌 값
'''
for testcase in range(1, int(input())+1) :
    n, q = map(int, input().split())
    nl = [0] * n
    for i in range(1, q+1) :
        l, r = map(int, input().split())
        for j in range(l-1, r) :
            nl[j] = i
    print(f"#{testcase}", *nl)









