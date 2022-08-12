
def st(s):
    sl = len(s)
    a = [None] * sl
    for i in range(sl):
        a[i], a[sl-i-1] = s[sl-i-1], s[i]
    return str(a)

stt="hello"
ts = ''
for ch in stt:
    ts = ch+ts

print(st('aabbbccc'), ts)

def atoi(s):
    i = 0
    for x in s :
        i = i*10 + ord(x) - ord('0')
    return i

def itoa(i) :
    return chr(48+i)

# 문자열 -> 정수
st1 = '1234'
sm = 0
for ch in st1 :
    sm = sm*10+ (ord(ch) - ord('0'))
print(sm)

# 정수 -> 문자열

def itoa(i):
    i = 123
    st=''
    while i > 0:
        st = chr(i%10 + ord('0')) + st
        i //= 10
    return st

가위바위보

if i == cpu :
    res = 0
elif i == (cpu+1)%3 :
    res = 1
else :
    res = -1

이거 대신 dp로 처리 할 수 있다면? dp와 다를게 없다. 룩업테이블? 이라고 하는 듯?





