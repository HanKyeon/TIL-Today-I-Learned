
a = int(input())
s = 0
k = 0

def re (x) :
    global s
    global k
    if s < x :
        k += 1
        s += k
        re(x)

re(a)
print(k)

