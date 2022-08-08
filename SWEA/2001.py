'''
파리퇴치

N*N 배열에 파리갯수
M*M 파리채 크기
한번에 최대한 많이 잡기

입력


출력

'''
# 그래프와 사이즈를 받고 최대 벌레 반환
def bugcut (g, psize) :
    # 좌표를 받고 벌레 얼마나 잡는지 반환
    def bugsc (x, y, psize) :
        bugsum = 0
        for i in range(x, x + psize) :
            for j in range(y, y + psize) :
                bugsum += g[i][j]
        return bugsum
    # 실행
    ln = len(g)
    bug = []
    for i in range(ln - psize + 1) :
        for j in range(ln - psize + 1) :
            bug.append(bugsc(i, j, psize))
    return max(bug)

for testcase in range(1, int(input())+1) :
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{testcase} {bugcut(g, m)}")

