'''
연산자 끼워넣기

N개의 수로 이루어진 수열
N-1개의 연산자
예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고
덧셈 2개, 뺄셈 1개, 곱셈 1개, 나눗셈 1개인 경우에는 총 60가지의 식
1. 우선순위 무시하고 앞에서부터 진행
2. 나눗셈 : 몫만 취함
3. 음수를 나눌 때 : 양수로 바꾼 뒤 몫을 취하고 음수로 바꿈.
가능한 최댓값과 최솟값 출력

입력
2이상 11이하 N
수열1 수열2 수열3 수열4.. 수열n
덧 빼 곱 나 갯수
'''
def dfs(num, idx, cali): # 저장된 숫자, 다음 숫자 인덱스, 계산 인덱스
    global mx, mn
    if cal[cali] > 0: # 연산자 소모
        cal[cali] -= 1
    if cali == 0: # 덧셈이면 더하고
        num += nl[idx]
    if cali == 1: # 뺄셈이면 빼고
        num -= nl[idx]
    if cali == 2: # 곱셈이면 곱하고
        num *= nl[idx]
    if cali == 3: # 나눗셈이면 나누는데
        if num < 0: # 음수 조건 처리해주고
            num = -((-num)//nl[idx])
        else: # 아니면 그냥 몫만 취한다.
            num //= nl[idx]
    if idx == n-1: # 곱해지는 수의 idx가 맨 끝이면
        if mx < num : # 최댓값 기록
            mx = num
        if mn > num : # 최솟값 기록
            mn = num
        return # 종료

    for i in range(4): # cal 순회할거다.
        if cal[i] == 0: # 연산자 없으면 넘기고
            continue
        elif cal[i] != 0: # 연산자 있으면 dfs 해봐라.
            dfs(num, idx+1, i)
            cal[i] += 1 # 다음 순회를 위해 복원해주고.

n = int(input()) # 수열 길이
nl = list(map(int, input().split())) # 수열
cal = list(map(int, input().split())) # 덧 빼 곱 나 0 1 2 3
mx, mn = -1000000000, 1000000000 # 최대, 최소 저장 할 것
for i in range(4): # 연산자 순회 할 것임
    if cal[i] != 0: # 연산자 채워져 있으면
        dfs(nl[0], 1, i) # dfs 실행
        cal[i]+=1 # 반복하므로 복구해준다.
print(mx)
print(mn)



