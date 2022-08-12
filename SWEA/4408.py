'''
자기 방으로 돌아가기

홀수방---
짝수방----
복도 길 곂치면 안됨.
방이동은 거리 관계 없이 단위시간1이 걸린다.

입력
테케수
학생수
현재방 / 돌아갈방
현재방 돌아갈 방
학생수
현재방 돌아갈방

출력
돌아가는데 필요한 시간
'''

for testcase in range(1, int(input())+1) :
    n = int(input())
    ss = [list(map(int, input().split())) for _ in range(n)]
    d = [0] * 201 # 버스합으로 풀기 위한 201.
    sz = [0] * 201 # 버스 합 아니면 200 해도 됨.
    for s in ss: # 애들 루트 보면서
        sta, end = sorted(s) # 시작 도착 바꿔놔도 상관 없으므로 정렬
        if sta % 2 == 0: # 시작 인덱스가 짝이면 2로 나눈 몫에서 -1
            sta = sta // 2 - 1
        elif sta % 2 == 1: # 시작 인덱스가 홀인면 그냥 2로 나눈 몫
            sta = sta // 2
        if end % 2 == 0:
            end = end // 2 - 1
        elif end % 2 == 1:
            end = end // 2

        d[sta] += 1
        d[end+1] -= 1 # 이 부분이 버스합 때 필요한 부분이라 201로

        for i in range(200):
            sz[i] = sum(d[:i+1])

        # for k in range(sta, end+1): # 버스합 안썼을 때
        #     d[k] += 1

    print(f"#{testcase} {max(sz)}")







