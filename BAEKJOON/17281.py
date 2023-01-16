'''
⚾

⚾은 9인 2팀이 공 수 번갈아 한다. 공수가 1이닝. n이닝 진행. 3아웃 시 공수 변경
경기 시작 전 타순을 정해야 하고 경기 중에는 변경 불가능. 9번 타자까지 쳤는데 3아웃 아니면 1번타자부터 시작. 타순은 이닝이 변경되어도 순서를 유지해야 한다. 2이닝에 6이 마지막이면 3은 7부터 시작.
타자가 공을 쳐서 얻을 수 있는 결과는 안타 2루타 3루타 홈런 아웃 중 하나.
안타 : 타자와 모든 주자 1루 전진
2루타 : 2루
3루타 : 3루
홈런 : 홈까지
아웃 : 진루 못하고 아웃 증가

총 9명의 선수, 1부터 9까지 번호. 1번 선수가 4번 타자이다. 각 선수가 각 이닝에서 어떤 결과를 얻는지 미리 알고 있다면 가장 많이 득점하는 타순을 찾고 그 때의 득점을 구하자.

입력
이닝 수 n 제시.
n개 줄에는 각 선수가 얻는 결과가 1이닝부터 n이닝까지 순서대로 제시.
안타 1 2루2 3루3 홈4 아웃0
아웃은 무조건 존재.

출력
'''
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
nl = [1,2,3,4,5,6,7,8]
ans = 0
for permu in permutations(nl, 8):
    ss = []
    for i in permu:
        if len(ss) == 3:
            ss.append(0)
        ss.append(i)
    pointer = 0
    ret = 0
    for i in g:
        ggp = [i[x] for x in ss]
        o, b1, b2, b3 = 0, 0, 0, 0
        while o != 3:
            sj = ggp[pointer]
            if not sj:
                o += 1
            elif sj == 1:
                ret += b3
                b1,b2,b3 = 1,b1,b2
            elif sj == 2:
                ret += b3+b2
                b1,b2,b3 = 0,1,b1
            elif sj == 3:
                ret += b1+b2+b3
                b1,b2,b3 = 0,0,1
            elif sj == 4:
                ret += b1+b2+b3+1
                b1,b2,b3=0,0,0
            pointer += 1
            if pointer == 9:
                pointer = 0
    if ret > ans:
        ans = ret
print(ans)

n = int(input())
p = list(permutations([x for x in range(1, 9)], 8))
board = [list(map(int, input().split(' '))) for x in range(n)]
answer = 0

for i in set(p):
    order = list(i[:3]) + [0] + list(i[3:])
    score = 0
    index = 0
    for inning in range(n):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out != 3:
            if board[inning][order[index]] == 0:
                out += 1
            elif board[inning][order[index]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif board[inning][order[index]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif board[inning][order[index]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif board[inning][order[index]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            index += 1
            if index == 9:
                index = 0

    answer = max(answer, score)
print(answer)

'''
def lego(num):
    point = 0
    for i in range(3, -1, -1):
        if zr[i]:
            if i+num > 3:
                point += 1
            else:
                zr[i+num] = 1
            zr[i] = 0
    return point

n = int(input())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
nl = [1,2,3,4,5,6,7,8]
ans = 0
for permu in permutations(nl, 8):
    ss = []
    for i in permu:
        if len(ss) == 3:
            ss.append(0)
        ss.append(i)
    pointer = 0
    ret = 0
    for i in g:
        ggp = [i[x] for x in ss]
        zr, o = [0, 0, 0, 0], 0
        while o != 3:
            if not ggp[pointer]:
                o += 1
            else:
                zr[0] = 1
                ret += lego(ggp[pointer])
            pointer += 1
            if pointer == 9:
                pointer = 0
    if ret > ans:
        ans = ret
print(ans)
'''