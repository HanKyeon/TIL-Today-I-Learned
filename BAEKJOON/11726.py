'''
2*n 타일링

2*n 크기 직사각형을 12 21 타일로 채우는 방법의 수

입력
n 1이상 1000이하
첫째줄에 2*n 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지 출력
'''

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else: # 1,2 예외처리 이후 피보나치 진행
    g = [0]*(n+1)
    g[1], g[2] = 1, 2
    for i in range(3, n+1):
        g[i] = g[i-1]+g[i-2]
    print(g[n]%10007)








