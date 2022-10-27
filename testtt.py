'''
arr = [2, 3, 4]
subsets = [[]]
for num in arr:
    print(num)
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])
print(subsets)
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
m, M = 1000000, -1000000
for i in nl:
    if m > i:
        m = i
    if M < i:
        M = i
print(m, M)


