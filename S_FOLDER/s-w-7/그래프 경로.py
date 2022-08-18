'''
그래프 경로

V개 이내 노드를 E개 간선으로 연결한 **방향성** 그래프에 대해
특정 두개의 노드에 경로를 확인하는 프로그램 작성

입력
테케T
노드 갯수 간선 갯수 5이상 50이하, 4이상 1000이하
시작노드, 도착노드

'''
def 함수(sta, end):
    if sta == end:
        return 1
    li = [sta]
    while li:
        nst = li.pop()
        v[nst] = 1
        if v[end] == 1:
            return 1
        for i in g[nst]:
            if v[i] == 0 and not (i in li):
                li.append(i)
    return 0

for testcase in range(1, int(input())+1):
    ns, ls = map(int, input().split())
    g = [[] for _ in range(ns+1)]
    v = [0]*(ns+1)
    for i in range(ls):
        st, en = map(int, input().split())
        g[st].append(en)
    s, e = map(int, input().split())
    c = 함수(s, e)
    print(f"#{testcase} {c}")

