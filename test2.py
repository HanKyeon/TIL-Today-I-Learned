T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    ans = 0
    k = 0
    N = len(lst) # N bit (lst member: N)

    for bit in range(1, 2**N): # == 1<<N
        sm = 0
        for i in range(0, N): # every lst index
            if bit & (1 << i):
                sm += lst[i]
            
        if sm == k:
            ans = 1
            break
    print(f'#{test_case} {ans}')

    arr = [3,6,7,1,5,4]

