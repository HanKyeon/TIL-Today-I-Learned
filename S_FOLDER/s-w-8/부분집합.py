'''
부분집합

n은 1~12 k는 1~100
'''

for testcase in range(1, int(input())+1):
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        bb = []
        for j in range(n):
            if i & (1<<j):
                bb.append(nl[j])
        if sum(bb) == k:
            ans += 1
    print(f"#{testcase} {ans}")
