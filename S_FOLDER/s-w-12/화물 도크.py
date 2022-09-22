'''
화물 도크

물류센터에 도크. 0시부터 담날 0시 전까지 A도크 사용 신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면 최대 몇대의 화물차가 이용 가능?

입력
테케 T
작업시작S 종료시간E 제시.

출력
#T 최대 화물 갯수
'''
for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(int, input().rstrip().split())) for _ in range(n)]
    g.sort(key=lambda x:(x[1], x[0]))
    sta, end = 0, 0
    ans = 0
    while g:
        ns, ne = g.pop(0)
        if ns < end:
            continue
        if ns >= end:
            ans += 1
            sta = end
            end = ne
    print(f"#{tc} {ans}")








