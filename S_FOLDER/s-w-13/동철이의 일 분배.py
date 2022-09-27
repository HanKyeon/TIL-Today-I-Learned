'''
동철이의 일 분배

N명의 직원
해야 할 일 N개
공평하게 하나씩
직원 번호 1~N. 해야 할 일 1~N.
i번 직원이 j번 일 하면 성공할 확률이 Pij.
동철이가 모든 일이 잘 풀리도록 헬프.
해야 할 일을 하나씩 배분해야한다.
주어진 일이 모두 성공 할 확률의 최댓값을 구하는 프로그램 작성.

입력
테케T
n 제시.
그래프 제시. %단위 정수.

출력
#테케T 최대화 될 때의 확률을 퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째 까지 출력
'''
def 레쓰고(dep, pct):
    global ans, n, v
    if dep == n:
        ans = max(ans, pct*100)
        return
    if pct*100 <= ans:
        return
    for i in range(n):
        if v[i]:
            continue
        v[i] = 1
        레쓰고(dep+1, pct*g[dep][i]*0.01)
        v[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    g = [list(map(float, input().rstrip().split())) for _ in range(n)]
    v = [0]*n
    ans = 0
    for i in range(n):
        v[i] = 1
        레쓰고(1, g[0][i]*0.01)
        v[i] = 0
    print(f"#{tc} {ans:.6f}")














