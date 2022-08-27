'''
좌표 정렬하기
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
nl = sorted([list(map(int, input().rstrip().split())) for _ in range(n)])
for i in nl:
    print(*i)