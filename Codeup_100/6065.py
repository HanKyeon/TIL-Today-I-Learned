a, b, c = map(int, input().split())

def zzak (x, y, z) :
    if x % 2 == 0 :
        print(x, end = ' ')
    if y % 2 == 0 :
        print(y, end = ' ')
    if z % 2 == 0 :
        print(z, end = ' ')

zzak(a, b, c)