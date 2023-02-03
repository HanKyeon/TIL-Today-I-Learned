'''
A -> B

A를 B로 바꿀 것.
*2
*10+1
연산 최소 횟수.

입력
a, b 제시

출력
필요한 연산의 최솟값에 1 더한 값 출력. 못만들면 -1
'''
from collections import deque
a, b = map(int, input().split())
q = deque([(a, 1)])
while(q):
    num, cnt = q.popleft()
    if num > b:
        continue
    if num*10+1 == b or num*2 == b:
        print(cnt+1)
        break
    q.append((num*10+1, cnt+1))
    q.append((num*2, cnt+1))
else:
    print(-1)