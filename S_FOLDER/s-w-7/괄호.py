for t in range(1, int(input())+1):
    c = 0
    s = input()
    for i in s:
        if i == '(':
            c += 1
        if i == ')':
            c -= 1
        if c < 0:
            break
    if c == 0:
        print(f'#{t} 1')
    if c != 0:
        print(f'#{t} 0')