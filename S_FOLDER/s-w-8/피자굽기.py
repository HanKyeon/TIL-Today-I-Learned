'''
피자 굽기

피자 N개 동시굽기 가능
치즈 다 녹으면 꺼낸다. 피자마자 치즈 양 다름.
조건에 따라 피자를 구울 때 화덕에 마지막까지 남아있는 피자는?

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

입력
테케T
화덕크기 N 피자갯수M 3<=N<=20, N<=M<=100, 1<=Ci<=20
치즈C1 C2 C3 C4...

출력
#테케 마지막 남은 피자 번호
'''
from collections import deque

def pizza():
    global n, g
    hd = deque()
    for _ in range(n):
        hd.append(g.pop(0))
    while len(hd) > 1:
        idx, a = hd.popleft()
        a = a//2
        if a == 0:
            if g:
                hd.append(g.pop(0))
            if not g:
                continue
        else:
            hd.append((idx, a))
    return hd[0][0]

for testcase in range(1, int(input())+1):
    n, m = map(int, input().split())
    pl = [0]+list(map(int, input().split()))
    g = []
    for i, v in enumerate(pl):
        if i != 0:
            g.append((i, v))
    print(f"#{testcase} {pizza()}")
