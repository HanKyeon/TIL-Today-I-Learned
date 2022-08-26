'''
두개의 숫자열

마주보는 숫자들 곱한 뒤 합할 때 최댓값
3이상 20이하 n m

입력
테케T
N M 제시
N배열
M배열

출력
#테케T 최댓값
'''

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split())
    nl, ml = list(map(int, input().split())), list(map(int, input().split()))
    ans = int(-10e9)
    if n > m:
        for i in range(n-m+1):
            s = 0
            for j in range(m):
                s += nl[i+j]*ml[j]
            ans = max(s, ans)
    else:
        for i in range(m-n+1):
            s = 0
            for j in range(n):
                s += ml[i+j]*nl[j]
            ans = max(s, ans)
    print(f"#{testcase} {ans}")

