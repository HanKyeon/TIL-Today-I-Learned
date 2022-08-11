'''
경비원

직사각형 모양의 블록

입력
블록의 가로길이 세로길이 1이상 100이하
상점 갯수 1이상 100이하
상점위치한방향 : 북1 남2 서3 동4 / 북남,동서 좌측경계,위쪽경계로부터 거리
막줄 동근이 위치

출력
동근이의 위치와 각 상점 사이 최단거리의 합
'''
# 입력
m, n = map(int, input().split())
stn = int(input())
stt = [list(map(int, input().split())) for _ in range(stn)]
dg = list(map(int, input().split()))
std = [0] * stn
i = -1
while stt : # stt가 빌 때까지
    direc, dist = stt.pop()
    i += 1
    if direc == dg[0] : # 같은 방향에 있을 때
        std[i] = abs(dg[1] - dist)
        continue
    if dg[0] <= 2 and direc <= 2 : # 남북 맞은 편이면
        std[i] = min(n + dg[1] + dist, n + 2*m - dg[1] - dist)
        continue
    elif dg[0] > 2 and direc > 2 : # 동서 맞은 편이면
        std[i] = min(m + dg[1] + dist, m + 2*n - dg[1] - dist)
        continue

    if dg[0] % 2 and direc % 2 : # 상점, 동근이 북서쪽에 모여 있으면
        std[i] = dg[1] + dist
        continue
    elif dg[0] % 2 == 0 and direc % 2 == 0 : # 상점 동근이가 동남쪽에 모여있으면 
        std[i] = m + n - dg[1] - dist
        continue
    # 나머지 처리 서남  동북에 배치되어 있을 때
    else :
        if dg[0] == 2 :
            std[i] = dg[1] + n - dist
            continue
        elif dg[0] == 3 :
            std[i] = n - dg[1] + dist
            continue
        elif dg[0] == 4 :
            std[i] = m - dist + dg[1]
            continue
        elif dg[0] == 1 :
            std[i] = m - dg[1] + dist
            continue

print(sum(std))




