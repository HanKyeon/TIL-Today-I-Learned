'''
최대 상금
'''
def chanum(num, k, d):
    
    if k == 0:
        return num
    if (num, k) in d:
        return d[(num, k)]
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                cnum = list(num)
                cnum[i], cnum[j] = cnum[j], cnum[i]
                num = chanum(''.join(cnum), k-1, d )
                if (num, k) in d:
                    if d[(num, k)] < num:
                        d[(num, k)] = num
                else:
                    d[(num, k)] = num
    return d[(num, k)]

for testcase in range(1, int(input()) + 1):
    num, k = input().split()
    k = int(k)
    d = {}
    result = chanum(num, k, d)
    print(f'#{testcase} {result}')
    




