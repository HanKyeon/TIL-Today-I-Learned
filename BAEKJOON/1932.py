'''
정수 삼각형

삼각형이 있다.
맨위부터 수를 하나씩 선택하며 내려온다.
선택된 수의 합이 최대가 되는 경로를 구해라
위 아니면 대각선 왼쪽 가능하다.

입력
삼각형의 크기 n 1이상 500이하
삼각형 제시

출력
합이 최대가 되는 경로에 있는 수의 합
'''
# 오 g를 이렇게 네모로 만들 수도 있다!
n = int(input())
g = [list(map(int, input().split())) + [0]*i for i in range(n-1, -1, -1)]

for i in range(1, n):
    for j in range(i+1):
        
        if j == 0 :
            g[i][j] += g[i-1][j]
        else:
            g[i][j] += max(g[i-1][j-1], g[i-1][j])
print(max(g[n-1]))