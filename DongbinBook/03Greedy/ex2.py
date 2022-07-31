'''
모험가 길드
'''

import gc


n = int(input())

l = list(map(int, input().split()))

l.sort()

gc, pc = 0, 0

for i in l :
    pc += 1
    if pc >= i :
        gc += 1
        pc = 0

print(gc)

