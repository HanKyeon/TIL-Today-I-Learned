'''
물통

부피가 A, B, C 물통 3개.
A B는 비어있고, C는 가득 차있다.
어떤 물통에 들어있는 물을 다른 물통으로 쏟을 수 있는데, 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 부을 수 있다. 손실되는 물은 없음.
세번째 물통에 담길 수 있는 물의 양을 모두 구해라.

입력
a, b, c 제시.

출력
공백 구분 오름차순 답 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
v = {(0, 0, c)}
q = deque([(0, 0, c)])
cli = {c}
while q:
    ab, bb, cb = q.popleft()
    if not ab:
        cli.add(cb)
    if ab:
        pr = min(ab, b-bb)
        if b-bb and (ab-pr, bb+pr, cb) not in v:
            v.add((ab-pr, bb+pr, cb))
            q.append((ab-pr, bb+pr, cb))
        pr = min(ab, c-cb)
        if c-cb and (ab-pr, bb, cb+pr) not in v:
            v.add((ab-pr, bb, cb+pr))
            q.append((ab-pr, bb, cb+pr))
    if bb:
        pr = min(bb, a-ab)
        if a-ab and (ab+pr, bb-pr, cb) not in v:
            v.add((ab+pr, bb-pr, cb))
            q.append((ab+pr, bb-pr, cb))
        pr = min(bb, c-cb)
        if c-cb and (ab, bb-pr, cb+pr) not in v:
            v.add((ab, bb-pr, cb+pr))
            q.append((ab, bb-pr, cb+pr))
    if cb:
        pr = min(cb, b-bb)
        if b-bb and (ab, bb+pr, cb-pr) not in v:
            v.add((ab, bb+pr, cb-pr))
            q.append((ab, bb+pr, cb-pr))
        pr = min(cb, a-ab)
        if a-ab and (ab+pr, bb, cb-pr) not in v:
            v.add((ab+pr, bb, cb-pr))
            q.append((ab+pr, bb, cb-pr))

print(*sorted(list(set(cli))))








