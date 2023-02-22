'''
한조 대기 중

n명 플레이어. 같은 팀에서 여러 명이 한 영웅 픽 불가. m개의 영웅은 게임 승패를 결정지을 정도로 구리다.
m개 트롤픽 중 원하는 트롤픽을 말하고 많은 팀원이 즐겜 할 수 있도록 트롤픽 분배.
트롤픽을 적게 한 팀이 이긴다. 트롤픽 리스트가 주어지 때, 그마 찍을 수 있는가? 비기면 승급x 이겨야 한다.

입력
플레이어 수 트롤픽 수 원하는 트롤픽 갯수 n, m, k1, k2 제시
k1개 줄 i, j 제시. i번 플레이어가 j번 픽 원함
k2개 줄 i, j 제시. i번 플레이어가 j번 원한다.

출력
승급 할 수 있으면 "네 다음 힐딱이" 없다면 "그만 알아보자"
'''
import sys
input = sys.stdin.readline

def matching(idx, tn):
    if tn:
        for i in g1[idx]:
            if v[i]:
                continue
            v[i] = 1
            if not connect1[i] or matching(connect1[i], tn):
                connect1[i] = idx
                return True
        return False
    for i in g2[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect2[i] or matching(connect2[i], tn):
            connect2[i] = idx
            return True
    return False

n, m, k1, k2 = map(int, input().rstrip().split())
g1 = [[] for _ in range(n+1)]
g2 = [[] for _ in range(n+1)]
for _ in range(k1):
    i, j = map(int, input().rstrip().split())
    g1[i].append(j)
for _ in range(k2):
    i, j = map(int, input().rstrip().split())
    g2[i].append(j)

connect1, connect2 = [0]*(m+1), [0]*(m+1)
ans1, ans2 = 0, 0
for i in range(1, n+1):
    v = [0]*(m+1)
    a = matching(i, 1)
    if a:
        ans1 += 1
    v = [0]*(m+1)
    b = matching(i, 0)
    if b:
        ans2 += 1
if ans2 > ans1:
    print("네 다음 힐딱이")
else:
    print("그만 알아보자")






