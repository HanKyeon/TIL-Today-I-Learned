'''
길찾기

방향성 그래프.
노드 99개. 출발점0 도작점 99
출발/노드 제외 98개 아래
한개의 정점에서 최대 2개

입력
각 테케 첫 줄에는 테케 번호와 간선의 총 갯수 제시
순서쌍. 나열한 대로 순서쌍임.

출력
#테케 도착가능1? 도착 불가능0?
'''
def dfs(num):
    v[num] = 1
    for i in g[num]:
        if v[i] == 0 :
            dfs(i)

def dfs2(num):
    li = [num]
    while li:
        nn = li.pop()
        v[nn] = 1
        for i in g[nn]:
            if v[i] == 0 and not (i in li):
                li.append(i)

for testcase in range(1, 11):
    _, l = map(int, input().split())
    nl = list(map(int, input().split()))
    g = [[] for _ in range(100)]
    v = [0]*100
    for i in range(0, 2*l, 2):
        g[nl[i]].append(nl[i+1])
    dfs2(0)
    print(f"#{testcase} {v[99]}")