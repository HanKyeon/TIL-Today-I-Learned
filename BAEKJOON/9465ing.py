'''
스티커

2행 n열로 붙은 스티커.
하나 떼면 대각선 뗄 수 있다.
최대 가치는

입력
테케T
1~10만 N
스티커가치0~100 * n
스티커가치0~100 * n

출력
최댓값테케1
최댓값테케2
'''

for _ in range(1, int(input())+1):
    n = int(input())
    nl = [[0]+list(map(int, input().split())) for _ in range(2)]
    g = [nl[0][:], nl[1][:]] # 데이터 다룰 리스트
    for w in range(1, n+1): # 지그재그로 일단 더해줌
        for h in range(2):
            g[h][w] += g[(h+1)%2][w-1]
    for i in range(2, n+1): # 점화식. 지그재그로 더해준 것, 한 칸 멈췄다가 더해준 것의 크기 비교. 중앙은 없어도 될듯?
        g[0][i] = max(g[1][i-2]+nl[0][i], g[1][i-1]+nl[0][i], g[0][i])
        g[1][i] = max(g[0][i-2]+nl[1][i], g[0][i-1]+nl[1][i], g[1][i])
    print(max(g[0][-1], g[1][-1]))
    #print(dp[-1])


# dp = [max(u, d) for u, d in list(zip(*g))]
# 이렇게 하면 반례가 생긴다.
# 반례
# 1
# 4
# 100 1 1 100
# 1 1 100 1