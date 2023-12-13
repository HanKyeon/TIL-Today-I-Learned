'''
최대공약수

n, m 제시. 최대 공약수 구해라.

입력
n, m 제시

출력 최대 공약수 출력
'''
def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    

A, B = map(int, input().split())
print('1' * gcd(A, B))
