import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, value = q.popleft()
    ans.append(idx + 1)

    if value > 0:
        q.rotate(-(value - 1))
    elif value < 0:
        q.rotate(-value)

print(' '.join(map(str, ans)))