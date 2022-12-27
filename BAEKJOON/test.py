n, m = int(input()), int(input())
for i in range(m):
    a, b = map(int, input().rstrip().split())
    n -= a*b
if n:
    print("No")
else:
    print("Yes")