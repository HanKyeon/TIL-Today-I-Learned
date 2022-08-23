'''
토너먼트 카드게임.

1가위 2바위 3보
같은 카드일 경우 번호가 작은 쪽의 승리.
1등 찾기

입력
테케T 1이상 50이하
인원수 N
N명이 고른 카드들~
반복

출력
#테케 승리자 번호
'''
def sol(sta, end):
    if sta == end:
        return sta+1 # 인덱스 리턴
    mid = (sta+end)//2
    a = sol(sta, mid)
    b = sol(mid+1, end)
    return wl(a, b)

def wl(p1, p2):
    if (pc[p1]+1) % 3 == pc[p2] % 3: # 승패처리. 하나 늘려서 3으로 나눈 나머지가 같다면
        return p2 # p2 승
    elif pc[p1] % 3 == (pc[p2]+1) % 3: # 승패처리.
        return p1 # p1 승
    elif pc[p1] == pc[p2]: # 둘이 같으면
        if p1<p2:return p1 # 작은놈
        if p2>p1:return p2 # 이 이김

for testcase in range(1, int(input())+1):
    n = int(input())
    nr = list(range(1, n+1)) # 넘버링
    nl = list(map(int, input().split())) # 뭐 냈나
    pc = {} # 홀수 일 때를 위해 -1은 -1이라는 딕트값 추가
    for i, v in zip(nr, nl): # 사람번호를 key로 가진 카드를 dict에 담음.
        pc[i] = v
    if n == 1: # 1명일 때 예외처리
        print(f"#{testcase} {nl[0]}")
        continue
    print(f"#{testcase} {sol(0, n-1)}")
    # print(f"#{testcase} {wl(al[0], al[1])}")
'''
def sol(sta, end):
    if sta == end:
        return sta
    mid = (sta+end)//2
    a = sol(sta, mid)
    b = sol(mid+1, end)

    return wl(wl(pc[a], pc[b]))


for testcase in range(1, int(input())+1):
    n = int(input())
    g = [0] + list(map(int, input().split()))
    ans = sol(1, n)
    print(f"#{testcase} {ans}")





def qs(sta, end, li):
    if len(li) == 1:
        return li[0][0]
    if len(li) == 2:
        return wl(li[0][0], li[1][0])

    mid = (sta+end)//2
    rs, ls = li[:mid], li[mid:]
    return wl(qs(sta, mid, ls), qs(mid+1, end, rs))

def wl(p1, p2):
    if pc[p2] == -1: # p2가 -1이면 p1이 승리. -1은 p2쪽에만 담긴다.
        return p1
    if pc[p1] == -1: # 근데 그래도 해줘봄
        return p2

    if (pc[p1]+1) % 3 == pc[p2] % 3: # 승패처리. 하나 늘려서 3으로 나눈 나머지가 같다면
        return p2 # p2 승
    elif pc[p1] % 3 == (pc[p2]+1) % 3: # 승패처리.
        return p1 # p1 승
    elif pc[p1] == pc[p2]: # 둘이 같으면
        if p1<p2:return p1 # 작은놈
        if p2>p1:return p2 # 이 이김

for testcase in range(1, int(input())+1):
    n = int(input())
    nr = list(range(1, n+1)) # 넘버링
    nl = list(map(int, input().split())) # 뭐 냈나
    pc = {-1:-1} # 홀수 일 때를 위해 -1은 -1이라는 딕트값 추가
    for i, v in zip(nr, nl): # 사람번호를 key로 가진 카드를 dict에 담음.
        pc[i] = v
    if n == 1: # 1명일 때 예외처리
        print(f"#{testcase} {nl[0]}")
        continue
    print(qs(0, n-1, list(zip(nr, nl))))
    # print(f"#{testcase} {wl(al[0], al[1])}")
'''























def lrs(li):
    a = len(li)//2 # 길이 반 이 아니라 i+j // 2다 그지같은 문제
    ls = li[:a] # 그만큼
    rs = li[a:] # 반
    # if len(rs) % 2 == 1: # 홀수면 그래서 홀수처리 필요 없는듯
    #     rs += [-1] # 임의 하나 더해줌
    # if len(ls) % 2 == 1: # 홀수면
    #     ls += [-1] # 임의 하나 더해줌
    w = [] # 승자들
    for i in range(0, len(ls), 2): # ls 스텝2로 순회하면서
        w.append(wl(ls[i], ls[i+1])) # 승자들 담아줘라
    for i in range(0, len(rs), 2): # rs도 스텝2로 순회하면서
        w.append(wl(rs[i], rs[i+1])) # 승자들 담아줘라
    return w # 승자들 리스트 반환.
# 승패 판정 번호 받아서 dict 값을 비교.
def wl(p1, p2):
    if pc[p2] == -1: # p2가 -1이면 p1이 승리. -1은 p2쪽에만 담긴다.
        return p1
    if pc[p1] == -1: # 근데 그래도 해줘봄
        return p2

    if (pc[p1]+1) % 3 == pc[p2] % 3: # 승패처리. 하나 늘려서 3으로 나눈 나머지가 같다면
        return p2 # p2 승
    elif pc[p1] % 3 == (pc[p2]+1) % 3: # 승패처리.
        return p1 # p1 승
    elif pc[p1] == pc[p2]: # 둘이 같으면
        if p1<p2:return p1 # 작은놈
        if p2>p1:return p2 # 이 이김

for testcase in range(1, int(input())+1):
    n = int(input())
    nr = list(range(1, n+1)) # 넘버링
    nl = list(map(int, input().split())) # 뭐 냈나
    if n == 1: # 1명일 때 예외처리
        print(f"#{testcase} {nl[0]}")
        continue
    pc = {-1:-1} # 홀수 일 때를 위해 -1은 -1이라는 딕트값 추가
    for i, v in zip(nr, nl): # 사람번호를 key로 가진 카드를 dict에 담음.
        pc[i] = v
    al = nr # 1부터 n까지 리스트
    while len(al) > 2: # 2개 될 때까지 한다
        al = lrs(al)
    print(f"#{testcase} {wl(al[0], al[1])}")






