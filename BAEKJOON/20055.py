'''
컨베이어 벨트 위의 로봇

길이 n 컨베이어 벨드.
길이 2n 벨트가 위 아래 감싸고 도는 중.
벨트가 한 칸 회전하면 1번부터 2n-1번까지 칸은 다음 번호의 칸이 있는 위치로 이동, 2n번 칸은 1번 ㅏㄴ의 위치로 이동.
i번 칸의 내구도는 Ai이다. 1번 칸의 위치를 올리는 위치, n번 칸의 위치를 내리는 위치. (윗줄)

1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동 할 수 있다면 이동한다. 이동 할 수 없다면 가만히 있는다. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 갯수가 k개 이상이라면 과정 종료.
종료 되었을 대, 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번 단계부터이다.

입력
n, k 제시.
a1, ... , a2n 제시.

출력
몇번째 단계가 진행 중일 때 종료 되었는지 출력.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
cb = list(map(int, input().rstrip().split()))
rbt = [0]*(2*n)
inn, outt = 0, n-1
ans, cnt = 0, 0
while cnt < k:
    ans += 1
    inn, outt = inn-1, outt-1
    if inn == -1:
        inn = 2*n-1
    if outt == -1:
        outt = 2*n-1

    rbt[outt] = 0

    i = outt
    while i != inn:
        if not cb[i] or rbt[i] or not rbt[i-1]:
            i -= 1
            if i == -1:
                i = 2*n-1
            continue
        rbt[i], rbt[i-1] = rbt[i-1], rbt[i]
        cb[i] -= 1
        if not cb[i]:
            cnt += 1
        i -= 1
        if i == -1:
            i = 2*n-1

    rbt[outt] = 0

    if cb[inn]:
        rbt[inn] = 1
        cb[inn] -= 1
        if not cb[inn]:
            cnt += 1

print(ans)
















'''
n, k = map(int, input().rstrip().split())
cb = list(map(int, input().rstrip().split()))
rbt = [0]*(2*n)
inn, outt = 0, n-1
ans, cnt = 0, 0
while cnt < k:
    ans += 1
    cb.insert(0, cb.pop())
    rbt.insert(0, rbt.pop())
    if rbt[n-1]:
        rbt[n-1] = 0
        cb[n-1] -= 1
        if not cb[n-1]:
            cnt+=1
    print(cb)
    print(rbt)
    print('==')
    for i in range(n-1, -1, -1):
        if not rbt[i]:
            continue
        if cb[i+1] and not rbt[i+1]:
            rbt[i], rbt[i+1] = rbt[i], rbt[i+1]
            cb[i+1] -= 1
            if not cb[i+1]:
                cnt += 1
    print(cb)
    print(rbt)
    print('==')
    if rbt[n-1]:
        rbt[n-1] = 0
        cb[n-1] -= 1
        if not cb[n-1]:
            cnt+=1
    if cb[0]:
        rbt[0] = 1

print(ans)
'''










'''
n, k = map(int, input().rstrip().split())
cb = list(map(int, input().rstrip().split()))
rbt = [0]*(2*n)
inn, outt = 0, n-1
ans, cnt = 0, 0
while cnt < k:
    ans += 1
    inn, outt = inn-1, outt-1
    if inn == -1:
        inn = 2*n-1
    if outt == -1:
        outt = 2*n-1
    cb.append(cb.pop(0))

    if rbt[outt]:
        cb[outt] -= 1
        rbt[outt] = 0
        if not cb[outt]:
            cnt+=1

    i = outt
    while i != inn:
        if not cb[i] or rbt[i]:
            i -= 1
            if i == -1:
                i = 2*n-1
            continue
        rbt[i], rbt[i-1] = rbt[i-1], rbt[i]
        i -= 1
        if i == -1:
            i = 2*n-1

    if rbt[outt]:
        cb[outt] -= 1
        rbt[outt] = 0
        if not cb[outt]:
            cnt+=1
    
    if cb[inn]:
        rbt[inn] = 1
    print(ans, inn, outt, cnt)
    print(cb)
    print(rbt)

print(ans)

'''
