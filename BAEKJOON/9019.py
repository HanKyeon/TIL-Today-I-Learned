'''
DSLR

0이상 1만 미만 십진수 저장 가능.
각 자리가 d1 d2 d3 d4

1. D : D는 n을 두배로 바꾼다. 9999 넘어가면 10000으로 나눈 나머지만 취한다. 그 결괏값 저장.
2. S : S는 n에서 1 뺀 결과인 n-1을 저장한다. n이 0이라면 9999가 저장.
3. L : 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장. 1234가 2341이 된다.
4. R : 오른쪽 회전. 1234가 4123이 된다.

L과 R 명령어는 십진 자릿수를 가정하고 연산 수행.
주어진 서로 다른 두 정수 A와 B에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램.
A = 1234, B - 3412라면 LL 혹은 RR로 가능.

입력
테케T
A B 공백 구분 제시. 초깃값과 최종값.

BFS
A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력. 여러개라면 아무거나 출력.
'''
'''
S 연산에서 n이 0이라면이다. n-1이 0이라면이 아님....
'''
from collections import deque
import sys
input = sys.stdin.readline

def D(num): # D연산
    num = (num*2)%10000
    return num
def S(num): # S연산
    num -= 1
    if num == -1:
        num = 9999
    return num
def L(num): # L연산
    return (num%1000) * 10 + num//1000
def R(num): # R연산
    return (num%10)*1000 + num//10

# 방문처리를 set()로 해줬는데 생각해보니 visited = [0]*10000으로 해도 된다. 해봤자 1만번 연산이었다.
for _ in range(int(input())):
    a, b = map(int, input().split()) # 시작값, 목표값
    sets = set() # 중복값 넣지 않을것임. 먼저 들어간게 짧은 것이므로.
    q = deque() # BFS 할거임
    q.append((a, '')) # 숫자랑 정답
    sets.add(a) # 중복값 넣지 않기 위해 set에 넣어줌.
    # ret = ''
    while q:
        num, ans = q.popleft()
        if num == b:
            break
        nl = [D(num), S(num), L(num), R(num)]
        for i in range(4):
            if nl[i] in sets:
                continue
            else:
                sets.add(nl[i])
                if i == 0:
                    # print('D', nl[i])
                    q.append((nl[i], ans+'D'))
                elif i == 1:
                    # print('S', nl[i])
                    q.append((nl[i], ans+'S'))
                elif i == 2:
                    # print('L', nl[i])
                    q.append((nl[i], ans+'L'))
                elif i == 3:
                    # print('R', nl[i])
                    q.append((nl[i], ans+'R'))
    print(ans)


'''
def L(num):
    d4 = num % 10
    num //= 10
    d3 = num % 10
    num //= 10
    d2 = num % 10
    num //= 10
    d1 = num % 10
    num //= 10
    return(d2*1000+d3*100+d4*10+d1)
def R(num):
    d4 = num % 10
    num //= 10
    d3 = num % 10
    num //= 10
    d2 = num % 10
    num //= 10
    d1 = num % 10
    num //= 10
    return(d4*1000+d1*100+d2*10+d3)
'''



'''
# 매우 시간이 짧은 코드

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def dslr(a,b) :
    visited = [0]*10000
    visited[a] = 1
    q = deque()
    q.append(('D',(2*a)%10000))
    if a != 0 :
        q.append(('S',a-1))
    else :
        q.append(('S',9999))
    q.append(('L',(a%1000)*10+(a//1000)))
    q.append(('R',(a//10)+(a%10)*1000))

    while q :
        command,num = q.popleft()

        if num == b :
            return command

        d = (2*num)%10000
        if num != 0 :
            s = num-1
        else :
            s = 9999
        l = (num%1000)*10+(num//1000)
        r = (num//10)+(num%10)*1000
        
        if d == b :
            return command+"D"
        else :
            if visited[d] == 0 :
                q.append((command+"D",d))
                visited[d] = 1
        if s == b :
            return command+"S"
        else :
            if visited[s] == 0 :
                q.append((command+"S",s))
                visited[s] = 1
        if l == b :
            return command+"L"
        else :
            if visited[l] == 0 :
                q.append((command+"L",l))
                visited[l] = 1
        if r == b :
            return command+"R"
        else :
            if visited[r] == 0 :
                q.append((command+"R",r))
                visited[r] = 1

for _ in range(t) :
    a,b = map(int,input().split())
    print(dslr(a,b))
'''