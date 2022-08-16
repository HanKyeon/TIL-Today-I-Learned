'''
백만장자 프로젝트

1. 연속된 N일 동안의 물건 매매가를 예측함
2. 당국의 감시망에 걸리지 않기 위해 하루 최대 1 구매 가능
3. 판매 언제든 가능

입력
테케T
2이상 100만이하 N
각날의 매매가 N개를 공백으로 구분하여 제시

출력
#t 최대이득
'''

# 포대기 덮는 것 처럼 max까지는 쭉 max, 그 뒤로는 그 다음 max에 뚜껑 덮어준 리스트 만들고 빼줌

for testcase in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().split()))
    ben = 0
    cnl = nl[:]
    mnu = max(nl)
    mn = nl.index(mnu)
    for i in range(mn):
        cnl[i] = mnu
    for i in range(n-1, mn, -1):
        if cnl[i] > cnl[i-1]:
            cnl[i-1] = cnl[i]
    for i in range(n):
        ben += cnl[i]-nl[i]
    print(f"#{testcase} {ben}")

'''
rnl = list(reversed(nl))
    m = rnl.index(max(rnl))
    ma = max(rnl)
    for i in range(1, m):
        if rnl[i] < rnl[i-1]:
            rnl[i] = rnl[i-1]
    for i in range(m, n):
        rnl[i] = ma
    nnl = list(reversed(rnl))
    for i in range(n):
        ben += nnl[i]-nl[i]
    print(f"#{testcase} {ben}")
'''
'''
    for i in range(n-1):
        m = max(nl[i+1:])
        if nl[i] <= m:
            ben += m-nl[i]
    print(f"#{testcase} {ben}")
'''