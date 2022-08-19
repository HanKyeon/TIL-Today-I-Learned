'''
성 지키기
'''
n, m = map(int, input().split())
g = [input() for _ in range(n)]
s = [''.join(x) for x in zip(*g)]
c, sc = 0, 0
for i in g:
    if not 'X' in i:
        c+=1
for j in s:
    if not 'X' in j:
        sc+=1
print(max(c, sc))