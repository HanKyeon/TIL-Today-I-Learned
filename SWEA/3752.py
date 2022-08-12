'''
가능한 시험 점수

입력
테케
문제 갯수 N 1이상 100이하
N개의 문제 배점 1이상 100이하

출력
받을 수 있는 점수의 종류
'''

def sco(dg, num):
    if dg == [] or num > sum(nl):
        return
    d = dg[:]
    g[num] = 1
    d.remove(num)
    for s in d:
        sco(d, num + s)

for testcase in range(int(input())+1):
    n = int(input())
    nl = list(map(int, input().split()))
    g = [0] * 10001
    g[0], g[sum(nl)] = 1, 1
    for i in nl:
        g[i] = 1
    for x in nl:
        sco(nl, x)




