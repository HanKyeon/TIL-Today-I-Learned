'''
모든 순열

n이 주어졌을 때, 1부터 n까지 수로 이루어진 순열을 사전순으로 출력해라.

입력
n 제시

출력
n!개 줄 걸쳐 순열 사전순 출력
'''
from itertools import permutations
n = int(input())
for i in sorted(permutations(range(1, n+1), n)): print(*i)
