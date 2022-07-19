a = int(input())

def zzakhol (x) :
    if (x % 2 == 0) and (x < 0) :
        print('A')
    elif (x % 2 == 1) and (x < 0):
        print('B')
    elif (x % 2 == 0) and (x > 0):
        print('C')
    elif (x % 2 == 1) and (x > 0):
        print('D')
    else :
        print('error')

zzakhol(a)
