'''
플로이드 워셜 알고리즘 소스코드

3중 for문을 이용해 3차원 데이터 구조를 읽는 형태.
모든 데이터를 계산하므로 시간 복잡도가 N^3이다.
따라서 n이 500 이하 일 때만 사용하면 좋다.
'''
# 무한은 10억
INF = int(1e9)
# n,m 입력받기.
n = int(input())
m = int(input())
# g테이블을 [x][y] 형태로 나타낼 수 있도록 초기화 및 거리 INF
g = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신에서 자신으로 가는 거리는 0
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            g[a][b] = 0
# 각 간선에 대한 정보 입력 받기, 해당 값으로 해당 테이블 초기화
for _ in range(m) :
    # A에서 B로 가는 비용이 C이다
    a, b, c = map(int, input().split())
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1) :
    for a in range(1, n+1) :
        for b in range(1, n + 1) :
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])
# 수행된 결과 출력
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        # 갈 수 없으면 갈수 없다고
        if g[a][b] == INF :
            print("INFINITY", end=" ")
        # 갈 수 있으면 최솟값 출력
        else :
            print(g[a][b], end=" ")
    print() # \n




