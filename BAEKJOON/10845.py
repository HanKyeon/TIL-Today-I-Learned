'''
큐

6개 명령대로 실행.
push X : x를 큐에 넣기
pop : 가장 앞에 있는거 popleft 후 출력
size : 정수 개수 출력
empty : 비어있으면 1 아니면 0
front : 큐의 맨 앞에 있는 정수 출력. 없으면 -1
back 큐 가장 뒤의 정수 출력. 없으면 -1

입력
명령 수 n 제시
n개 줄 명령 제시.

출력
명령 따라 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def lego(mzy):
    if mzy == "p":
        if q:
            return q.popleft()
    elif mzy == "s":
        return len(q)
    elif mzy == "e":
        if q:
            return 0
        return 1
    elif mzy == "f":
        if q:
            return q[0]
    else:
        if q:
            return q[-1]
    return -1

n = int(input().rstrip())
q = deque()
for _ in range(n):
    s = input().rstrip()
    try:
        int(s[-1])
        a, b = s.split()
        q.append(b)
    except:
        print(lego(s[0]))







