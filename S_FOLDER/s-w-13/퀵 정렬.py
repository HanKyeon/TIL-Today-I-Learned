'''
퀵 정렬 구현
'''

def qs(li):
    if len(li)<=1:
        return li
    pv = li[0]
    li = li[1:]
    left, right = [i for i in li if i <= pv], [i for i in li if i > pv]
    return qs(left)+[pv]+qs(right)

for tc in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().split()))
    nl = qs(nl)
    print(f"#{tc} {nl[n//2]}")




