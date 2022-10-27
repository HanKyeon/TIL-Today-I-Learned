'''
정육면체 전개도

전개도 만들 수 있다.
6줄에 걸쳐 전개도 하나씩 제시.
판별

입력
3개 데이터, 6개줄. 1은 정사각형, 떨어져 있는 경우는 없다.

출력
세개 줄에 걸쳐 입력된 순서대로 전개도가 정육면체의 전개도면 yes 아니면 no
'''
import sys
input = sys.stdin.readline

# 1 4 1
# 3 3
# 2 2 2
# 2 3 1
# 1 1 2 1 1
# 82% 쯤 틀렸습니다.

zgd = {(0,2,0,0,1,0,0), (0,0,3,0,0,0,0), (0,1,1,1,0,0,0), (0,3,0,1,0,0,0), (0,2,2,0,0,0,0)}

def lego():
    ret = True
    g = [list(map(int, input().rstrip().split())) for _ in range(6)]
    s = list(map(list, zip(*g)))
    # 가로 세로 길이 구하기
    mh, Mh, mw, Mw = 8, 0, 8, 0
    for i in range(6):
        for j in range(6):
            if g[i][j]:
                mh, Mh, mw, Mw = min(mh, i), max(Mh, i), min(mw, j), max(Mw, j)
    gli, sli = [], []
    ori, cpi = [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]
    for i in g:
        si = sum(i)
        if si:
            gli.append(si)
            ori[si] += 1
    for i in s:
        si = sum(i)
        if si:
            sli.append(si)
            cpi[si] += 1
    ori, cpi = tuple(ori), tuple(cpi)
    h, w = Mh-mh+1, Mw-mw+1
    if h*w == 10:
        if (ori == (0,0,0,2,0,0,0) and cpi == (0,4,1,0,0,0,0)) or (cpi == (0,0,0,2,0,0,0) and ori == (0,4,1,0,0,0,0)):
            pass
        else:
            ret = False
    elif h*w == 12:
        if ori in zgd and cpi in zgd:
            if ori == (0,2,0,0,1,0,0):
                if gli == [1,4,1]:
                    pass
                else: ret = False
            if cpi == (0,2,0,0,1,0,0):
                if sli == [1,4,1]:
                    pass
                else: ret = False
            if ori == (0,1,1,1,0,0,0):
                if gli == [1,2,3] or gli == [3,2,1]:
                    ret = False
            if cpi == (0,1,1,1,0,0,0):
                if sli == [1,2,3] or sli == [3,2,1]:
                    ret = False
        else:
            ret = False
    else:
        ret = False

    if ret:
        return 'yes'
    else:
        return 'no'

for _ in range(3):
    print(lego())



'''
# 전개도 부분 빼기
    mh, Mh, mw, Mw = 8, 0, 8, 0
    for i in range(6):
        for j in range(6):
            if g[i][j]:
                mh, Mh, mw, Mw = min(mh, i), max(Mh, i), min(mw, j), max(Mw, j)
    zgd = []
    for i in range(mh, Mh+1):
        zgd.append(g[i][mw:Mw+1])
    for i in zgd:
        print(i)
'''
'''
1 0 0 0 0 0
1 1 1 1 0 0
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

1 0 0 0 0 0
1 0 0 0 0 0
1 1 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

1 0 0 0 0 0
1 1 0 0 0 0
0 1 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

0 0 0 1 0 0
0 1 1 1 0 0
1 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
'''