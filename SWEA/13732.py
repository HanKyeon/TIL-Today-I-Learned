'''
정사각형 판별

#으로 정사각형이면 yes 안되면 no

n은 1이상 20이하 

'''

for testcase in range(1, int(input())+1):
    n = int(input())
    g = [list(input()) for _ in range(n)]
    ng = []
    for i in range(n):
        ng.append([i for i, v in enumerate(g[i]) if v == '#'])
    # 판별 flag
    flag = True
    nng = [] # 조사를 위한 필요 정보만 모아두는 틀
    for i in range(n):
        if ng[i] != []:
            nng.append(ng[i])
    nngl = [i for i, v in enumerate(ng) if v != []] # 비어있지 않은 리스트가 연속인가? 판별을 위함.
    if nngl != 1: # ng에서 연속 배치되지 않은 경우 판별
        for i in range(1, len(nngl)):
            if nngl[i] != nngl[i-1]+1:
                flag = False
                break
    lnng = len(nng)

    for i in range(lnng):
        if len(nng[i]) != lnng:
            flag = False
            break
    if lnng == 1 and len(nng[0]) == 1: # 1개만 있으면 True
        flag = True
    else:
        for i in range(1, lnng): # 순회하면서
            if flag == False:
                break
            if nng[i] != nng[i-1]: # 앞뒤로 담은 숫자가 다르면 False
                flag = False
                break
            for j in range(lnng):
                if nng[j][i-1]+1 != nng[j][i]: # 숫자가 연속되지 않았으면 False
                    flag = False
                    break
    if flag:
        print(f"#{testcase} yes")
    else:
        print(f"#{testcase} no") # 아;;; 여기에 # 붙이는거 까먹음

'''
잠만 생각 못해준 부분이 있음
1
3
##.
...
##.

에 대해서 판별을 잘못 할 듯 싶음.
해결 완료
'''