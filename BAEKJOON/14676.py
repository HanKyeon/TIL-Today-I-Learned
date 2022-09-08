'''
영우는 사기꾼?

ACM 크래프트인데 이제 대결하는. 치트키 사용 여부 판단하는 프로그램 작성.

입력
건물 종류 갯수N 건물 사이 관계 갯수M 영우 게임정보K 셋다 1이상 10만이하
m줄에 걸쳐 X Y 제시. x를 건설해야 y를 지을 수 있다.
k줄에 걸쳐 영우 게임 정보 제시.
1 a : 영우가 a번 건물을 1개 건설함
2 a : 영우의 a번 건물이 1개 파괴됨.

출력
정상적으로 건물을 건설하거나, 건설한 만큼의 건물만 파괴되었다면 'King-God-Emperor', 건설할 수 없는 건물을 건설하거나, 건설한적 없는 건물이 파괴되었다면 'Lier!' 출력
'''
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
reqn = [0] * (n+1)
g = [[] for _ in range(n+1)]
rg = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # x->y
    reqn[b] += 1
    g[a].append(b)
    rg[b].append(a)
fla = False # 치트를 썻냐? 의 대답
sets = []
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    if fla:
        continue
    if a == 1:
        if reqn[b] > 0:
            fla = True
            continue
        if not b in sets:
            for i in g[b]:
                reqn[i] -= 1
        sets.append(b)
    if a == 2:
        if not b in sets:
            fla = True
            continue
        sets.remove(b)
        if not b in sets:
            for i in g[b]:
                reqn[i] += 1
if fla:
    ans = 'Lier!'
else:
    ans = 'King-God-Emperor'
print(ans)








