'''
View
'''
# 테케 입력
for t in range(1, 11) :
    # 입력
    n = int(input())
    d = list(map(int, input().split()))
    # 조광 하우스 0개
    jh = 0
    # 반복하는데 0, 1, n-2, n-1 인덱스 일 때 따로 해줌
    for hn in range(0, n) :
        if hn == 0 :
            if d[hn] > max(d[hn+1], d[hn+2]) :
                jh += d[hn] - max(d[hn+1], d[hn+2])
            else : 
                continue
        elif hn == 1 :
            if d[hn] > max(d[hn-1], d[hn+1], d[hn+2]) :
                jh += d[hn] - max(d[hn-1], d[hn+1], d[hn+2])
            else : 
                continue
        elif hn == n-2 :
            if d[hn] > max(d[hn-2], d[hn-1], d[hn+1]) :
                jh += d[hn] - max(d[hn-2], d[hn-1], d[hn+1])
            else : 
                continue
        elif hn == n-1 :
            if d[hn] > max(d[hn-2], d[hn-1]) :
                jh += d[hn] - max(d[hn-2], d[hn-1])
            else : 
                continue
        # 맨뒤 맨앞 2개 아니고 해당 층 높이가 다른층보다 높으면 빼주고
        # 조광 하우스에 더해줌
        else : 
            if d[hn] > max(d[hn-2], d[hn-1], d[hn+1], d[hn+2]) :
                jh += d[hn] - max(d[hn-2], d[hn-1], d[hn+1], d[hn+2])
            else : 
                continue
    # 출력
    print(f'#{t}', end=' ')
    print(jh)
