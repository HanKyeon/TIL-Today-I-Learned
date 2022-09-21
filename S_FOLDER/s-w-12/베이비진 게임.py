'''
베이비진 구현
'''

def check():
    li = [0]*10
    for i in set(nl):
        li[i] = nl.count(i)
    k = 0
    gin = 0
    while k <= 7:
        if li[k] == 0:
            k+=1
            continue
        if sum(li[k:k+3]) % 3:
            k+=1
        else:
            gin += sum(li[k:k+3])//3
            k += 3
    if gin == 2:
        return 1
    else:
        return 0

for testcase in range(1, int(input())+1) :
    nl = list(map(int, list(input())))
    nl.sort()
    print(f"#{testcase} {check()}")









