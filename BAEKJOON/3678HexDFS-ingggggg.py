'''
카탄의 개척자

벌집모양으로 만들어 갈 것이다.
새 타일은 이미 채워진 인접한 타일에 들어있는 자원과 다른 자원
보드에 존재하는 자원 중 가장 적은 자원 선택.
가능한 자원이 여러가지라면 가 작은 것을 선택.

빙글빙글 돌면서 시작한다. n번째 타일에 어떤 자원이 나타나는가?

입력
테케 t 제시.
정수 n 제시.

출력
n번째 타일에 들어있는 자원 출력.
'''
import sys
from collections import deque
input = sys.stdin.readline

# mov = [(0,-1),(1,-1),(1,0),(0,1),(-1,1),(-1,0)]
dh = [0,1,1,0,-1,-1]
dw = [-1,-1,0,1,1,0]
'''
0 0 0 0 0 0 0
0 0 0 A 9 8 0
0 0 B 2 1 7 0
0 C 3 0 6 I 0
0 D 4 5 H 0 0
0 E F G 0 0 0
0 0 0 0 0 0 0
'''
nz = [0, 6, 18, 36, 60, 90, 126, 168, 216, 270, 330, 396, 468, 546, 630, 720, 816, 918, 1026, 1140, 1260, 
1386, 1518, 1656, 1800, 1950, 2106, 2268, 2436, 2610, 2790, 2976, 3168, 3366, 3570, 3780, 3996, 4218, 4446, 4680, 4920, 5166, 5418, 5676, 5940, 6210, 6486, 6768, 7056, 7350, 7650, 7956, 8268, 8586, 8910, 9240, 9576, 9918, 10266]
def check(num):
    for i in range(59):
        if num > nz[i]+1:
            continue
        return i

def lego(num):
    if num <= 7:
        if num == 6:
            return 2
        if num == 7:
            return 3
        return num
    size = check(num)
    mtr = [1, 1, 0, 0, 0] # 0 1 2 3 4 로 재료 표기.
    size2 = 1+size*2
    g = [[-1]*(size2) for _ in range(size2)]
    g[size][size] = 0
    g[size-1][size+1] = 1
    q = deque([(size-1, size+1, 0)]) # h, w, di
    while q and num:
        h, w, di = q.popleft()
        num -= 1
        if di == 6:
            di = 0
        ndi = (di+1)%6
        nh, nw = h+dh[di], w+dw[di]
        nnh, nnw = h+dh[ndi], w+dw[ndi]
        if g[nnh][nnw] < 0:
            
            # 보드에 가장 적게 나타난 자원
            tg, val = -1, 10001
            hbg = sorted(list(hbg))
            for i in hbg:
                if mtr[i] < val:
                    tg = i
                    val = mtr[i]
            mtr[tg] += 1 # 카운트 증가
            print(mtr, hbg, num)
            # 큐 삽입
            g[nnh][nnw] = tg
            q.append((nnh, nnw, di+1))
        else:
            
            # 보드에 가장 적게 나타난 자원
            tg, val = -1, 10001
            hbg = sorted(list(hbg))
            for i in hbg:
                if mtr[i] < val:
                    tg = i
                    val = mtr[i]
            mtr[tg] += 1 # 카운트 증가
            print(mtr, hbg, num)
            # 큐 삽입
            g[nh][nw] = tg
            q.append((nh, nw, di))
        for i in g:
            print(i)
        print('================================================================')
    return tg+1


for _ in range(int(input())):
    n = int(input())
    print(lego(n))

'''
육각형 2차원을 만든다.
만든 뒤 확인 할 칸은 자신 주위 6칸으로 하기는 싫다.
내가 이전에 온 방향, 가려는 방향, 그 사이 방향

0 0 0 0 0 0 0
0 0 0 A 9 8 0
0 0 B 2 1 7 0
0 C 3 0 6 I 0
0 D 4 5 H 0 0
0 E F G 0 0 0
0 0 0 0 0 0 0

# 기본 육각형 순회.
# 이거는 일단 size를 정하는 함수
nl = [0]
for i in range(1, int(input())):
    # nl.append(nl[i-1] + (i*(i+1))//2 * 6)
    nl.append(nl[i-1] + i * 6)
print(nl)
# 육각형 만들기.
def lego(num):
    if num == 1: # 1개면 수동 계산해라.
        return
    size = check(num)
    mtr = [1, 1, 0, 0, 0] # 0 1 2 3 4 로 재료 표기.
    size2 = 1+size*2
    g = [[-1]*(size2) for _ in range(size2)]
    g[size][size] = 0
    g[size-1][size+1] = 1
    q = deque([(size-1, size+1, 0)]) # h, w, di, rot
    cnt = 1
    while q:
        h, w, di = q.popleft()
        cnt+=1
        if cnt == num:
            break
        if di == 6:
            di = 0
        ndi = (di+1)%6
        nh, nw = h+dh[di], w+dw[di]
        nnh, nnw = h+dh[ndi], w+dw[ndi]
        if g[nnh][nnw] < 0:
            g[nnh][nnw] = cnt
            q.append((nnh, nnw, di+1))
        else:
            g[nh][nw] = cnt
            q.append((nh, nw, di))
'''


