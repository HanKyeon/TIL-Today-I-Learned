'''
N과 M 5

n개 자연수 중 m개 고른 수열 출력

중복수열x 공백 구분 출력 사전순 증가

입력
n, m 제시
n개 수 제시

출력
중복수열x 공백 구분 출력 사전순 증가
'''
def prt(cnt):
    global m
    if cnt == m:
        print(*nl)
        return
    for i in nz:
        if i in nl:
            continue
        nl.append(i)
        prt(cnt+1)
        nl.pop()

n, m = map(int, input().rstrip().split())
nz = list(set(map(int, input().rstrip().split())))
nz.sort()
nl = []
for i in nz:
    nl.append(i)
    prt(1)
    nl.pop()
