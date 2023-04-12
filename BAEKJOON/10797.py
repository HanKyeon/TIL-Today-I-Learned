
n = int(input())
nl = list(map(int, input().rstrip().split()))
nl = [i for i in nl if i%10 == n]
print(len(nl))