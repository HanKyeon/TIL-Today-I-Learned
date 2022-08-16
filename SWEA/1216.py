'''
회문 2

가장 긴 회문의 길이를 출력
'''
# 길이를 받아서 회문 갯수를 반환하는 함수
def hm(hl) :
    a = len(g) # 그래프 크기를 내부에서 받아줘야함
    c = 0 # 갯수 세기
    # 인덱스가 0이상 a-hl이하여야 hl길이의 회문을 찾을 수 있다.
    for i in range(a-hl+1) :
        for j in range(a) :
            p, q = g[j][i:i+hl], s[j][i:i+hl]
            if p[:] == p[::-1] :
                c += 1
            if q[:] == q[::-1] :
                c += 1
    return c

for t in range(1, 11) :
    # 입력
    n = 100
    hl = int(input())
    g = [list(input()) for _ in range(n)]
    s = [[] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            s[i] += g[j][i]
    # 회문 길이 비교
    l = 0
    for i in range(1, n+1) :
        if hm(i) != 0 :
            l = max(l, i)
    #출력
    # g, s에 대해 길이로 hm 함수 실행
    print(f"#{t} {l}")

'''
시간 줄이기.
def hm(hl) :
    for i in range(100-hl+1) :
        for j in range(100) :
            p, q = g[j][i:i+hl], s[j][i:i+hl]
            if p == p[::-1] :
                return True
            if q == q[::-1] :
                return True
    return False

for t in range(1, 11) :
    _ = input()
    g = [input() for _ in range(100)]
    s = [''.join(x) for x in zip(*g)] # 이 부분에서 시간을 줄일 수 있다.

    for i in range(100, 0, -1) :
        if hm(i):
            l = i
            break
    print(f"#{t} {l}")

'''


