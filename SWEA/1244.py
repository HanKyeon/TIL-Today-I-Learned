'''
최대 상금
'''
def find_max_price(number, k, memo):
    if k == 0:
        return number
    if (number, k) in memo:
        return memo[(number, k)]
    for i in range(len(number)):
        for j in range(len(number)):
            if i != j:
                number2 = list(number)
                number2[i], number2[j] = number2[j], number2[i]
                num = find_max_price(''.join(number2), k-1, memo)
                if (number, k) in memo:
                    if memo[(number, k)] < num:
                        memo[(number, k)] = num
                else:
                    memo[(number, k)] = num
    return memo[(number, k)]

T = int(input())
for tc in range(1, T + 1):
    num, k = input().split()
    k = int(k)
    result = find_max_price(num, k, {})
    print(f'#{tc} {result}')
    




