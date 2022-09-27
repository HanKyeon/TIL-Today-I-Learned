'''
이진탐색 구현
'''

def bs(li, tg):
    sta, end = 0, len(li)-1
    cnt = 0
    check = []
    while sta <= end:
        mid = (sta+end)//2
        if li[mid] == tg:
            return True
        if li[mid] > tg:
            if not check:
                check.append(1)
            elif check and check[-1] == 1:
                return False
            check.append(1)
            check.pop(0)
            end = mid-1
            cnt+=1
        else:
            if not check:
                check.append(0)
            elif check and check[-1] == 0:
                return False
            check.append(0)
            check.pop(0)
            sta = mid+1
            cnt+=1
    return False

for tc in range(1, int(input())+1):
    a, b = map(int, input().rstrip().split())
    al, bl = list(map(int, input().rstrip().split())), list(map(int, input().rstrip().split()))
    al.sort()
    ans = 0
    for i in bl:
        a = bs(al, i)
        if a:
            ans += 1
    print(f"#{tc} {ans}")




