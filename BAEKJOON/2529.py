'''
부등호

<와 >가 k개 나열된 순서열 A 존재. 앞뒤로 서로 다른 한자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려 한다.

입력
부등호 갯수 k 제시
부등호 공백 구분 제시

출력
k+1자리의 최대 최소 정수를 첫째 줄과 둘때 줄에 각각 출력해야 한다. 첫자리가 0인 경우도 포함됨
'''
def check():
    global mans, n
    if mans: return
    if len(stk) == n+1: mans = ''.join(map(str, stk))
    for i in range(10):
        if mans: return
        if not stk: v[i]=1; stk.append(i); check(); v[i]=0; stk.pop(); continue
        if v[i]: continue
        if bdh[len(stk)-1] == '>' and stk[-1] > i: v[i]=1; stk.append(i); check(); v[i]=0; stk.pop()
        elif bdh[len(stk)-1] == '<' and stk[-1] < i: v[i]=1; stk.append(i); check(); v[i]=0; stk.pop()

def maxCheck():
    global MANS, n
    if MANS: return
    if len(stk) == n+1: MANS = ''.join(map(str, stk))
    for i in range(9, -1, -1):
        if MANS: return
        if not stk: v[i]=1; stk.append(i); maxCheck(); v[i]=0; stk.pop(); continue
        if v[i]: continue
        if bdh[len(stk)-1] == '>' and stk[-1] > i: v[i]=1; stk.append(i); maxCheck(); v[i]=0; stk.pop()
        elif bdh[len(stk)-1] == '<' and stk[-1] < i: v[i]=1; stk.append(i); maxCheck(); v[i]=0; stk.pop()

n = int(input())
bdh = list(input().split())
mans, MANS = '', ''
v, stk = [0]*10, []
check()
v, stk = [0]*10, []
maxCheck()
print(MANS)
print(mans)