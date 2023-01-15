'''
저울

무게가 서로 다른 n개의 물건. 1부터 n까지 번호. 양팔 저울로 어떤게 무거운가 측정한 결과표 보유중
직접 측정하지 않은 물건 쌍의 비교 결과를 알아낼 수도 있고 알아낼 수 없을 수도 있다.
모순된 입력은 불가능하다.
물건 갯수 n과 일부 물건 쌍의 비교 결과가 제시되었을 때, 각 물건에 대해 그 물건과의 비교 결과를 알 수 없는 물건의 갯수를 출력해라.

입력
물건 갯수 n 제시. 5~100
측정된 쌍의 갯수 m 0~2000
m개 줄비교 결과 제시. a, b. a가 b보다 무겁다.

출력
n개 줄에 결과를 출력.
i번째 줄에는 물건 i와 비교 결과를 알 수 없는 물건의 갯수 출력.
'''
import sys
input = sys.stdin.readline
n, m = int(input()), int(input())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] and g[k][j]:
                g[i][j] = 1

for i in range(n):
    for j in range(n):
        if g[i][j]:
            g[j][i] = 1

ans = map(lambda x: n-sum(x)-1, g)
for i in ans:
    print(i)























