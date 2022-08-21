
def maxIV(li): # 리스트를 받아서 max값의 첫번째 idx와 val을 반환
    ri, rv = 0, 0
    for i in range(len(li)):
        if rv < li[i]:
            rv = li[i]
            ri = i
    return ri, rv # 값만 필요하면 rv만 리턴, 인덱스만 필요하면 ri만 리턴

def minIV(li): # 리스트를 받아서 min값의 첫번째 idx와 val을 반환
    ri, rv = 0, 100000000
    for i in range(len(li)):
        if rv > li[i]:
            rv = li[i]
            ri = i
    return ri, rv # 값만 필요하면 rv만 리턴, 인덱스만 필요하면 ri만 리턴

def sumli(li): # 리스트를 받아서 합을 반환
    ret = 0
    for i in li:
        ret += i
    return ret

def idxli(li, val): # 리스트와 타겟값을 받아서 타겟값의 첫번째 인덱스를 반환
    idx = 0
    for i in range(li):
        if li[i] == val:
            idx = i
            break
    return idx
'''
index()는 그냥 리스트 컴프리헨션 쓰면 될듯?
[i for i, v in enumerate(li) if v == 타겟]
'''

def qs(li): # 퀵 소트
    if len(li) == 1:
        return li
    p = li[0]
    t = li[1:]
    ls = [x for x in t if x <= p]
    rs = [x for x in t if x > p]
    return qs(ls) + [p] + qs(rs)

def rvs(li): # 뒤집개
    n = len(li)
    m = n//2
    for i in range(m):
        li[i], li[n-1-i] = li[n-1-i], li[i]
    return li




