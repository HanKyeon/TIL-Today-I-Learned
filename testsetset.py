
ans = 0
for _ in range(5):
    a = int(input())
    if a < 40:
        a = 40
    ans += a//5
print(ans)


'''
from heapq import heapify, heappop

a = [55,3,21,5,6,7,3,1251,61,3,3,3,3]
print(a)
heapify(a)
print(a)
heappop(a)
heappop(a)
print(a)

'''