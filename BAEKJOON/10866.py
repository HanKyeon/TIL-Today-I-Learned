'''
덱

정수 저장하는 덱 구현 후 입력되는 명령을 처리해라.

push_front X : 정수 X를 덱 앞에 넣는다.
push_back X : 정수 X를 덱 맨 뒤에 넣는다.
pop_front : 덱 가장 앞에 있는 수를 빼고 출력한다. 덱이 비었다면 -1 출력
pop_back : 덱의 가장 뒤에 있는 수를 빼고 출력한다. 덱이 비었다면 -1 출력
size : 덱 길이 출력
empty : 비어있으면 1을, 아니면 0 출력
front : 덱 가장 앞 정수 출력. 없으면 -1
back : 덱의 가장 뒤 정수 출력. 없으면 -1

입력
n 제시
명령어 제시

출력
출력해야 하는거 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    s = input().rstrip()
    try:
        a, b = s.split()
        if s[5] == "b":
            q.append(b)
        else:
            q.insert(0, b)
    except:
        if s[0] == "s":
            print(len(q))
        elif s[0] == "f":
            if q:
                print(q[0])
            else:
                print(-1)
        elif s[0] == "b":
            if q:
                print(q[-1])
            else:
                print(-1)
        elif s[0] == "e":
            if q:
                print(0)
            else:
                print(1)
        elif s[4] == "f":
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif s[4] == "b":
            if q:
                print(q.pop())
            else:
                print(-1)
