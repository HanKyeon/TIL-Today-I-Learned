'''
서점왕 김장훈

높이 B 선반. 선반 쌉가능
n명의 점원들이 선반 위 물건 사용해야 한다.
점원의 키는 Hi로 제시.
점원 탑을 쌓아 선반 위 물건 사용.
탑 높이는 점원 키의 합과 같다.
탑의 높이가 B 이상인 경우 선반 위의 물건을 사용 할 수 있는데 탑의 높이가 높을수록 더 위험하므로 높이가 B이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.

입력
테케T
두 정수 n, b 제시.
s는 두 번째 줄에서 주어지는 점원들 키의 합.
두 번째 줄에는 n개의 정수가 공백 구분 세지, 각 정수는 각 점원의 키를 나타낸다.

출력
#테케 만들 수 있는 높이가 B이상인 탑 중에서 탐의 높이가 B와 차이가 가장 작은 것
'''
def dfs(idx, val):
    global ans
    if val >= b:
        ans = min(ans, abs(b-val))
        return
    for i in range(idx+1, n):
        if v[i]:
            v[i] = 0
            dfs(i, val+kz[i])
            v[i] = 1

for tc in range(1, int(input())+1):
    n, b = map(int, input().rstrip().split())
    kz = list(map(int, input().rstrip().split()))
    if sum(kz) < b:
        print(f"#{tc} {b-sum(kz)}")
        continue
    if sum(kz) == b:
        print(f"#{tc} {0}")
        continue
    v = [1]*n
    ans = int(10e9)
    for i in range(n):
        v[i] = 0
        dfs(i, kz[i])
        v[i] = 1
    
    print(f"#{tc} {ans}")













