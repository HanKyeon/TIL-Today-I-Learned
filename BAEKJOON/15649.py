'''
N과 M (1)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

입력
N과 M 제시. 1이상 M N 8이하

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열.
'''
from itertools import permutations

n, m = map(int, input().split())
nl = list(range(1, n+1))
ans = []
ans += list(permutations(nl, m))
for i in sorted(ans):
    print(*i)
