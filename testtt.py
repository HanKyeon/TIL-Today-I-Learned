n = int(input())
for i in range(n):print(" "*i + "*"*(n-i))

ans = [0]*26
s = input()
for i in s:
    ans[ord(i)-97] += 1
print(*ans)

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
# import sys
# input = sys.stdin.readline

# n = int(input())
# nl = list(map(int, input().rstrip().split()))
# m, M = 1000000, -1000000
# for i in nl:
#     if m > i:
#         m = i
#     if M < i:
#         M = i
# print(m, M)
a = [
    [
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
    ],
    [
        [0,1,0,0],
        [1,1,1,1],
        [1,0,0,0],
    ],
    [
        [0,0,1,0],
        [1,1,1,1],
        [1,0,0,0],
    ],
    [
        [0,0,0,1],
        [1,1,1,1],
        [1,0,0,0],
    ],
    [
        [1,0,0,0],
        [1,1,1,1],
        [0,1,0,0],
    ],
    [
        [0,1,0,0],
        [1,1,1,1],
        [0,1,0,0],
    ],
    [
        [0,0,1,0],
        [1,1,1,1],
        [0,1,0,0],
    ],
    [
        [0,0,0,1],
        [1,1,1,1],
        [0,1,0,0],
    ],
    [
        [1,0,0,0],
        [1,1,1,1],
        [0,0,1,0],
    ],
    [
        [0,1,0,0],
        [1,1,1,1],
        [0,0,1,0],
    ],
    [
        [0,0,1,0],
        [1,1,1,1],
        [0,0,1,0],
    ],
    [
        [0,0,0,1],
        [1,1,1,1],
        [0,0,1,0],
    ],
    [
        [1,0,0,0],
        [1,1,1,1],
        [0,0,0,1],
    ],
    [
        [0,1,0,0],
        [1,1,1,1],
        [0,0,0,1],
    ],
    [
        [0,0,1,0],
        [1,1,1,1],
        [0,0,0,1],
    ],
    [
        [0,0,0,1],
        [1,1,1,1],
        [0,0,0,1],
    ],
    [
        [0,0,1,1,1],
        [1,1,1,0,0]
    ],
    [
        [1,1,1,0,0],
        [0,0,1,1,1]
    ],
    [
        [0,0,1,1],
        [0,1,1,0],
        [1,1,0,0]
    ],
    [
        [1,1,0,0],
        [0,1,1,0],
        [0,0,1,1]
    ],
    [
        [0,0,1,1],
        [1,1,1,0],
        [1,0,0,0]
    ],
    [
        [1,0,0,0],
        [1,1,1,0],
        [0,0,1,1],
    ],
    [
        [1,1,0,0],
        [0,1,1,1],
        [0,0,0,1]
    ],
    [
        [0,0,0,1],
        [0,1,1,1],
        [1,1,0,0],
    ],
    [
        [1,1,0,0],
        [0,1,1,1],
        [0,1,0,0]
    ],
    [
        [0,1,0,0],
        [0,1,1,1],
        [1,1,0,0],
    ],
    [
        [0,0,1,1],
        [1,1,1,0],
        [0,0,1,0]
    ],
    [
        [0,0,1,0],
        [1,1,1,0],
        [0,0,1,1],
    ],
    [
        [0,1,0,0],
        [1,1,1,0],
        [0,0,1,1]
    ],
    [
        [0,0,1,1],
        [1,1,1,0],
        [0,1,0,0],
    ],
    [
        [0,0,1,0],
        [0,1,1,1],
        [1,1,0,0]
    ],
    [
        [1,1,0,0],
        [0,1,1,1],
        [0,0,1,0],
    ],
]
zgds = set()
for i in a:
    ti = tuple(map(tuple, i))
    # 상하반전 = tuple(map(tuple, reversed(i)))
    전치 = tuple(zip(*i))
    zgds.add(ti)
    # zgds.add(상하반전)
    zgds.add(전치)

for _ in range(3):
    g = [list(map(int, input().rstrip().split())) for _ in range(6)]
    mh, Mh, mw, Mw = 8, 0, 8, 0
    for i in range(6):
        for j in range(6):
            if g[i][j]:
                mh, Mh, mw, Mw = min(mh, i), max(Mh, i), min(mw, j), max(Mw, j)
    zgd = []
    for i in range(mh, Mh+1):
        zgd.append(g[i][mw:Mw+1])
    zgd = tuple(map(tuple, zgd))
    if zgd in zgds:
        print('yes')
    else:
        print('no')
