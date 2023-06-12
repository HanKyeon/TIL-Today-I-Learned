'''
n과 m 4

1부터 n까지 자연수 중에서 m개를 고른 수열
같은 수 여러번 가능
비내림차순이어야 한다.

입력
n, m 제시

출력
만족 수열 출력
'''
def prt(cnt):
    global m
    if cnt == m:
        print(*nl)
        return
    for i in nz:
        if i < nl[-1]:
            continue
        nl.append(i)
        prt(cnt+1)
        nl.pop()

n, m = map(int, input().rstrip().split())
nz = list(range(1, n+1))
nl = []
for i in nz:
    nl.append(i)
    prt(1)
    nl.pop()

