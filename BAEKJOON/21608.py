'''
상어 초등학교

n*n 교실 n**2 학생 수
r,c는 r행 c열. 1,1로 시작, n,n끝 학생순서, 학생이 좋아하는 학생 4명 조사.
칸 당 하나 |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다. -> 사방인접

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러개면 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로.

선호 학생 인접 수 우선, 인접 빈칸 수 우선, 좌상단 우선.

자리배치 이후 만족도. 주변에 앉은 좋아하는 애 수 0 0, 1or2 10, 3 100, 4 1000
학생 만족도의 총합.

입력
n 3이상 20이하
학생번호 선호4학생 n**2만큼 제시.

출력
만족도 총 합
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

n = int(input())
g = [[0]*n for _ in range(n)]
dic = {}
sit = set()
for i in range(n**2):
    idx, l1, l2, l3, l4 = map(int, input().rstrip().split())
    dic[idx] = set([l1, l2, l3, l4])
    nsits = []
    for i in range(n):
        for j in range(n):
            if (i, j) in sit:
                continue
            # [fz, zs, h, w]
            fz, zs = 0, 0
            for k in range(4):
                ni, nj = i + dh[k], j + dw[k]
                if 0<=ni<n and 0<=nj<n:
                    if g[ni][nj] == 0:
                        zs+=1
                    elif g[ni][nj] in dic[idx]:
                        fz+=1
            if nsits and nsits[0][0] < -fz:
                continue
            heappush(nsits, [-fz, -zs, i, j])
    frnz, zerz, h, w = heappop(nsits)
    sit.add((h, w))
    g[h][w] = idx


score = [0]*5
for i in range(n):
    for j in range(n):
        bgr = dic[g[i][j]]
        c = 0
        for k in range(4):
            ni, nj = i + dh[k], j + dw[k]
            if 0<=ni<n and 0<=nj<n and g[ni][nj] in bgr:
                c+=1
        # print(g[i][j], c)
        # print(bgr)
        score[c] += 1
# print(dic)
# for i in g:
#     print(*i)
# print(score)
ans = score[1] + score[2]*10 + score[3]*100 + score[4]*1000
print(ans)




'''
2 2 1 2 3 2 1 1 0
'''
