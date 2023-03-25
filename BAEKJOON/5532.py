'''

l, a, b, c, d 입력 받는다.
a/c b/c 중 큰 값을 l에서 빼라
'''

l,a,b,c,d=int(input()),int(input()),int(input()),int(input()),int(input())
a=a//c+1 if a%c else a//c
b=b//d+1 if b&d else b//d
print(l-max(a,b))
a, b = a//c+1 if a%c else a//c, b//d+1 if b&d else b//d