'''
괄호 추가하기

길이가 n인 수식.
수식으 0이상 9이하 정수 및 연산자 제시.
연산자 우선순위는 모두 동일.
괄호를 맘껏 넣어도 된다.
최댓값 구해주기.
+ - * 셋으로만 제시.

괄호 안에는 연산자가 하나만 있어야 한다.

입력
수식 길이 제시.
수식 제시.

출력
최댓값
'''
from itertools import combinations
import sys
input = sys.stdin.readline

sz = '123456789'
ysz = '+-*'

n = int(input())
s = list(input().rstrip())
if n == 1:
    print(s[0])
else:
    nbz = []
    yszz = []
    for i in range(n):
        if s[i] in ysz:
            yszz.append(i//2)
        else:
            nbz.append(int(s[i]))
    yszn = (n//2)//2+1 if (n//2)%2 else (n//2)//2
    ans = -int(10e9)
    for i in range(1, yszn+1):
        for ys in combinations(yszz, i):
            fla = False
            ys = sorted(ys)
            for i in range(len(ys)-1):
                if abs(ys[i]-ys[i+1]) == 1:
                    fla = True
                    break
            if fla:
                continue
            nl = nbz[:]
            yv = [0]*(n//2)
            for gh in ys:
                if s[gh*2+1] == '+':
                    a, b = nl[gh], nl[gh+1]
                    nl[gh], nl[gh+1] = a+b, a+b
                    yv[gh] = 1
                elif s[gh*2+1] == '-':
                    a, b = nl[gh], nl[gh+1]
                    nl[gh], nl[gh+1] = a-b, a-b
                    yv[gh] = 1
                elif s[gh*2+1] == '*':
                    a, b = nl[gh], nl[gh+1]
                    nl[gh], nl[gh+1] = a*b, a*b
                    yv[gh] = 1
            Mans = nl.pop(0)
            yszjp = -1
            while nl:
                num = nl.pop(0)
                fla = yv.pop(0)
                yszjp += 2
                if fla:
                    continue
                elif s[yszjp] == '+':
                    Mans += num
                elif s[yszjp] == '-':
                    Mans -= num
                elif s[yszjp] == '*':
                    Mans *= num
            ans = max(ans, Mans)
    print(ans)

'''
# 빠른 코드

j=int
def g(x,y,c):return x+y if c=='+'else x-y if c=='-'else x*y
def f(i,c):return c if i>=n else max(f(i+2,g(c,j(s[i]),s[i-1])),f(i+4,g(c,g(j(s[i]),j(s[i+2]),s[i+1]),s[i-1]))if i<n-2 else -99)
n,s=j(input()),input()
print(f(2,j(s[0])))

#######
def calc(operand1, operand2, operater):
    if operater == '+':
        return int(operand1) + int(operand2)
    if operater == '-':
        return int(operand1) - int(operand2)
    if operater == '*':
        return int(operand1) * int(operand2)

answer = -float('inf')

def finder(result, rest):
    global answer
    if not rest:
        answer = max(answer, result)
        return

    #case1
    finder(calc(result, rest[1], rest[0]), rest[2:])

    #case2
    if len(rest) > 3:
        finder(calc(result, calc(rest[1], rest[3], rest[2]),rest[0]), rest[4:])

input()
expression = '+' + input()
finder(0, expression)

print(answer)
'''

















