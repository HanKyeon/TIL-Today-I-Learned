'''
키로거

입력한 키 제시. 비번 알아내라. 대소문자 숫자 지우기 화살표

입력
테케T 제시
문자열 제시. 백스페이스는 -, 화살표는 <> 나머지는 비번 일부

출력
각 테케에 대해 비번 출력. 비번 길이는 항상 0이상
'''
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    l, r = [], []
    queries = deque(input().rstrip())
    while queries:
        a = queries.popleft()
        if a == '-':
            if l: l.pop()
        elif a == '<':
            if l: r.append(l.pop())
        elif a == '>':
            if r: l.append(r.pop())
        else: l.append(a)
    l.extend(reversed(r))
    print(''.join(l))

'''
# 이게 왜 시간초과?
class PW:
    def __init__(self, arr) -> None:
        self.query = arr[:]
        self.l = []
        self.r = []
    def remove(self):
        try: self.l.pop()
        except: pass
    def left(self):
        try: self.r.append(self.l.pop())
        except: pass
    def right(self):
        try: self.l.append(self.r.pop())
        except: pass
    def add(self, v):
        self.l.append(v)
    def ans(self):
        return ''.join(self.l+self.r[::-1])
    def lego(self):
        while self.query:
            s = self.query.pop(0)
            if s == '<': self.left()
            elif s == '>': self.right()
            elif s == '-': self.remove()
            else: self.add(s)
        return self.ans()

for _ in range(int(input())):
    s = PW(list(input().rstrip()))
    print(s.lego())
'''
'''
# 클래스 시간초과
class PW:
    def __init__(self, arr) -> None:
        self.pwArr = arr[:]
        self.cursor = 0
        self.ans = []
    def moveCursor(self, v):
        if v == '<':
            self.cursor -= 1 if self.cursor else 0
        elif v == '>':
            self.cursor += 1 if self.cursor < len(self.ans) else 0
    def remove(self):
        try:
            self.ans.pop(self.cursor)
            self.moveCursor('<')
        except:
            if self.cursor and self.cursor == len(self.ans): self.ans.pop()
    def add(self, v):
        self.ans.insert(self.cursor, v)
        self.moveCursor('>')
    def returnAns(self):
        return ''.join(self.ans)
    def lego(self):
        while self.pwArr:
            v = self.pwArr.pop(0)
            if v == '-': self.remove()
            elif v == '<' or v == '>': self.moveCursor(v)
            else: self.add(v)
        return self.returnAns()

for _ in range(int(input())):
    s = PW(list(input().rstrip()))
    print(s.lego())
'''


