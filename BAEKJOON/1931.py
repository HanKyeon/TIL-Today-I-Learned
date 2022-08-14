'''
회의실 배정

회의실 1개. N개의 회의. 회의실 사용표 제작.
회의 I에 대해 시작시간과 끝나는 시간 제시.
각 회의가 겹치지 않게 하면서 회의실을 사용 할 수 있는 최대 회의 갯수
회의는 시작하면 중단x, 한 회의가 끝나는 것과 동시에 다음 회의 시작 가능.
회의는 시작시간과 끝나는 시간이 같을 수 있다.

입력
첫째줄 : 회의의 수 N 1이상 10만이하
이후 회의 정보 제시. 공백을 두고 시작시간 종료시간 제시.
시작시간과 종료시간은 2^31-1보다 작거나 같은 자연수
단축 입력
N
staT endT * n

출력
최대 사용 할 수 있는 회의 최대 갯수

'''
def cc(endtime, c):
    if endtime == 2**31:
        return c
    c+=1
    nsi = min(tt[tt[endtime]:])
    #tt.index(nsi)
    return cc(nsi, c)

n = int(input())
visited = [0] * n
sts, ets = [0] * n, [0] * n
tms = {}
for _ in range(n):
    st, et = map(int, input().split())
    tms[st] = min(tms[st], et)









