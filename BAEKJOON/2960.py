'''
에라토스테네스의 체

n, k가 주어졌을 때 k번째 수를 구하는 프로그램 작성

입력
n, k 제시

출력
k번째 지워진 수 출력
'''
n, m = map(int, input().split())
cnt, v = 0, [0,0]+[1]*(n-1)
def lego():
    global n, m, cnt
    for i in range(2, n+1):
        if not v[i]: continue
        k = 0
        while i+i*k <= n:
            if v[i+i*k]:
                v[i+i*k], cnt = 0, cnt+1
                if cnt == m: return i+i*k
            k+=1
print(lego())
