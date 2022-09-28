'''
연산

자연수 n에서 몇 번의 연산을 통해 다른 자연수 m을 만들려 한다.

사용 할 수 있는 연산이 +1 -1 *2 -10 네가지 일 때, 최소 몇 번의 연산을 거쳐야 하는지 구해라. 연산 중간 결과도 항상 100만이하 자연수.
'''
from collections import deque

def bfs(sta, end):
    if sta == end:
        return 0
    q = deque([(sta, 0)])
    v = [0]*(end+5)
    v[sta] = 1
    while q:
        num, cnt = q.popleft()
        if 0 < num*2 <= end+4 and not v[num*2]:
            if num*2 == end:
                return cnt+1
            v[num*2] = 1
            q.append((num*2, cnt+1))

        if 0 < num+1 <= end+4 and not v[num+1]:
            if num+1 == end:
                return cnt+1
            v[num+1] = 1
            q.append((num+1, cnt+1))

        if 0 < num-10 <= end+4 and not v[num-10]:
            if num-10 == end:
                return cnt+1
            v[num-10] = 1
            q.append((num-10, cnt+1))

        if 0 < num-1 <= end+4 and not v[num-1]:
            if num-1 == end:
                return cnt+1
            v[num-1] = 1
            q.append((num-1, cnt+1))

for tc in range(1, int(input())+1):
    sta, end = map(int, input().rstrip().split())
    print(f"#{tc} {bfs(sta, end)}")














