'''
카드2

n장의 카드. 1부터 n까지. 1번이 젤 위 n이 젤 아래.
젤 위 카드 버린다.
젤 위 카드 젤 아래로.
마지막에 남는 카드는?
'''
from collections import deque

q = deque(range(int(input())))
fla = False
while len(q) != 1:
    num = q.popleft()
    fla = ~fla
    if fla:
        continue
    q.append(num)
print(q[0]+1)







