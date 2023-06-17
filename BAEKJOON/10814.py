import sys
input = sys.stdin.readline
l = [list(input().rstrip().split())for _ in range(int(input()))]
l.sort(key=lambda x: int(x[0]))
for i in l:
    print(" ".join(i))
