'''
0과 1

0과 1로만 이루어져 있어야 하고
1이 적어도 하나 있어야 하과
길이가 100이하여야 하고
0으로 시작하지 않는다.
위의 조건을 만족하는 수를 좋아한다.
자연수 n 제시. n배수 중 구사과가 좋아하느 수를 구해라.

입력
테케T 제시
T개 줄 자연수 n 제시. n은 2만 이하 자연수

출력
n배수면서 좋아하는 수 출력. 없다면 BRAK 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

def lego():
    n = int(input())
    q = deque([(1, '1')])
    v = [0,1]+[0]*19999
    while q:
        mn, num = q.popleft()
        if mn == 0:
            return num
        if len(num) > 100:
            return 'BRAK'
        # x % n은 (x % n) % n과 같음
        if not v[(mn*10)%n]:
            v[(mn*10)%n] = 1
            q.append(((mn*10)%n, num + '0'))
        if not v[(mn*10+1)%n]:
            v[(mn*10+1)%n] = 1
            q.append(((mn*10+1)%n, num + '1'))
    return 'BRAK'

ans = []
for _ in range(int(input())):
    ans.append(lego())
for i in ans:
    print(i)

'''
# 압도적으로 빠른 코드

import sys


def main():
    input = sys.stdin.readline

    for _ in range(int(input())):
        n = int(input())
        print(smallest_multiple(n))


def smallest_multiple(n):
    if n == 1:
        return "1"

    visited = [0] * (n + 1)
    parent = [0] * (n + 1)
    used_digit = [0] * (n + 1)
    queue = [1]

    for num_digits in range(100):
        next_queue = []

        for remainder in queue:
            for digit in [0, 1]:
                next_remainder = (remainder * 10 + digit) % n
                if visited[next_remainder] == 0:
                    visited[next_remainder] = 1
                    parent[next_remainder] = remainder
                    used_digit[next_remainder] = digit
                    if next_remainder == 0:
                        break
                    next_queue.append(next_remainder)
            else:
                continue
            break

        if parent[0] != 0:
            break

        queue = next_queue

    if parent[0] == 0:
        return "BRAK"

    ans = []
    current = 0
    while current != 1:
        ans.append(str(used_digit[current]))
        current = parent[current]
    ans.append("1")
    return "".join(reversed(ans))


main()

'''










