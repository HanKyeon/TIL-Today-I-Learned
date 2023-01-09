'''
물통

용량이 다른 두 개의 빈 물통 a, b 존재.
채우고 비워 원하는 상태가 되도록 만들 것.
쿼리는 3종.
F(x) : 물통 x에 물을 가득 채운다. 비었든 말든
E(x) : 물통 x의 물을 모두 버린다.
M(x,y) : x의 물을 y에 전부 붓는다. 부을 수 있는 만큼 싹 다.

두 물통의 용량과 원하는 최종 상태를 받은 후, 두 물통이 비어있는 상ㅇ태에서 시작하여 최종 상태까지 도달하기 위한 최소 작업 수를 구해라.

입력
용량 a, b 제시. 1이상 10만이하. 최종 상태에서 a에 남겨야 하는 물의 용량 c, b에 남겨야 하는 용량 d 제시.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global a,b,c,d
    q = deque([(0, 0, 0)])
    while q:
        fst, snd, cnt = q.popleft()
        if fst == c and snd == d:
            return cnt
        if fst < a:
            if not (a, snd) in v:
                v.add((a, snd))
                q.append((a, snd, cnt+1))
            if fst+snd <= a and not (fst+snd, 0) in v:
                v.add((fst+snd, 0))
                q.append((fst+snd, 0, cnt+1))
            elif fst+snd > a and not (a, snd-a+fst) in v:
                v.add((a, snd-a+fst))
                q.append((a, snd-a+fst, cnt+1))
        if snd < b:
            if not (fst, b) in v:
                v.add((fst, b))
                q.append((fst, b, cnt+1))
            if fst+snd <= b and not (0, fst+snd) in v:
                v.add((0, fst+snd))
                q.append((0, fst+snd, cnt+1))
            elif fst+snd > b and not (fst-b+snd, b) in v:
                v.add((fst-b+snd, b))
                q.append((fst-b+snd, b, cnt+1))
            # 마찬가지.
        if fst and not (0, snd) in v:
            v.add((0, snd))
            q.append((0, snd, cnt+1))
        if snd and not (fst, 0) in v:
            v.add((fst, 0))
            q.append((fst, 0, cnt+1))
    return -1

a, b, c, d = map(int, input().rstrip().split())
v = {(0, 0)} # 방문 배열을 set가 아닌 2차원 배열로 해도 가능할듯.
print(bfs())

'''
# 빠른 사람

a, b, a1, b1 = map(int, input().split())

def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    tmp=a%b
    while tmp!=0:
        a=b
        b=tmp
        tmp=a%b
    return abs(b)

def P1(a, b, a1, b1):
    result=0
    while True:
        if a1==b1==0:
            return result
        if a==a1:
            if a-b+b1>=0:
                a1,b1 = a-b+b1,b
            else:
                a1,b1 = 0,b1+a
        elif b==b1:
            b1=0
        elif a1==0:
            a1=a
        elif b1==0:
            a1, b1=0,a1
        else:
            return -1
        result+=1

def P2(a, b, a1, b1):
    result=0
    while True:
        if a1==b1==0:
            return result
        if b==b1:
            a1,b1=a,b-a+a1
        elif a==a1:
            a1=0
        elif b1==0:
            b1=b
        elif a1==0:
            if b1-a>0:
                a1, b1=a,b1-a
            else:
                a1,b1=b1,0
        else:
            return -1
        result+=1

if gcd(b1,a1)%gcd(b,a)!=0:
    print(-1)
elif a1==a and b1==b:
    print(2)
else:
    print(min(P1(a, b, a1, b1),P2(a, b, a1, b1)))
'''




