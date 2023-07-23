'''
괄호의 값

() []를 이용해 만들어지는 괄호열 중 올바른 괄호열에 대해 계산.
() 값은 2 [] 값은 3
(x) 값은 2*x
[x] 값은 3*x
붙어있으면 덧셈

입력
괄호 문자열 제시

출력
괄호열이 나타내는 값 출력. 올바르지 못하다면 0이다.
'''
sl = list(input().rstrip())
stk = []
def lego():
    ans, iv = 0, 0
    while sl:
        v = sl.pop(0)
        if v == "(":
            stk.append(v)
        elif v == ")":
            try:
                if stk.pop() == "(":
                    if iv:
                        iv*=2
                    else:
                        iv+=2
                if not stk:
                    ans+=iv
                    iv = 0
            except:
                return 0
        elif v == "[":
            stk.append(v)
        elif v == "]":
            try:
                if stk.pop() == "[":
                    if iv:
                        iv*=3
                    else:
                        iv+=3
                if not stk:
                    ans+=iv
                    iv = 0
            except:
                return 0
        print(ans, iv, stk, v)
    if stk:
        return 0
    return ans
print(lego())

sl = input().rstrip()
stk = []
ans, ret = 0, 1
for i in range(len(sl)):
    b = sl[i]   
    if b == '(':
        ret *= 2
        stk.append(b)
    elif b == '[':
        ret *= 3
        stk.append(b)
    elif b == ')':
        if not stk or stk[-1] == '[':
            ans = 0
            break
        if sl[i-1] == '(':
            ans += ret
        ret //= 2
        stk.pop()  
    else:
        if not stk or stk[-1] == '(':
            ans = 0
            break
        if sl[i-1] == '[':
            ans += ret
        ret //= 3
        stk.pop() 

if stk:
    ans = 0
print(ans)
