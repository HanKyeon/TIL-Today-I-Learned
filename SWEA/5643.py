'''
키 순서

입력
테케T 1~15
학생수N 2~500
키비교횟수M (0 ≤ M ≤ N*(N-1)/2)
작은애 큰애
작은애 큰애 ...

출력
#테케 자기 키를 알 수 있는 애들
'''

def 큰놈(num): # num보다 큰놈 찾기
    v[num] = 1 # visited
    for i in bl[num]: # big list
        if v[i] == 0:
            큰놈(i)
    return

def 작은놈(num): # num보다 작은놈 찾기
    v[num] = 1 # visited
    for i in sl[num]: #small list
        if v[i] == 0:
            작은놈(i)
    return

for testcase in range(1, int(input())+1):
    # 입력
    n = int(input()) # 사람 수
    m = int(input()) # 간선 수
    # vvv 아래 변수는 index 기준 지들보다 큰놈들 big list 기록, 작은놈들 small list 기록
    bl, sl = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
    for _ in range(m):
        s, b = map(int, input().split()) # small big
        bl[s].append(b)
        sl[b].append(s)
    c = 0
    for i in range(n+1):
        v = [0] * (n+1) # 반복마다 visited 초기화
        큰놈(i) # 큰놈들 방문처리
        작은놈(i) # 작은놈들 방문처리
        if sum(v) == n: # 방문처리된 합이 n이면
            c += 1
    print(f"#{testcase} {c}") # 출력



'''
from copy import deepcopy

def 큼(num):
    bl, sl = deepcopy(bb), deepcopy(ss)
    li, sli, al = [num], [num], [num]
    while li: # 키 큰애들 리스트
        nn = li.pop()
        if not bl[nn]:
            continue
        for _ in range(len(bl[nn])):
            a = bl[nn].pop()
            if not a in li:
                li.append(a)
            if not a in al:
                al.append(a)
    # 키 작은 애들 리스트 조작
    while sli:
        nn2 = sli.pop()
        if not sl[nn2]:
            continue
        for _ in range(len(sl[nn2])):
            b = sl[nn2].pop()
            if not b in sli:
                sli.append(b)
            if not b in al:
                al.append(b)
    return len(al)

for testcase in range(1, int(input())+1):
    n = int(input())
    m = int(input())
    kl = [list(map(int, input().split())) for _ in range(m)]
    bb, ss = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
    for s, b in kl:
        bb[s].append(b)
        ss[b].append(s)
    c = 0
    for i in range(1, n+1):
        if 큼(i) == n:
            c+=1
    print(f"#{testcase} {c}")
'''


