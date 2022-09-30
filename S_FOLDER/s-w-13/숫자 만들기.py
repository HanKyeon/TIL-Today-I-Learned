'''
숫자 만들기.

사칙연산 공부. 오른쪽에서 차례대로 계산.
연산자 카드를 사용하여 수식 계산 했을 때, 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력.

입력
테케T
n 제시
+ - * / 갯수 제시.
n개 숫자가 순서대로 공백을 사이에 두고 제시.

출력
#테케T 테케의 답 출력.
'''
def dfs(idx, val, yn):
    global ansM, ansm
    if yn == 0:
        val += nl[idx+1]
    elif yn == 1:
        val -= nl[idx+1]
    elif yn == 2:
        val *= nl[idx+1]
    elif yn == 3:
        if val >= 0:
            val //= nl[idx+1]
        else:
            val *= -1
            val //= nl[idx+1]
            val *= -1
    if idx == n-2:
        ansM, ansm = max(ansM, val), min(ansm, val)
        return
    for i in range(4):
        if not ysz[i]:
            continue
        ysz[i] -= 1
        dfs(idx+1, val, i)
        ysz[i] += 1

for tc in range(1, int(input())+1):
    n = int(input())
    ysz = list(map(int, input().rstrip().split()))
    nl = list(map(int, input().rstrip().split()))
    ansM, ansm = -int(10e9), int(10e9)
    for i in range(4):
        if not ysz[i]:
            continue
        ysz[i] -= 1
        dfs(0, nl[0], i)
        ysz[i] += 1
    print(f"#{tc} {ansM-ansm}")









