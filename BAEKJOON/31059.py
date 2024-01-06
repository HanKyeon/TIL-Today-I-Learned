'''
건초 분포

n개의 곳간. 정수좌표 위.
존은 n개의 건초를 임의의 좌표 y로 배달하고 각 곳간에 배분할거임
슬프게도 ㅈㄴ 낭비임. 특히 ai와 bi 건초에서 ai 건초는 왼쪽으로 가느라 낭비되고 bi는 오른쪽으로 가느라 낭비됨.
x에서 y로 가는데 낭비식 있음.

(x > y ? bi : ai) * abs(x-y)

Q개의 쿼리 날릴 것. ai, bi
적당한 y값을 골라서 손실 최소화 해라

입력
n 제시
x라인 제시
q 제시
q개 줄 ai bi 제시

출력
쿼리에 대한 해답 제시
'''
'''
100,000 * 100,000 * 1,000,000
2초
'''
import sys
input = sys.stdin.readline

def getWasted(x, y):
    global a, b
    return (x-y)*b if x > y else (y-x)*a

def lego(y):
    global a, b
    ret = 0
    for x in nl: ret += getWasted(x, y)
    return ret

n = int(input())
nl = list(map(int, input().rstrip().split())); nl.sort()
ans = []
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    test = []
    for i in range(nl[-1]):
        test.append(lego(i))
        # print(lego(i), end=', ')
    print(f"a는 {a}, b는 {b}: {test}")
'''
1 2 3 4 10
합은 20
'''