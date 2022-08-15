'''
격자판 칠하기

N*M 직사각형 격자판. 단위 1*1 검은색이나 흰색으로 칠할 것
몇개를 검은색으로 칠할지 흰색으로 칠할지 정해줌. 0이상 NM이하
#일 경우 검은색 .이면 흰색 ?는 몰?루
정해지지 않은 칸들을 어떤 색으로 할 지 정한 뒤 격자판 칠 할 것이다.
인접한 칸의 색이 항상 다르게 할 수 있는지 판단하는 프로그램 출력

입력
테케
세로n 가로m 1이상50이하 둘다
행렬A #.?????.####.... n번 주어짐

출력
가능하면 possible
불가능하면 impossible
#.#.#.#.
.#.#.#.#
'''
def dotsharp():
    global n, m
    s, d = [], [] # sharp와 dot 좌표 받을 리스트
    # (i+j)%2 값으로 받으면 체스판 문제는 쉽다!
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                s.append((i+j)%2)
            elif g[i][j] == '.':
                d.append((i+j)%2)
            else : continue
    if (1 in s and 0 in s) or (1 in d and 0 in d): # 각각 지그재그가 안되면
        return 'impossible'
    if d == [] or s == [] : # 한쪽이 하나로 통일 되어있고 한쪽이 비어있으면
        return 'possible'
    if bool(sum(s)) == bool(sum(d)) : # 양쪽의 i+j 의 홀짝 여부가 동일하다면
        return 'impossible'
    return 'possible'

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split()) # n, m 입력
    g = [list(input()) for _ in range(n)] # 표 입력 받기
    print(f"#{testcase} {dotsharp()}") # 실행 및 출력
