def rvs(li): # 뒤집개
    n = len(li)
    m = n//2
    for i in range(m):
        li[i], li[n-1-i] = li[n-1-i], li[i]
    return li

def qs(li):
    if len(li) <= 1:
        return li
    p = li[0]
    t = li[1:]
    ls = [x for x in t if x<=p]
    rs = [x for x in t if x>p]
    return qs(ls)+[p]+qs(rs)

a = [1,2, 0, 5, 6, 99, 123, 1,3,4,5,6]
print(rvs(a))
print(qs(a))