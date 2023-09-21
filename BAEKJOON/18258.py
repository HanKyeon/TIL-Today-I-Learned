'''
큐2

정수 저장 큐 구현, 입력으로 주어지는 명령 처리

push X : 정수를 큐에 넣는다
pop: 가장 앞에 잇는 정수 빼고 그 수 출력. 없으면 -1 출력
size: 정수 갯수 출ㄹ력
empty: 비어있으면 1 아니면 0
front: 가장 앞에 있는 정수 출력. 없으면 -1
back: 가장 뒤에 있는 정수 출력. 없으면 -1
'''
import sys
from collections import deque
input = sys.stdin.readline

class Q:
    def __init__(self): self.q = deque()
    def push(self, x): self.q.append(x)
    def pop(self):
        try: print(self.q.popleft())
        except: print(-1)
    def size(self): print(len(self.q))
    def empty(self): print(0 if len(self.q) else 1)
    def front(self):
        try: print(self.q[0])
        except: print(-1)
    def back(self):
        try: print(self.q[-1])
        except: print(-1)
    def lego(self, s: str):
        ns = s.split()
        if ns[0] == 'push': self.push(ns[1]); return
        if ns[0] == 'front': self.front(); return
        if ns[0] == 'pop': self.pop(); return
        if ns[0] == 'size': self.size(); return
        if ns[0] == 'empty': self.empty(); return
        if ns[0] == 'back': self.back(); return

q = Q()
for _ in range(int(input().rstrip())): q.lego(input().rstrip())
