'''
햄버거 다이어트

입력
테케 갯수 T
재료수N 1이상 20이하, 제한 칼로리L 1이상 10000이하
점수 / 칼로리
점수/칼로리
점수/칼로리

제한 칼로리 이하의 조합 중 가장 맛 점수가 높은 햄버거 점수 출력
'''
def dfs(idx, scor, calo, v):
    global l
    if sum(v) == len(v):
        return
    v[idx] = 1
    dp[calo] = scor
    cscca = scca[:]
    for i in range(n):
        if v[i] == 0 and calo+scca[i][1] <= l :
            dfs(i, dp[calo] + scca[i][0], calo + scca[i][1], v)
            #dp[calo+scca[i][1]] = dp[calo] + scca[i][0]

for testcase in range(1, int(input())+1) :
    n, l = map(int, input().split())
    scca = [list(map(int, input().split())) for _ in range(n)]
    maxsc = 0
    for i in range(2**n):
        bubun = []
        for j in range(n):
            if i & (1<<j) :
                bubun.append(scca[j])
            if sum([sco[1] for sco in bubun]) <= l:
                maxsc = max(maxsc, sum(sco[0] for sco in bubun))
    print(f"#{testcase} {maxsc}")

    
    
    
'''
def select(idx, point, cal):
    global result

    if idx == N:
        if result < point:
            result = point
        return

    if sum(points[idx:]) + point < result:
        return

    if cal + cals[idx] < L:
        select(idx+1, point+points[idx], cal+cals[idx])
    select(idx+1, point, cal)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())

    points = []
    cals = []

    for i in range(N):
        point, cal = map(int, input().split())
        points.append(point)
        cals.append(cal)

    result = 0

    select(0, 0, 0)

    print('#{} {}'.format(tc, result))
'''



    '''
    avcasc = [[] for _ in range(n)]
    for i in range(n):
        sc, ca = map(int, input().split())
        avcasc[i] = [sc/ca, ca, sc]
    nowcal = 0
    nowsco = 0
    for val in avcasc :
        if val[1] <= l - nowcal:
    '''        


