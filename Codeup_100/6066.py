a, b, c = map(int, input().split())

def zzakhol (x) :
    if x % 2 == 0 :
        print('zzak', end = ' ')
    else :
        print('hol', end = ' ')

zzakhol(a)
zzakhol(b)
zzakhol(c)