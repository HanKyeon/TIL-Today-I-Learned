'''
사칙연산

입력
정점의 총 수 n 제시.
n줄에 걸쳐 정점 정보 제시.
정점 번호는 1부터 N까지 정수.
루트 정점 번호 1
a, b, c, d
a는 해당 정점, b는 그 정점 값, c는 좌식, d는 우식
정점 번호 매기는 특별한 규칙 x
'''
ysz = '+-*/'

def 계산(num):
    l, r = hnz[num]
    if l==0 and r==0:
        return g[num]
    a = g[num]
    if a in ysz:
        if a == '+':
            return 계산(l)+계산(r)
        elif a == '-':
            return 계산(l)-계산(r)
        elif a == '*':
            return 계산(l)*계산(r)
        elif a == '/':
            return 계산(l)/계산(r)

for testcase in range(1, 11):
    n = int(input())
    g = [0] * (n+1)
    hnz = [[0, 0] for _ in range(n+1)]
    for _ in range(n):
        s = input().rstrip().split()
        if len(s) == 4:
            nod, val, lft, rgt = s
            nod = int(nod)
            if val in ysz:
                g[nod] = val
            else:
                g[nod] = int(val)
            hnz[nod][0] = int(lft)
            hnz[nod][1] = int(rgt)
        elif len(s) == 3:
            nod, val, lft = s
            nod = int(nod)
            if val in ysz:
                g[nod] = val
            else:
                g[nod] = int(val)
            hnz[nod][0] = int(lft)
        elif len(s) == 2:
            nod, val = s
            nod = int(nod)
            if val in ysz:
                g[nod] = val
            else:
                g[nod] = int(val)
    # 계산하기
    print(f"#{testcase} {int(계산(1))}")



'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65

    -
  - 10
88 65
'''









