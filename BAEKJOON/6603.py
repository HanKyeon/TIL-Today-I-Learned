'''
로또

1~49 중 6개
집합 S와 K가 주어졌을 때 수를 고르는 모든 방법을 구해라.

입력
한 줄로 제시. k s s s s s s
마지막 0 제시
'''
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    s = list(map(int, input().rstrip().split()))
    k = s.pop(0)
    if not k:
        break
    ans = []
    for i in combinations(s, 6):
        ans.append(sorted(i))
    ans.sort()
    for i in ans:
        print(*i)
    print()

