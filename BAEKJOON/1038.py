'''
감소하는 수

음이 아닌 정수 x의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소하면 감소하는 수.
n번째 감소하는 수를 출력해라.
0은 0번재 감소하는 수, 1은 1번째 감소하는 수. n번째 감소하는 수가 없다면 -1 출력

입력
n 제시. n은 100만 이하

출력
n번째 감소하는 수 출력
'''
def dfs():
    global n, ans, length
    if len(stk) == length:
        n -= 1
        if not n:
            print(''.join(map(str, stk)))
            exit()
    for i in range(stk[-1]):
        stk.append(i)
        dfs()
        stk.pop()

n = int(input())
if n < 10: print(n); exit()
if n > 1022: print(-1); exit()
n -= 9
stk = []
for length in range(2, 11):
    for endNum in range(10):
        stk.append(endNum)
        dfs()
        stk.pop()

'''
n = int(input())
ans = []

def decrease(x):
    ans.append(x)
    left = int(str(x)[0])
    for i in range(left+1, 10):
        decrease(int(str(i) + str(x)))

for i in range(10):
    decrease(i)
    
ans.sort()

try :
    print(ans[n])
except : 
    print(-1)
'''
