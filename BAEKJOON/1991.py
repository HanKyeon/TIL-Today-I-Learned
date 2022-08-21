'''
트리 순회

전위순회 루트 좌식 우식
중위순회 좌식 루트 우식
후위순회 좌식 우식 루트
세개 출력해라

입력
노드갯수 1이상 26이하 N
노드이름 좌식 우식 N번 제시 없으면 .

출력
전위 순회 순서
중위 순회 순서
후위 순회 순서

'''
def 전위(a):
    global ans
    l, r, alp = a
    ans += chr(alp+65)
    if l != '.':
        전위(tr[l])
    if r != '.':
        전위(tr[r])
    return ans

def 중위(a):
    global ans
    l, r, alp = a
    if l != '.':
        중위(tr[l])
    ans += chr(alp+65)
    if r != '.':
        중위(tr[r])
    return ans

def 후위(a):
    global ans
    l, r, alp = a
    if l != '.':
        후위(tr[l])
    if r != '.':
        후위(tr[r])
    ans += chr(alp+65)
    return ans

n = int(input())
tr = {}
for i in range(n):
    ro, le, ri = input().split()
    tr[ro] = (le, ri, ord(ro)-65)
ans = ''
print(전위(tr['A']))
ans = ''
print(중위(tr['A']))
ans = ''
print(후위(tr['A']))






